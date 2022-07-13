from heroes import ChackNorris, SuperHeroInterface, Superman
from newssenders import NewsSender, PlanetSender
from places import Kostroma, Place, Tokyo


def save_the_place(hero: SuperHeroInterface, place: Place):
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    NewsSender.create_news(hero, place)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma())
    print('-' * 20)
    save_the_place(ChackNorris(), Tokyo())
    print('-' * 20)
    PlanetSender.send_message_to_planet('We need help!', [351.2, 258.15, 433.3])
