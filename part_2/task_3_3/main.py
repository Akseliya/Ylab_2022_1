from heroes import ChackNorris, SuperHero, Superman
from newssender import NewsSender
from places import Kostroma, Place, Tokyo


def save_the_place(hero: SuperHero, place: Place):
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
    NewsSender.send_message_to_planet('We need help!', [351.2, 258.15, 433.3])
