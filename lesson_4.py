'''# Примеры https://github.com/pygamelib/pygamelib/blob/master/examples/tutorials/01-game-basics.py

from pygamelib import engine, board_items, constants
from pygamelib.gfx import core
from pygamelib.assets import graphics

def update_game(game: engine.Game, key, elapsed_time):
    game.tutorial_01_timer += elapsed_time

    if game.tutorial_01_timer > 2:
        game.tutorial_01_timer = 0
        game.tutorial_01_counter += 1

        if game.current_level == 1:
            game.change_level(2)
        else:
            game.change_level(1)

        game.screen.place(mygame.current_board().name, 0, 0)
        game.screen.place(mygame.current_board(), 1, 0)

        if game.tutorial_01_counter == 10:
            game.stop()
        game.screen.update()

if __name__ == "__main__":
    mygame = engine.Game(
        name="Demo game", user_update=update_game, mode=constants.MODE_RT
    )
    board1 = engine.Board(
        name="Level 1",
        ui_board_void_cell=graphics.GREEN_SQUARE,
        player_starting_position=[0, 0],
    )
    board2 = engine.Board(
        name="Level 2",
        ui_board_void_cell=graphics.MAGENTA_SQUARE,
        player_starting_position=[4, 4],
    )

    mygame.player = board_items.Player(
        name="DaPlay3r",
        sprixel=core.Sprixel(graphics.Models.UNICORN, is_bg_transparent=True),
    )

    mygame.add_board(1, board1)
    mygame.add_board(2, board2)
    mygame.change_level(1)
    mygame.screen.place(mygame.current_board().name, 0, 0)
    mygame.screen.place(mygame.current_board(), 1, 0)

    mygame.tutorial_01_counter = 0
    mygame.tutorial_01_timer = 0

    mygame.run()

'''

# Знакомство с классами
'''a = input('Введитете данные: ')
print(a)'''

def get_test_data():
    a = input('Введитете данные: ')
    print(a)


class Bicycle:
    def __init__(self):
        # Атрибуты класса (любое кол-во)
        self.color = 'red'
        self.type = 'горный'
        self.speed = '20'

    # Методы класса
    def ride(self):
        print('я еду')

    def stop(self):
        print('я стою')


b = Bicycle # создали экземпляр класса
print(b) # <class '__main__.Bicycle'>
b.ride(1) # я еду
b.stop(1) # я стою


class Cat:
    def __init__(self, color, breed, age):
        self.color = 'white'
        self.breed = None
        self.age = 5
        self.is_kind = True

    def sleep(self):
        return 'Z-Z-Z'

    def eat(self):
        return 'amamam'

    def say_meu(self):
        return 'meu'

    def get_info(self):
        print('Кошка:','\nЦвет: ', self.color,
              '\nПорода: ', self.breed,
              '\nВозраст: ', self.age,
              '\nДобрая?: ', self.is_kind)

cat1 = Cat(color='black', breed='породистая', age=3)
cat2 = Cat(color='green', breed='-', age=12)
print(cat1)
print(cat1.sleep())
print(cat1.sleep())
print(cat1.sleep())
print(cat1.eat())
print(cat1.say_meu())
cat1.get_info()
