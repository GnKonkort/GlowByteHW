from doctor import Doctor
from animal import Animal

class Veterinary(Doctor):
    def __init__(self, name, healing_factor):
        self._name = name
        self._healing_factor = healing_factor

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,new_name):
        self._name = new_name

    @property
    def healing_factor(self):
        return self._healing_factor

    @healing_factor.setter
    def healing_factor(self, new_healing_factor):
        self._healing_factor = new_healing_factor

    def heal(self,animal: Animal):
        if(animal.nickname == None):
            print("Got new patient: Unnamed animal with {}/{} HP".format(animal.current_health,animal.max_health))
            print("Healing unnamed animal...")
        else:
            print("Got new patient: {} with {}/{} HP".format(animal.nickname,animal.current_health,animal.max_health))
            print("Healing {}...".format(animal.nickname))
        #print("{} -> {}".format(animal.current_health, animal.current_health * self.healing_factor))
        animal.current_health = animal.current_health * self.healing_factor
        animal.make_sound()
        print("Finished healing!")
        print("Patient current status: {}/{}\n".format(animal.current_health,animal.max_health))
