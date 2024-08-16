from abc import ABC, abstractmethod
from animal import Animal


class Doctor(ABC):
    @property
    @abstractmethod
    def name(self):
        ...

    @name.setter
    @abstractmethod
    def name(self,new_name):
        ...
    
    @property
    @abstractmethod
    def healing_factor(self):
        ...

    @healing_factor.setter
    @abstractmethod
    def healing_factor(self, new_healing_factor):
        ...
    
    @abstractmethod
    def heal(self,animal: Animal):
        ...