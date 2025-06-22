from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    @abstractmethod
    def get_description(self):
        pass