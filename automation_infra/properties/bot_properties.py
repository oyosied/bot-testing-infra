from typing import List


class BotProperties:
    def __init__(self, name: str, url: str, intents: List, **kwargs):
        self.intents = intents
        self.url = url
        self.name = name
        self.kwargs = kwargs

    def to_dict(self):
        return {
            "name": self.name,
            "intents": self.intents,
            "url": self.url,
            **self.kwargs
        }
