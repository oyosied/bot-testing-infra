# Here I am attempting to recreate sequalize framework same in NodeJS
# This will act similarly
import os

from common.common import ROOT_PATH
from database.db_handler import DatabaseHandler
from database.models.BaseModel import BaseModel

file_path = os.path.join(f"{ROOT_PATH}\\database\\", 'bot.json')
field_map = ['name', 'url', 'intents']
unique_fields = ['name']


class Bot(BaseModel):
    def __init__(self):
        self.db_handler: DatabaseHandler = DatabaseHandler(path_to_json=file_path, field_map=field_map,
                                                           unique_fields=unique_fields, primary_search_key='name')

    # bot's main index is the name, there is no search by ID
    def insert(self, new_bot):
        return self.db_handler.add_to_json(new_item=new_bot)

    def update(self, bot_name, updated_fields):
        self.db_handler.update_value(item_id=str(bot_name), updated_fields=updated_fields)

    def delete(self, bot_name):
        self.db_handler.remove_from_json(item_id=str(bot_name))

    # will search by name of the bot
    def get(self, bot_name):
        return self.db_handler.get_specific_data(item_id=str(bot_name))
