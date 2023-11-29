##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-02 10:05:46 am
 # @copyright SMTU
 #
from core.Link import Link
class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2, dist)

    def __str__(self):
        return f'{self.v1}, {self.v2}'