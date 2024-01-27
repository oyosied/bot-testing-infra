import json
import os
from typing import List


def commit_changes(func):
    def open_and_save_data(self, *arg, **kw):
        self.validate_path()
        with open(self.path_to_json, 'r+') as file:
            data = json.load(file)
            result = func(self, data, *arg, **kw)
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=4)
            return result

    return open_and_save_data


class DatabaseHandler:

    def __init__(self, path_to_json, field_map, unique_fields):
        self.path_to_json = path_to_json
        self.field_map = field_map
        self.unique_fields = ['id', *unique_fields]
        self.validate_path()

    def validate_path(self):
        if not os.path.exists(self.path_to_json):
            raise FileNotFoundError(f"File not found: {self.path_to_json}")

    def get_all_data(self):
        self.validate_path()
        with open(self.path_to_json, 'r+') as file:
            data = json.load(file)
            return data

    def get_specific_data(self, item_id):
        self.validate_path()
        with open(self.path_to_json, 'r+') as file:
            try:
                data = json.load(file)
                return data['items'][item_id]
            except KeyError as e:
                raise KeyError(f"Couldn't find '{item_id}'")

    def unique_field_exists(self, data, value, field_name):
        return value in data["unique_fields"][field_name]

    def check_all_unique_fields_exists(self, data, item):
        non_unique_fields = {}
        for unique_field in self.unique_fields:
            if self.unique_field_exists(data, item[unique_field], unique_field):
                non_unique_fields[unique_field] = item[unique_field]
        return non_unique_fields if non_unique_fields else False

    def add_unique_field(self, data, value, field_name):
        data["unique_fields"][field_name].append(value)
        return

    @commit_changes
    def add_to_json(self, data: dict, new_item: dict):
        current_id = data["current_id"]
        new_item = {'id': current_id, **new_item}
        existing_values = self.check_all_unique_fields_exists(data=data, item=new_item)
        if existing_values:
            raise Exception(f"Could not add '{new_item}', "
                            f"error: 'The following values already exist '{existing_values}'")

        data["items"][new_item['name']] = new_item
        data["current_id"] += 1
        for field in self.unique_fields:
            self.add_unique_field(data, new_item[field], field)
        return current_id

    def remove_unique_field_value(self, data, value, field_name):
        data["unique_fields"][field_name].remove(value)
        return

    @commit_changes
    def remove_from_json(self, data: dict, item_id: str):
        if not item_id or item_id == '':
            return "Nothing to remove"
        try:
            for field in self.unique_fields:
                self.remove_unique_field_value(data, data["items"][item_id][field], field)
            data["items"].pop(item_id)

        except KeyError as e:
            raise KeyError(f"Couldn't find '{item_id}', skipping ....")
        except Exception as e:
            raise Exception(f"Could not remove '{item_id}', error:{e}")

    @commit_changes
    def update_value(self, data: dict, item_id: str, updated_fields: dict):
        if not item_id or item_id == '':
            return "Please provide an ID"
        try:
            try:
                data["items"][item_id].update(updated_fields)
            except KeyError as e:
                raise KeyError(f"Couldn't find '{item_id}', skipping ....")
        except Exception as e:
            raise Exception(f"Could not update '{item_id}', error:{e}")
