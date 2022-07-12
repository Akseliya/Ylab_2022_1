from abc import ABC, abstractmethod
from typing import List

from heroes import SuperHero
from places import Place


class NewsSender(ABC):

    @staticmethod
    def create_news(hero: SuperHero, place: Place):
        print(f'{hero.name} saved the {place.name}!')

    @staticmethod
    def create_newspaper_article(hero: SuperHero, place: Place):
        print(f'{hero.name} victory!\n{hero.name} has defeated all the villains in the {place.name}!')

    @staticmethod
    def send_message_to_planet(message: str, coordinates: List[float]):
        print(f'The message "{message}" was successfully sent to the planet with coordinates', *coordinates)
