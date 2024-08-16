from animal import Animal
from animal import AnimalType

class Tiger(Animal):
    def __init__(self, name, health,max_health, domestication: AnimalType):
        self._nickname = name
        self._current_health = health
        self._max_health = max_health
        self._domestication = domestication

    @property
    def current_health(self):
        return self._current_health

    @current_health.setter
    def current_health(self, new_health):
        self._health = new_health

    @current_health.setter
    def current_health(self, new_health):
        if(new_health > self.max_health):
            self._current_health = self._max_health
        else:
            self._current_health = new_health
    
    @property
    def max_health(self):
        return self._max_health

    @property
    def nickname(self):
        if(self._domestication == AnimalType.DOMESTICATED):
            return self._nickname
        else:
            # Only domesticated togers could have a name
            return None
    
    @nickname.setter
    def nickname(self, new_name):
        if(self._domestication == AnimalType.DOMESTICATED):
            self._nickname = new_name
        else:
            pass
    
    def make_sound(self):
        if(self._domestication == AnimalType.DOMESTICATED):
            print("Tiger, named {}, purrs at you".format(self.nickname))
        else:
            print("Tiger agressively roars at you!")

    @property
    def domestication(self) -> AnimalType:
        return self._domestication