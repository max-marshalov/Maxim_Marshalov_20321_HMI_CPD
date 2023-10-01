##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-01 7:31:58 pm
 # @copyright SMTU
 #
import psutil
class OsProcessesService:
    def __init__(self) -> None:
        '''Сервис для получения информации о процессах от OC'''
        self.__cpu_count = psutil.cpu_count()
        self.__virtual_memory = psutil.virtual_memory().total
        self.__sort_flag = 'pid'
        self.__old_flag = self.__sort_flag
        self.__procs = []

    def __get_processes(self):
        '''Возвращает информацию о процессах в виде словаря'''
        return psutil.process_iter(attrs=['pid', 'name', 'cpu_percent', 'memory_percent', "connections"])
    
    def get_sort_processes(self):
        try:
            return sorted(self.__get_processes(), key=lambda p : p.info[self.__sort_flag], reverse=True)
        except Exception as e:
            print(e)

    def change_old_flag(self):
        self.__old_flag = self.sort_flag
    
    def change_sort_flag(self, value:str):
        self.sort_flag = value
            
    
    @property
    def procs(self):
         return self.__procs
    @property
    def cpu_count(self):
        return self.__cpu_count
    
    @property
    def virtual_memory(self):
        return self.__virtual_memory
     
    
    @property
    def sort_flag(self):
        return self.__sort_flag
    
    @sort_flag.setter
    def sort_flag(self, value):
        self.__sort_flag = value
    
    @property
    def old_flag(self):
        return self.__old_flag
