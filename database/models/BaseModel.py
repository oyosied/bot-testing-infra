from abc import ABC, abstractmethod


class BaseModel(ABC):

    @abstractmethod
    def insert(self,new_item):
        pass

    @abstractmethod
    def update(self,item_id,updated_fields):
        pass

    @abstractmethod
    def delete(self,item_id):
        pass
