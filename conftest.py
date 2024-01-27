import functools
import pytest
from app import app
from automation_infra.managers.bot_manager import BotManager

from automation_infra.utils.log_handler import LoggingSettings


def pytest_addoption(parser):
    parser.addoption("--log_level", action="store", default="INFO", help="Set the log level for Loguru")


def pytest_sessionstart(session):
    log_level = session.config.getoption("--log_level").upper()
    logs_settings = LoggingSettings(log_level=log_level, log_path='automation_infra/automation_logs')
    logs_settings.configure_logs()


@pytest.fixture(scope="session", autouse=True)
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture(scope="session", autouse=True)
def bot_manager(client):
    return BotManager(client=client)


def pass_if_failed(test_func):
    @functools.wraps(test_func)
    def wrapper(*args, **kwargs):
        try:
            test_func(*args, **kwargs)
            assert False, "Test unexpectedly passed"
        except Exception:
            pass  # Test failed, which is the desired outcome

    return wrapper
