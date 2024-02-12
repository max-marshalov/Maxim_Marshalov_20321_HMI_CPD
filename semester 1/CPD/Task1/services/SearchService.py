##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-11-29 5:28:57 pm
 # @copyright SMTU
 #
from re import search
class SearchService:
    def __init__(self) -> None:
        pass
    def search(self, word_list: list ,word : str):
        for name in word_list:
            if search(word, name.info['name']):
                return name