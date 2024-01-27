from flask.testing import FlaskClient
from loguru import logger

from automation_infra.properties.bot_properties import BotProperties


class BotManager:

    def __init__(self, client: FlaskClient):
        self.client = client
        self.created_bots = []
        self.deleted_bots = []

    def get_bot(self, bot_name):
        response = self.client.get(f"/bot/{bot_name}")
        logger.info(f"Request:'/bot/{bot_name}'\n"
                    f"Response:{response.json}")
        assert response.status_code == 200

    def create_bot(self, bot_properties: BotProperties):
        self.created_bots.append(bot_properties.name)
        response = self.client.post(f"/bot", json=bot_properties.to_dict())
        logger.info(f"Request:'/bot'\n"
                    f"Response:{response.json}\n"
                    f"Body:{bot_properties.to_dict()}")
        assert response.status_code == 200

    def update_bot(self, bot_properties: BotProperties):
        self.created_bots.append(bot_properties.name)
        response = self.client.put(f"/bot/{bot_properties.name}", json=bot_properties.to_dict())
        logger.info(f"Request:'/bot'\n"
                    f"Response:{response.json}\n"
                    f"Body:{bot_properties.to_dict()}")
        assert response.status_code == 200

    def delete_bot(self, bot_name):
        try:
            self.created_bots.remove(bot_name)
        except:
            pass
        response = self.client.delete(f"/bot/{bot_name}")
        logger.info(f"Request:'/bot/{bot_name}'\n"
                    f"Response:{response.json}")
        assert response.status_code == 200
