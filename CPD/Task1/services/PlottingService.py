##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-04 10:29:22 am
 # @copyright SMTU
 #
import matplotlib.pyplot as plt
class PlottingService:
    def __init__(self, fig: plt.figure, ax: plt.Axes) -> None:
        '''Сервис для построения графиков\n
        В конструктор необходимо передать объект фигуры и объект оси'''
        self.__ax = ax
        self.__fig = fig