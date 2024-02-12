##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-04 10:47:48 am
 # @copyright SMTU
 #
from turtle import update
from controllers.Ship import Ship
from random import randint, choice
class GamePole:
    def __init__(self, pole_size: int) -> None:
        self._size = pole_size
        self._ships = []
        self._spaced_ships = []
        self._pole = [[0 for i in range(self._size)] for i in range(self._size)]
    
    def init(self):
        self._ships = [Ship(4, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)), 
                        Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)), 
                        Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2))]
        start_ship = self._ships[0]
        while True:
            x = randint(0, self._size -1)
            y = randint(0, self._size - 1)
            start_ship.set_start_coords(x, y)
            if not start_ship.is_out_pole(self._size):
                self._spaced_ships.append(start_ship)
                break
        
        for i in range(1, len(self._ships)):
            ship = self._ships[i]
            while True:
                x = randint(0, self._size -1)
                y = randint(0, self._size - 1)
                ship.set_start_coords(x, y)
                count = 0
                for spaced_ship in self._spaced_ships:
                    if not ship.is_collide(spaced_ship):
                        count += 1
                if (not ship.is_out_pole(self._size)) and (count == len(self._spaced_ships)):
                        self._spaced_ships.append(ship)
                        break
        self.make_pole()
        

    def get_ships(self):
        return self._ships
    
    def update_pole(self):
        self._pole = [[0 for _ in range(self._size)] for _ in range(self._size)]
        for ship in self._ships:
            x, y = self.get_random_cords(ship) if ship._x == ship._y is None else ship.get_start_coords()
            if ship.tp == 1:
                for index, i in enumerate(range(x, x + ship.length)):
                    self._pole[y][i] = ship._cells[index]
            elif ship.tp == 2:
                for index, i in enumerate(range(y, y + ship.length)):
                    self._pole[i][x] = ship._cells[index]
            ship.set_start_coords(x, y)
    def show(self):
        self.update_pole()
        for row in self._pole:
            print(" ".join([str (v) for v in row]))
    
    def secret_show(self):
        self.update_pole()
        for row in self._pole:
            for v in row :
                if v != 2:
                    print("#", end=" ")
                else:
                    print(str(v), end=" ")
            print("\n", end="")
    
    def get_pole(self):
        return tuple(tuple(i) for i in self._pole)
    
    def make_pole(self):
        for ship in self._ships:
            for index, data in ship.make_position().items():
                self._pole[data[0]][data[1]] = data[2]

    def move_check(self, ship, go):
        x, y = ship.get_start_coords()
        if ship.tp == 1:
            # Провека на столкновение
            zone = ship.get_zone(x + go, y, ship.tp, ship.length, self._size)
            if go == 1:
                check_length = x + go + ship.length
            else:
                check_length = x + go - 1
            for x_z, y_z in zone:
                if self._pole[y_z][x_z] != 0 and x_z == check_length:
                    return False

            # Проверка на выход из поля
            if x + go < 0 or x + go + ship.length > self._size:
                return False

        elif ship.tp == 2:
            # Проверка на столкновение
            zone = ship.get_zone(x, y + go, ship.tp, ship.length, self._size)
            if go == 1:
                check_lenght = y + go + ship.length
            else:
                check_lenght = y + go - 1
            for x_z, y_z in zone:
                if self._pole[y_z][x_z] != 0 and y_z == check_lenght:
                    return False

            
            if y + go < 0 or y + go + ship.length > self._size:
                return False
        return True

    def move_ships(self) -> None:
        for ship in self._ships:
            go = choice([-1, 1])
            flag = self.move_check(ship, go)
            if flag:
                ship.move(go)
                self.update_pole()
            else:
                flag = self.move_check(ship, -go)
                if flag:
                    ship.move(-go)
                    self.update_pole()
        self._attacked = []
