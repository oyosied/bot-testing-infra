# Here I am attempting to recreate sequalize framework same in NodeJS
# This will act similarly
import os

from common.common import root_path
from database.db_handler import DatabaseHandler
from database.models.BaseModel import BaseModel

file_path = os.path.join(f"{root_path}\\database\\", 'bot.json')
field_map = ['name', 'url', 'intents']
unique_fields = ['name']


class Bot(BaseModel):
    def __init__(self):
        self.db_handler: DatabaseHandler = DatabaseHandler(path_to_json=file_path, field_map=field_map,
                                                           unique_fields=unique_fields)

    def insert(self, new_bot):
        return self.db_handler.add_to_json(new_item=new_bot)

    def update(self, bot_id, updated_fields):
        self.db_handler.update_value(item_id=str(bot_id), updated_fields=updated_fields)

    def delete(self, bot_id):
        self.db_handler.remove_from_json(item_id=str(bot_id))

    def get(self, bot_id):
        return self.db_handler.get_specific_data(item_id=str(bot_id))
