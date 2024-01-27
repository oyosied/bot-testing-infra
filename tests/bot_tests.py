import random
import time

from automation_infra.properties.bot_properties import BotProperties
from common.common import ALLOWED_INTENTS
from conftest import pass_if_failed


class TestsBotAPI:

    @pass_if_failed
    def test_get_bot_bad_name(self, bot_manager):
        bot_manager.get_bot(bot_name=f"testing_{str(int(time.time() * 1000))}")

    @pass_if_failed
    def test_create_bot_empty_intents(self, bot_manager):
        bot_properties = BotProperties(name="sample-bot", url="http://example.com", intents=[])
        bot_manager.create_bot(bot_properties=bot_properties)

    @pass_if_failed
    def test_create_bot_bad_intents(self, bot_manager):
        bot_properties = BotProperties(name="sample-bot", url="http://example.com", intents=[''])
        bot_manager.create_bot(bot_properties=bot_properties)

    @pass_if_failed
    def test_create_bot_bad_url(self, bot_manager):
        bot_properties = BotProperties(name="sample-bot", url="", intents=[random.choice(ALLOWED_INTENTS)])
        bot_manager.create_bot(bot_properties=bot_properties)

    @pass_if_failed
    def test_create_bot_bad_name(self, bot_manager):
        bot_properties = BotProperties(name="", url="http://example.com", intents=[random.choice(ALLOWED_INTENTS)])
        bot_manager.create_bot(bot_properties=bot_properties)

    @pass_if_failed
    def test_create_bot_unknown_field(self, bot_manager):
        bot_properties = BotProperties(name="", url="http://example.com", intents=[random.choice(ALLOWED_INTENTS)],hello_there='123')
        bot_manager.create_bot(bot_properties=bot_properties)

    @pass_if_failed
    def test_delete_bot_not_existent_name(self, bot_manager):
        bot_manager.delete_bot(bot_name=f"testing_{str(int(time.time() * 1000))}")

    def test_update_bot(self, bot_manager):
        bot_properties = BotProperties(name=f"testing_{str(int(time.time() * 1000))}", url="http://example.com",
                                       intents=[random.choice(ALLOWED_INTENTS)])
        bot_manager.create_bot(bot_properties=bot_properties)
        bot_manager.update_bot(bot_properties=bot_properties)