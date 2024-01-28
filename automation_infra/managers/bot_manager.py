from flask.testing import FlaskClient
from loguru import logger

from automation_infra.properties.bot_properties import BotProperties


class BotManager:

    def __init__(self, client: FlaskClient):
        self.client = client
        self.created_bots = []

    def get_bot(self, bot_name, expected_status_code=200):
        response = self.client.get(f"/bot/{bot_name}")
        logger.info(f"Request:'/bot/{bot_name}'\n"
                    f"Response:{response.json}\n"
                    f"Status code:{response.status_code}")
        assert response.status_code == expected_status_code

    def create_bot(self, bot_properties: BotProperties, expected_status_code=200):
        response = self.client.post(f"/bot", json=bot_properties.to_dict())
        logger.info(f"Request:'/bot'\n"
                    f"Response:{response.json}\n"
                    f"Body:{bot_properties.to_dict()}\n"
                    f"Status code:{response.status_code}")
        assert response.status_code == expected_status_code
        if response.status_code == 200:
            self.created_bots.append(bot_properties.name)

    def update_bot(self, bot_name: str, bot_properties: BotProperties, expected_status_code=200):
        response = self.client.put(f"/bot/{bot_name}", json=bot_properties.to_dict())
        logger.info(f"Request:'/bot'\n"
                    f"Response:{response.json}\n"
                    f"Body:{bot_properties.to_dict()}\n"
                    f"Status code:{response.status_code}")
        assert response.status_code == expected_status_code
        if bot_name != bot_properties.name and response.status_code == 200:
            self.created_bots.remove(bot_properties.name)
            self.created_bots.append(bot_name)

    def delete_bot(self, bot_name, expected_status_code=200):
        response = self.client.delete(f"/bot/{bot_name}")
        logger.info(f"Request:'/bot/{bot_name}'\n"
                    f"Response:{response.json}\n"
                    f"Status code:{response.status_code}")
        assert response.status_code == expected_status_code
        try:
            self.created_bots.remove(bot_name)
        except:
            pass

    def delete_created(self):
        for bot_name in self.created_bots:
            self.delete_bot(bot_name=bot_name)
