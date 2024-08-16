from animal import Animal
from animal import AnimalType

class Dog(Animal):
    def __init__(self, name, health, max_health):
        self._nickname = name
        self._current_health = health
        self._max_health = max_health
        self._domestication = AnimalType.DOMESTICATED

    @property
    def current_health(self):
        return self._current_health

    @property
    def max_health(self):
        return self._max_health

    @current_health.setter
    def current_health(self, new_health):
        if(new_health > self.max_health):
            self._current_health = self._max_health
        else:
            self._current_health = new_health

    @property
    def nickname(self):
        return self._nickname
    
    @nickname.setter
    def nickname(self, new_name):
        self._nickname = new_name
    
    def make_sound(self):
        print("Dog, named {}, says 'Woof!'".format(self.nickname))

    @property
    def domestication(self) -> AnimalType:
        return self._domestication