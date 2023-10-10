##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-04 10:48:06 am
 # @copyright SMTU
 #
class Ship:
    def __init__(self, length: int, tp = 1, x = None, y = None) -> None:
        self.__length = length
        self.__tp = tp
        self.__x = x
        self.__y = y
        self.__is_move = True
        self.__cells = [1] * (self.__length + 1)

    def set_start_coord(self, x: int, y: int):
        self.__x = x
        self.__y = y
    
    def get_start_coord(self) -> tuple:
        return (self.__x, self.__y)
    
    def move(self, go: int):
        if self.__is_move:
            if self.__tp == 1:
                pass
            elif self.__tp == 2:
                pass
    
    def is_collide(self, ship):
       ship_zone = ship.calculate_zone()
       my_zone = self.calculate_zone()
       for i in ship_zone:
           for j in my_zone:
               if all(map(lambda x, y: x == y, i, j)):
                   return True
        
       return False

    def is_out_pole(self, size: int):
        if self.__tp == 1:
            return (self.__x + self.__length) > size
        elif self.__tp == 2:
            return (self.__y + self.__length) > size
    
    def calculate_zone(self):
        zone = []
        if self.__tp == 1:
            for i in range(self.__length):
                zone.append((self.__x + i, self.__y))
                zone.append((self.__x + i, self.__y + 1))
                zone.append((self.__x + i, self.__y - 1))
            zone.append((self.__x - 1, self.__y))
            zone.append((self.__x - 1, self.__y + 1))
            zone.append((self.__x - 1, self.__y - 1))
        elif self.__tp == 2:
            for i in range(self.__length):
                zone.append((self.__x, self.__y + i))
                zone.append((self.__x + 1, self.__y + i))
                zone.append((self.__x - 1, self.__y + i))
            zone.append((self.__x, self.__y - 1))
            zone.append((self.__x + 1, self.__y - 1))
            zone.append((self.__x - 1, self.__y - 1))
        return zone
    
    def make_position(self):
        position = dict()
        if self.__tp == 1:
            for i in range(self.__length):
                position[i] = (self.__x + i, self.__y, self.__cells[i])
        elif self.__tp == 2:
            for i in range(self.__length):
                position[i] = (self.__x, self.__y + i, self.__cells[i])
        return position
            


