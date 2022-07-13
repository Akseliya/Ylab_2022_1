from abc import ABC, abstractmethod

from places import Place
from weapons import Gun, HandToHandFight, Laser


class SuperHeroInterface(ABC):

    @property
    @abstractmethod
    def name(self):
        ...

    @property
    @abstractmethod
    def can_use_ultimate_attack(self):
        ...

    @abstractmethod
    def find(self, place: Place):
        ...

    @abstractmethod
    def attack(self):
        ...


class SuperHeroBase():
    can_use_ultimate_attack = False

    def find(self, place: Place):
        place.get_villain()


class Superman(SuperHeroBase, SuperHeroInterface):
    name = 'Clark Kent'
    can_use_ultimate_attack = True

    def attack(self):
        HandToHandFight.kick()

    def ultimate(self):
        Laser.incinerate_with_lasers()


class ChackNorris(SuperHeroBase, SuperHeroInterface):
    name = 'Chack Norris'

    def attack(self):
        Gun.fire_a_gun()
