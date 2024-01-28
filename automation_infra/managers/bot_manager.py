from flask.testing import FlaskClient
from loguru import logger

from automation_infra.properties.bot_properties import BotProperties


class BotManager:

    def __init__(self, client: FlaskClient):
        self.client = client
        self.created_bots = []

    def get_bot(self, bot_name):
        response = self.client.get(f"/bot/{bot_name}")
        logger.info(f"Request:'/bot/{bot_name}'\n"
                    f"Response:{response.json}")
        assert response.status_code == 200

    def create_bot(self, bot_properties: BotProperties):
        response = self.client.post(f"/bot", json=bot_properties.to_dict())
        logger.info(f"Request:'/bot'\n"
                    f"Response:{response.json}\n"
                    f"Body:{bot_properties.to_dict()}")
        assert response.status_code == 200
        self.created_bots.append(bot_properties.name)


    def update_bot(self, bot_properties: BotProperties):
        response = self.client.put(f"/bot/{bot_properties.name}", json=bot_properties.to_dict())
        logger.info(f"Request:'/bot'\n"
                    f"Response:{response.json}\n"
                    f"Body:{bot_properties.to_dict()}")
        assert response.status_code == 200
        self.created_bots.append(bot_properties.name)

    def delete_bot(self, bot_name):
        response = self.client.delete(f"/bot/{bot_name}")
        logger.info(f"Request:'/bot/{bot_name}'\n"
                    f"Response:{response.json}")
        assert response.status_code == 200
        self.created_bots.remove(bot_name)


    def delete_created(self):
        for bot_name in self.created_bots:
            self.delete_bot(bot_name=bot_name)
