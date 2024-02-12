## Морской бой

## Листинги
### 1. GamePole.py ###

```Py
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

```
### 2. Ship.py ###
```python
##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-04 10:48:06 am
 # @copyright SMTU
 #
class Ship:
    def __init__(self, length: int, tp = 1, x = None, y = None) -> None:
        self._length = length
        self._tp = tp
        self._x = x
        self._y = y
        self._is_move = True
        self._cells = [1] * (self._length)

    def set_start_coords(self, x: int, y: int):
        self._x = x
        self._y = y
    
    def get_start_coords(self) -> tuple:
        return (self._x, self._y)
    
    def move(self, go: int):
        if self._is_move:
            if self._tp == 1:
                pass
            elif self._tp == 2:
                pass
    
    def is_collide(self, ship):
        x, y = ship.get_start_coords()
        ship_zone = self.get_zone(x, y, ship.tp, ship.length, 10)
        self_zone = self.get_self_zone(self._x, self._y, self._tp, self._length)
        for cords in self_zone:
            if cords in ship_zone:
                return True
        return False

    def is_out_pole(self, size: int):
        if self._tp == 1:
            return (self._x + self._length) > size
        elif self._tp == 2:
            return (self._y + self._length) > size
    def get_zone(self, x: int, y: int, tp: int, length: int, size: int) -> list:
        zone = []
        if tp == 1:
            zone = [[i, j] for i in range(x - 1, x + 1 + length) for j in range(y - 1, y + 2) if
                    0 <= i < size and 0 <= j < size]
        elif tp == 2:
            zone = [[i, j] for i in range(x - 1, x + 2) for j in range(y - 1, y + length + 1) if
                    0 <= i < size and 0 <= j < size]
        return zone

    def get_self_zone(self, x, y, tp=None, length=None):
        if tp == 1:
            return [[i, y] for i in range(x, x + length)]
        else:
            return [[x, i] for i in range(y, y + length)]
    
    def make_position(self):
        position = dict()
        if self._tp == 1:
            for i in range(self._length):
                position[i] = (self._x + i, self._y, self._cells[i])
        elif self._tp == 2:
            for i in range(self._length):
                position[i] = (self._x, self._y + i, self._cells[i])
        return position
    
            
    @property
    def tp(self):
        return self._tp
    @property
    def length(self):
        return self._length
    def __getitem__(self, item):
        return self._cells[item]
    def __setitem__(self, value, item):
        self._cells.insert(value, item)

```
### 3. main.py ###
```python
##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-04 10:42:00 am
 # @copyright SMTU
 #
from tests.TestRunner import TestRunner
from services.GameService import GameService
if __name__ == "__main__":
   testRunner = TestRunner()
   testRunner.run()
   game = GameService(10)
   game.run()

```
### 4. GameService.py ###
```python
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
```
## Результат работы
<image src="images/img1.png">