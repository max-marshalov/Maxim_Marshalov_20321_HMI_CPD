##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-02 10:05:39 am
 # @copyright SMTU
 #
from core.Link import Link
class Vertex:
    def __init__(self) -> None:
        self.__links = []
    @property
    def links(self) -> list:
        return self.__links
    @links.setter
    def links(self, link: Link):
        self.__links.append(link)