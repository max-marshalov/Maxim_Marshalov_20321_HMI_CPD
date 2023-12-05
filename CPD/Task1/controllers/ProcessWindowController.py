##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-01 7:01:02 pm
 # @copyright SMTU
 #
import tkinter as tk
from services.OsProcessesService import OsProcessesService
from services.SearchService import SearchService
class ProcessWindowController:
    def __init__(self, window) -> None:
        self.__window = window
        self.__os_processes_service = OsProcessesService()
        self.__search_service = SearchService()
    
    def add_processes(self):
        sorted_processes = self.__os_processes_service.get_sort_processes()
        for i in range(len(sorted_processes)):
            self.__window.table.insert("", tk.END, values = (f"{sorted_processes[i].info['pid']}", f"{sorted_processes[i].info['name']}", f"{sorted_processes[i].info['cpu_percent']}", f"{float(sorted_processes[i].info['memory_percent']) / 100 * float(self.os_processes_service.virtual_memory)}", f"{len(sorted_processes[i].info['connections'])}"))
            self.__os_processes_service.procs.append(sorted_processes[i].info['pid'])
    
    def update_processes(self):
        try:
            sorted_processes = self.__os_processes_service.get_sort_processes()
            for i in range(len(sorted_processes)):
                item = self.__window.table.get_children()[i]
                if(self.__window.table.item(item)['values'][0] == sorted_processes[i].info['pid']):
                        self.__window.table.item(item, values = (f"{sorted_processes[i].info['pid']}", f"{sorted_processes[i].info['name']}", f"{sorted_processes[i].info['cpu_percent']}", f"{float(sorted_processes[i].info['memory_percent']) / 100 * float(self.os_processes_service.virtual_memory)}", f"{len(sorted_processes[i].info['connections'])}"))
                elif sorted_processes[i].info['pid'] not in self.__os_processes_service.procs:
                        self.table.insert("", tk.END, values = (f"{sorted_processes[i].info['pid']}", f"{sorted_processes[i].info['name']}", f"{sorted_processes[i].info['cpu_percent']}", f"{float(sorted_processes[i].info['memory_percent']) / 100 * float(self.os_processes_service.virtual_memory)}", f"{len(sorted_processes[i].info['connections'])}"))
                        self.__os_processes_service.procs.append(sorted_processes[i].info['pid'])
        except Exception as e:
             print(e)
    def search_process(self):
         word = self.__window.search_entry.get()
         procs = self.__os_processes_service.get_sort_processes()
         answer = self.__search_service.search(procs, word)
         for i in range(len(procs)):
              item = self.__window.table.get_children()[i]
              if(self.__window.table.item(item)['values'][0] == answer.info['pid']):
                   #self.__window.table.move("", item, 0)
                   self.__window.table.focus(item)
    def kill_process(self):
        try:
            items = self.__window.table.selection()
            for item in items:
                 proc_pid = self.__window.table.item(item)['values'][0]
                 self.os_processes_service.kill(proc_pid)
                 self.__window.table.delete(item)
        except Exception as e:
             pass
    
    @property
    def os_processes_service(self):
         return self.__os_processes_service
    
        
