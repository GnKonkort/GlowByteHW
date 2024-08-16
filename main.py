from dog import Dog
from cat import Cat
from tiger import Tiger
from veterinary import Veterinary
from animal import Animal
from animal import AnimalType
from collections import deque

animals = []




if __name__ == "__main__":
    animals.append(Dog("Jack",10,15))
    animals.append(Cat("Marina",14,15))
    animals.append(Tiger("Alex",25,30,AnimalType.WILD))

    doctor = Veterinary("Dr.Krinkov",1.4)

    for animal_ in animals:
        doctor.heal(animal_)