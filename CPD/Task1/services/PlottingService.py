##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-04 10:29:22 am
 # @copyright SMTU
 #
import matplotlib.pyplot as plt
from services.OsProcessesService import OsProcessesService
class PlottingService:
    def __init__(self,canvas, ax:plt.Axes, ax_type:str=None) -> None:
        '''Сервис для построения графиков\n
        В конструктор необходимо передать объект фигуры, объект оси и тип отрисовываемого процесса'''
        self.__ax = ax
        self.__ax_type = ax_type
        self.__canvas = canvas
        self.__os_service = OsProcessesService()
    
    @property
    def ax_type(self):
        return self.__ax_type
    
    @ax_type.setter
    def ax_type(self, v:str):
        self.__ax_type = v

    def plot_charts(self):
        for i in range(1000):
            value = self.__os_service.values_as_dict()[self.__ax_type]
            self.__ax.scatter(i, value, marker='_', color='red')
            plt.pause(0.05)
        self.__canvas.draw()
        