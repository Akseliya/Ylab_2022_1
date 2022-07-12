from abc import ABC


class Gun(ABC):

    @staticmethod
    def fire_a_gun():
        print('PIU PIU')


class Laser(ABC):

    @staticmethod
    def incinerate_with_lasers():
        print('Wzzzuuuup!')


class HandToHandFight(ABC):

    @staticmethod
    def kick():
        print('Kick')

    @staticmethod
    def roundhouse_kick():
        print('Bump')
