from abc import ABC, ABCMeta, abstractmethod
from enum import Enum

class AnimalType(Enum):
    DOMESTICATED = 0
    WILD = 1
    UNDEFINED = 2

class Animal(ABC):
    @property
    @abstractmethod
    def current_health(self):
        ...


    @current_health.setter
    @abstractmethod
    def current_health(self, new_health):
        ...

    @property
    @abstractmethod
    def max_health(self):
        ...
    
    @property
    @abstractmethod
    def nickname(self):
        ...
    
    @nickname.setter
    @abstractmethod
    def nickname(self, new_nickname):
        ...
    
    @property
    @abstractmethod
    def domestication(self) -> AnimalType:
        ...

    @abstractmethod
    def make_sound(self):
        ...