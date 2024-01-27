import json

from common.common import ROOT_PATH,CONFIG_FILE


class ConfigSettings:
    def __init__(self, log_path: str, log_level: str):
        self.log_path = log_path
        self.log_level = log_level

    @classmethod
    def load(cls) -> 'ConfigSettings':
        json_path = ROOT_PATH / CONFIG_FILE
        with open(json_path, 'r') as f:
            data = json.load(f)

        return cls(
            log_path=data.get('log_path', ''),
            log_level=data.get('log_level', '')
        )

ConfigSettings.load()