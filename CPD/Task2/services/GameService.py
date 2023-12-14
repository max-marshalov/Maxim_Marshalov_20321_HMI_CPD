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
            if (x, y) in ship.get_self_zone(ship._x, ship._x, ship._tp, ship._length):
                if ship._tp == 1:
                    ship._cells[x - ship._x] = 2
                    print("Есть пробитие")
                if self._tp == 2:
                    ship._cells[y - ship._y] = 2
                    print("Есть пробитие")
        else:
            print("Не пробил")
    def bot_attack(self):
        print("Ход противника")
        x = randint(0, self.player_pole._size)
        y = randint(0, self.player_pole._size)
        for ship in self.player_pole.get_ships():
            if (x, y) in ship.get_self_zone(ship._x, ship._x, ship._tp, ship._length):
                if ship._tp == 1:
                    ship._cells[x - ship._x] = 2
                    print("Есть пробитие")
                if self._tp == 2:
                    ship._cells[y - ship._y] = 2
                    print("Есть пробитие")
        else:
            print("Не пробил")
    def run(self):
        self.player_pole.init()
        self.bot_pole.init()
        while True:
            x, y = input("Хотите выстрелить? Введите х и у ").split(' ')
            self.attack(x, y)
            self.bot_attack()
            print("Поле игрока -----------------------------------------------------------------------------")
            self.player_pole.show()
            print("Поле бота--------------------------------------------------------------------------------")
            self.bot_pole.show()