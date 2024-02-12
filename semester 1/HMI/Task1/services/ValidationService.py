##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-01 3:26:04 pm
 # @copyright SMTU
 #

class ValidationService:
    '''Сервис, который хранит в себе механизмы валидации'''
    def __init__(self):
        pass
    def only_numbers_validation(self, value):
       return str.isnumeric(value) or value == ""
       
    def only_symbols_validation(self,value):
        return str.isalpha(value) or value == ""