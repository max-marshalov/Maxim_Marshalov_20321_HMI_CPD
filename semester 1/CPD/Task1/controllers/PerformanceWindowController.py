##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-01 7:01:05 pm
 # @copyright SMTU
 #
# from views.PerformanceWindow import PerformanceWindow
from services.PlottingService import PlottingService


class PerformanceWindowController:
    def __init__(self, window) -> None:
        self.__window = window
        self.plotting_service = PlottingService(self.__window.canvas, self.__window.axes, "CPU")
    
    def combo_box_request(self, text):
        self.plotting_service.ax_type =  text