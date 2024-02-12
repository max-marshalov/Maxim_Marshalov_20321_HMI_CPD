# Задание
### 1. Графический интерфейс ###
   - Основное окно со списком активных процессов.
   - Возможность обновления списка процессов.
   - Информационная панель, отображающая общие ресурсы системы (использование ЦП, памяти и т. д.).

### 2. Список процессов ###
   - Отображение PID (идентификатор процесса).
   - Отображение имени процесса.
   - Отображение использования ЦП и памяти конкретным процессом.
   - Возможность завершения выбранного процесса.
   - Возможность отсортировать список процессов по различным параметрам (например, использование ЦП, памяти).

### 3. Информационная панель ###
Обновление в реальном времени (matplotlib. FigureCanvasTkAgg):
   - Графическое представление загрузки ЦП.
   - Графическое представление использования оперативной памяти.
   - Графическое представление использования дискового пространства.
   - Отображение загруженности сети (загрузка/выгрузка).

### 4.Поиск ###
   - Поиск процессов по имени.
   - Возможность просмотра дополнительной информации о процессе (например, путь к исполняемому файлу, время запуска).
   - Возможность изменения приоритета процесса.

### 5. Настройки и предпочтения ###
   - Возможность выбора интервала обновления информации (например, каждые 2 секунды, 5 секунд и т. д.).

### 6. Безопасность и стабильность ###
   - Информирование пользователя о потенциально опасных действиях (например, предупреждение при попытке завершить какой-либо процесс (напр. важный системный процесс)).
# Результат работы
<image src="images/first.png" alt="Первое окно">
<image src="images/second.png" alt="Второе окно">

# Пример кода
1. ### PerformanceWindow.py ###
```python
##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-01 4:29:14 pm
 # @copyright SMTU
 #
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from controllers.PerformanceWindowController import PerformanceWindowController
import matplotlib.pyplot as plt
class PerformanceWindow:
    def __init__(self, tab : ctk.CTkTabview) -> None:
        '''Класс для отображения производительности процессов в графиках. \n
        В конструктор необходимо передать вкладку, к которой надо прикрепить view'''
        self.__tab = tab
        self.__tab.columnconfigure(0, weight=1)

        
        #Инициализируем и размещаем фреймы
        self.__plot_frame = ctk.CTkFrame(self.__tab, width=500)
        self.__menu_frame = ctk.CTkFrame(self.__tab, width=100)
        self.__menu_frame.grid(row=0, column=0, padx=5, pady=5)
        self.__plot_frame.grid(row=1, column=0, padx=5, pady=5)


        #Инициализируем canvas
        self.__fig, self.__ax = plt.subplots(figsize=(6,5))
        self.__ax.set_ylim(1, 100)
        self.__ax.set_xlim(1, 100)
        self.__canvas = FigureCanvasTkAgg(self.__fig, self.__plot_frame)
        self.__canvas.get_tk_widget().grid(row=0, column=0, padx=5, pady=5)

        self.performance_controller = PerformanceWindowController(self)

        #Инициализируем combobox
        self.__side_combo_box = ctk.CTkComboBox(self.__menu_frame, values=["CPU", "Memory", "Disk usage", "Network Dowload", "Network Upload"], command=self.performance_controller.combo_box_request)
        self.__side_combo_box.grid(row=0, column=0, padx=5, pady=5)


    @property
    def axes(self):
        return self.__ax
    
    @property
    def figure(self):
        return self.__fig
    @property
    def canvas(self):
        return self.__canvas
    @property
    def side_combo_box(self):
        return self.__side_combo_box
```
2. ### PerformanceWindowController.py ###
```python
##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-01 7:01:02 pm
 # @copyright SMTU
 #
import re
import tkinter as tk
from types import NoneType
from typing import Any

from services.OsProcessesService import OsProcessesService
from services.SearchService import SearchService



class ProcessWindowController:
    def __init__(self, window) -> None:
        self.__window = window
        self.__os_processes_service = OsProcessesService()
        self.__search_service = SearchService()
        self.__search_proc = Any
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
                        self.__window.table.insert("", tk.END, values = (f"{sorted_processes[i].info['pid']}", f"{sorted_processes[i].info['name']}", f"{sorted_processes[i].info['cpu_percent']}", f"{float(sorted_processes[i].info['memory_percent']) / 100 * float(self.os_processes_service.virtual_memory)}", f"{len(sorted_processes[i].info['connections'])}"))
                        self.__os_processes_service.procs.append(sorted_processes[i].info['pid'])
            
                 
        except Exception as e:
             print(e)
    def search_process(self):
         word = self.__window.search_entry.get()
         procs = self.__os_processes_service.get_sort_processes()
         self.__search_proc = self.__search_service.search(procs, word)
         self.__window.table.insert("", 0, values = (f"{self.__search_proc.info['pid']}", f"{self.__search_proc.info['name']}", f"{self.__search_proc.info['cpu_percent']}", f"{float(self.__search_proc.info['memory_percent']) / 100 * float(self.os_processes_service.virtual_memory)}", f"{len(self.__search_proc.info['connections'])}"))
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
    
```
3. ### AsyncService.py ###
```python 
##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-01 7:53:36 pm
 # @copyright SMTU
 #
import asyncio

class AsyncService:
    def __init__(self,app, interval=1/20) -> None:
        '''В этом классе выполняются все асинхронные процессы'''
        self.__interval = interval
        self.__tasks = []
        self.__app = app
        self.__loop = self.__app.loop
        self.__app.protocol("WM_DELETE_WINDOW", self.close)
        self.__process_window_controller = self.__app.process_window.process_controller
        self.__os_service = self.__process_window_controller.os_processes_service
        self.__performance_window_controller = self.__app.performance_window.performance_controller

        self.__tasks.append(self.__loop.create_task(self.processes_updater()))
        #self.__tasks.append(self.__loop.create_task(self.graphics_updater()))
        self.semaphore = asyncio.Semaphore(5)

    async def processes_updater(self):
         '''Функция асинхронного обновления'''
         async with self.semaphore:
            await self.semaphore.acquire()
            try:
                 self.__app.update()
                 self.__process_window_controller.add_processes()
            finally:
                self.semaphore.release()
         while True:
            try:
                if self.__os_service.sort_flag != self.__os_service.old_flag:
                    self.semaphore = asyncio.Semaphore(5)
                    async with self.semaphore:
                        await self.semaphore.acquire()
                        try:
                            self.processes_sorter()
                        finally:
                            self.semaphore.release()
                self.__process_window_controller.update_processes()
                self.__app.update()
                self.graphics_updater()
                await asyncio.sleep(self.__interval)
            except Exception as _:
                pass
    def graphics_updater(self):
        '''Функция  отрисовки графиков'''
        try:
            self.__performance_window_controller.plotting_service.plot_charts()

        except Exception as e:
                print(e)
    
    def processes_sorter(self):
            '''Функция  сортировки процессов'''
            try:
                    self.__app.process_window.table.delete(*self.__app.process_window.table.get_children())
                    self.__os_service.procs.clear()
                    self.__process_window_controller.add_processes()
                    self.__os_service.change_old_flag()
            except Exception as _:
                pass

    def close(self):
        for task in self.__tasks:
            task.cancel()
        self.__loop.stop()
        self.__app.destroy()
        exit()
```
