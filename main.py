"""Create character."""
from random import randint


def attack(char_name: str, char_class: str) -> str:
    """Define attack for character."""
    warrior_attack = 5 + randint(3, 5)
    mage_attack = 5 + randint(5, 10)
    healer_attack = 5 + randint(-3, -1)
    if char_class == 'warrior':
        return f'{char_name} нанёс урон противнику равный {warrior_attack}'
    if char_class == 'mage':
        return f'{char_name} нанёс урон противнику равный {mage_attack}'
    if char_class == 'healer':
        return f'{char_name} нанёс урон противнику равный {healer_attack}'
    return ''


def defence(char_name: str, char_class: str) -> str:
    """Define defence for character."""
    warrior_defence = 5 + randint(3, 5)
    mage_defence = 5 + randint(5, 10)
    healer_defence = 5 + randint(-3, -1)
    if char_class == 'warrior':
        return f'{char_name} блокировал {warrior_defence} урона'
    if char_class == 'mage':
        return f'{char_name} блокировал {mage_defence} урона'
    if char_class == 'healer':
        return f'{char_name} блокировал {healer_defence} урона'
    return ''


def special(char_name: str, char_class: str) -> str:
    """Define special ability for character."""
    warrior_special = 80 + 25
    mage_special = 5 + 40
    healer_special = 10 + 30
    if char_class == 'warrior':
        return (f'{char_name} применил специальное умение '
                f'«Выносливость {warrior_special}»')
    if char_class == 'mage':
        return (f'{char_name} применил специальное умение '
                f'«Атака {mage_special}»')
    if char_class == 'healer':
        return (f'{char_name} применил специальное умение '
                f'«Защита {healer_special}»')
    return ''


def start_training(char_name: str, char_class: str) -> str:
    """Start training for a character."""
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или special — '
          'чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Choose your character."""
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        char_class = input('Введи название персонажа, '
                           'за которого хочешь играть: '
                           'Воитель — warrior, Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. '
                  'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. '
                  'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. '
                  'Черпает силы из природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


def main():
    """Start your game."""
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))


main()
