##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-01 7:01:05 pm
 # @copyright SMTU
 #
from views.PerformanceWindow import PerformanceWindow
class PerformanceWindowController:
    def __init__(self, window: PerformanceWindow) -> None:
        self.__window = window