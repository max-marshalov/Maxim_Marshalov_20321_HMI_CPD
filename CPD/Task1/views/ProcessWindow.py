##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-01 4:29:11 pm
 # @copyright SMTU
 #
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
class ProccessWindow:
    def __init__(self, tab: ctk.CTkTabview) -> None:
        super().__init__()
        '''Класс для отображения списка процессов. \n
        В конструктор необходимо передать вкладку, к которой надо прикрепить view'''
        self._tab = tab
        self._tab.grid_columnconfigure(1, weight=1)

        #Инициализируем и размещаем фреймы
        self._search_frame = ctk.CTkFrame(self._tab, width=600, height=50)
        self._table_frame = ctk.CTkFrame(self._tab, width=600)

        self._search_frame.grid(row=0, column=0, padx=5, pady=5)
        self._table_frame.grid(row=1, column=0, padx=5, pady=5)
        self._search_frame.grid_rowconfigure(0, weight=1)
        self._table_frame.grid_rowconfigure(0, weight=1)

        #Инициализируем и размещаем поиск
        self._search_entry = ctk.CTkEntry(self._search_frame, placeholder_text="Search")
        self._search_btn = ctk.CTkButton(self._search_frame, text="Поиск")

        self._search_entry.grid(row=0, column=0, padx=5, pady=5)
        self._search_btn.grid(row=0, column=1, padx=5, pady=5)

        #Инициализируем и размещаем scrollbar
        self._scrollbar = ctk.CTkScrollbar(self._table_frame, orientation="vertical")
        self._scrollbar.grid(row=0, column=1, sticky="ns")

        #Инициализация  и размещение таблицы
        self._table = ttk.Treeview(self._table_frame, columns=("PID", "Name", "CPU", "Memory"), yscrollcommand=self._scrollbar.set, show="headings") # yscrollcommand=self.scrollbar.set
        self._table.heading("PID", text="PID")
        self._table.heading("Name", text="Name")
        self._table.heading("CPU", text="CPU")
        self._table.heading("Memory", text="Memory")
        self._table.column("PID", width=130)
        self._table.column("Name", width=130)
        self._table.column("CPU", width=130)
        self._table.column("Memory", width=130)
        self._table.grid(row=0, column=0, sticky="nsew")

        #Связка scrollbar и таблицы
        self._scrollbar.configure(command=self._table.yview)
        self._tab.grid_columnconfigure(0, weight=1)

        #Инициализация и размещение кнопки удаления
        self._remove_process_btn = ctk.CTkButton(self._table_frame, text="Снять задачу")
        self._remove_process_btn.grid(row=1, column=0, padx=5, pady=5)