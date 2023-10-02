##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-02 10:05:31 am
 # @copyright SMTU
 #
class Link:
    def __init__(self , v1, v2):
        self.__v1 = v1
        self.__v2 = v2
        self.__dist = 1
    @property
    def v1(self):
        return self.__v1
    @property
    def v2(self):
        return self.__v2
    @property
    def dist(self):
        return self.__dist
    @dist.setter
    def dist(self, new_dist):
        self.__dist = new_dist
