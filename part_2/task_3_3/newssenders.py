from typing import List

from heroes import SuperHeroInterface
from places import Place


class NewsSender():

    @staticmethod
    def create_news(hero: SuperHeroInterface, place: Place):
        print(f'{hero.name} saved the {place.name}!')


class NewspaperSender(NewsSender):

    @staticmethod
    def create_newspaper_article(hero: SuperHeroInterface, place: Place):
        print(f'{hero.name} victory!\n{hero.name} has defeated all the villains in the {place.name}!')


class PlanetSender(NewsSender):

    @staticmethod
    def create_news(hero: SuperHeroInterface, coordinates: List[float]):
        print(f'{hero.name} saved the planet', *coordinates)

    @staticmethod
    def send_message_to_planet(message: str, coordinates: List[float]):
        print(f'The message "{message}" was successfully sent to the planet with coordinates', *coordinates)
