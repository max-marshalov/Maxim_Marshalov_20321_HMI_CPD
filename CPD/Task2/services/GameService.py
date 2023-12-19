##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-12-13 2:16:15 pm
 # @copyright SMTU
 #
from controllers.GamePole import GamePole
from controllers.Ship import Ship
from random import randint
class GameService:
    def __init__(self, size) -> None:
        self.player_pole = GamePole(size)
        self.bot_pole = GamePole(size)
    def attack(self, x, y):
        for ship in self.bot_pole.get_ships():
            if [x, y] in ship.get_self_zone(ship._x, ship._y, ship._tp, ship._length):
                if ship._tp == 1:
                    ship._cells[x - ship._x] = 2
                    print("Игрок: Есть пробитие")
                    break
                if ship._tp == 2:
                    ship._cells[y - ship._y] = 2
                    print("Игрок: Есть пробитие")
                    break
        else:
            print("Игрок: Не пробил")
    def bot_attack(self):
        print("Ход противника")
        x = randint(0, self.player_pole._size)
        y = randint(0, self.player_pole._size)
        for ship in self.player_pole.get_ships():
            if [x, y] in ship.get_self_zone(ship._x, ship._y, ship._tp, ship._length):
                if ship._tp == 1:
                    ship._cells[x - ship._x] = 2
                    print("Бот: Есть пробитие")
                    break
                if ship._tp == 2:
                    ship._cells[y - ship._y] = 2
                    print("Бот: Есть пробитие")
                    break
        else:
            print("Бот: Не пробил")
    def run(self):
        self.player_pole.init()
        self.bot_pole.init()
        while True:
            print("Поле игрока -----------------------------------------------------------------------------")
            self.player_pole.show()
            print("Поле бота--------------------------------------------------------------------------------")
            self.bot_pole.secret_show()
            x, y = input("Хотите выстрелить? Введите х и у ").split(' ')
            self.attack(int(x), int(y))
            self.bot_attack()
            self.player_pole.move_ships()
            self.bot_pole.move_ships()
           