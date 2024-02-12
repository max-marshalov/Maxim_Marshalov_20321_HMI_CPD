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
