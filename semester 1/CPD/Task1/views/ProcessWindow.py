##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-01 4:29:11 pm
 # @copyright SMTU
 #
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from controllers.ProcessWindowController import ProcessWindowController
from services.ValidationService import ValidationService
class ProccessWindow:
    def __init__(self, tab: ctk.CTkTabview) -> None:
        super().__init__()
        '''Класс для отображения списка процессов. \n
        В конструктор необходимо передать вкладку, к которой надо прикрепить view'''
        self.__tab = tab
        self.__tab.grid_columnconfigure(1, weight=1)
        self.__validation_service = ValidationService()
        self.process_controller = ProcessWindowController(self)

        #Инициализируем и размещаем фреймы
        self.__search_frame = ctk.CTkFrame(self.__tab, width=600, height=50)
        self.__table_frame = ctk.CTkFrame(self.__tab, width=600)

        self.__search_frame.grid(row=0, column=0, padx=5, pady=5)
        self.__table_frame.grid(row=1, column=0, padx=5, pady=5)
        self.__search_frame.grid_rowconfigure(0, weight=1)
        self.__table_frame.grid_rowconfigure(0, weight=1)

        #Инициализируем и размещаем поиск
        self.__search_entry = ctk.CTkEntry(self.__search_frame, placeholder_text="Поиск")
        self.__search_btn = ctk.CTkButton(self.__search_frame, text="Поиск", command=self.process_controller.search_process)

        self.__search_entry.grid(row=0, column=0, padx=5, pady=5)
        self.__search_btn.grid(row=0, column=1, padx=5, pady=5)

        #Инициализируем и размещаем scrollbar
        self.__scrollbar = ctk.CTkScrollbar(self.__table_frame, orientation="vertical")
        self.__scrollbar.grid(row=0, column=1, sticky="ns")

        #Инициализация  и размещение таблицы
        self.__table = ttk.Treeview(self.__table_frame, columns=("PID", "Name", "CPU", "Memory", "Network"), yscrollcommand=self.__scrollbar.set, show="headings") # yscrollcommand=self.scrollbar.set
        self.__table.heading("PID", text="PID", command=lambda:self.process_controller.os_processes_service.change_sort_flag('pid'))
        self.__table.heading("Name", text="Name", command=lambda:self.process_controller.os_processes_service.change_sort_flag('name'))
        self.__table.heading("CPU", text="CPU", command=lambda:self.process_controller.os_processes_service.change_sort_flag('cpu_percent'))
        self.__table.heading("Memory", text="Memory", command=lambda:self.process_controller.os_processes_service.change_sort_flag('memory_percent'))
        self.__table.heading("Network", text="Network", command=lambda:self.process_controller.os_processes_service.change_sort_flag('connections'))
        self.__table.column("PID", width=110)
        self.__table.column("Name", width=110)
        self.__table.column("CPU", width=110)
        self.__table.column("Memory", width=110)
        self.__table.column("Network", width=110)

        self.__table.grid(row=0, column=0, sticky="nsew")
        #Связка scrollbar и таблицы
        self.__scrollbar.configure(command=self.__table.yview)
        self.__tab.grid_columnconfigure(0, weight=1)

        #Инициализация и размещение кнопки удаления
        self.__remove_process_btn = ctk.CTkButton(self.__table_frame, text="Снять задачу", command=self.process_controller.kill_process)
        self.__remove_process_btn.grid(row=1, column=0, padx=5, pady=5)



        #Определяем property
    @property
    def table(self):
        '''Возвращает объект таблицы'''
        return self.__table
    
    @property
    def search_entry(self):
        '''Возвращает объект поля ввода'''
        return self.__search_entry
    
    @property
    def search_btn(self):
        '''Возвращает '''
        return self.__search_btn
    
    @property
    def remove_process_btn(self):
        return self.__remove_process_btn