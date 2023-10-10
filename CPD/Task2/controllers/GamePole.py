##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-04 10:47:48 am
 # @copyright SMTU
 #
from controllers.Ship import Ship
from random import randint
class GamePole:
    def __init__(self, pole_size: int) -> None:
        self.__size = pole_size
        self.__ships = []
        self.__spaced_ships = []
        self.__pole = [[0 for i in range(self.__size)] for i in range(self.__size)]
    
    def init(self):
        self.__ships = [Ship(4, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)), 
                        Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)), 
                        Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2))]
        start_ship = self.__ships[0]
        while True:
            x = randint(0, self.__size -1)
            y = randint(0, self.__size - 1)
            start_ship.set_start_coord(x, y)
            if not start_ship.is_out_pole(self.__size):
                self.__spaced_ships.append(start_ship)
                break
        
        for i in range(1, len(self.__ships)):
            ship = self.__ships[i]
            while True:
                x = randint(0, self.__size -1)
                y = randint(0, self.__size - 1)
                ship.set_start_coord(x, y)
                count = 0
                for spaced_ship in self.__spaced_ships:
                    if not ship.is_collide(spaced_ship):
                        count += 1
                if (not ship.is_out_pole(self.__size)) and (count == len(self.__spaced_ships)):
                        self.__spaced_ships.append(ship)
                        break
        self.make_pole()
        

    def get_ships(self):
        return self.__ships
    
    def show(self):
        for row in self.__pole:
            print(" ".join([str (v) for v in row]))
        
    
    def get_pole(self):
        return self.__pole
    
    def make_pole(self):
        for ship in self.__ships:
            for index, data in ship.make_position().items():
                self.__pole[data[0]][data[1]] = data[2]

