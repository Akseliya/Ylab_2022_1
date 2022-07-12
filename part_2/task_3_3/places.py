from abc import ABC, abstractmethod


class Place(ABC):

    @property
    @abstractmethod
    def name(self):
        ...

    @abstractmethod
    def get_villain(self):
        ...


class Kostroma(Place):
    name = 'Kostroma'

    def get_villain(self):
        print('Orcs hid in the forest')


class Tokyo(Place):
    name = 'Tokyo'

    def get_villain(self):
        print('Godzilla stands near a skyscraper')
