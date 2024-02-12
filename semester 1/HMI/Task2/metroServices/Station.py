##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-02 10:05:52 am
 # @copyright SMTU
 #
from core.Vertex import Vertex
class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.__name = name

    def __str__(self):
        return f'{self.__name}'

    def __repr__(self):
        return f'{self.__name}'