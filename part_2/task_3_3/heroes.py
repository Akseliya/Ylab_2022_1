from places import Place
from weapons import Gun, HandToHandFight, Laser


class SuperHero:

    def __init__(self, name: str, can_use_ultimate_attack: bool = True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack

    def find(self, place: Place):
        place.get_villain()

    def attack(self):
        HandToHandFight.kick()


class Superman(SuperHero):

    def __init__(self):
        super().__init__('Clark Kent')

    def attack(self):
        HandToHandFight.kick()

    def ultimate(self):
        Laser.incinerate_with_lasers()


class ChackNorris(SuperHero):

    def __init__(self):
        super().__init__('Chack Norris', False)

    def attack(self):
        Gun.fire_a_gun()
