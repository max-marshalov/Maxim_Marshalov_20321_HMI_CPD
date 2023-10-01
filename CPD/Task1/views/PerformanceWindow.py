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
import matplotlib.pyplot as plt
class PerformanceWindow:
    def __init__(self, tab : ctk.CTkTabview) -> None:
        '''Класс для отображения производительности процессов в графиках. \n
        В конструктор необходимо передать вкладку, к которой надо прикрепить view'''
        self._tab = tab
        self._tab.columnconfigure(0, weight=1)

        #Инициализируем и размещаем фреймы
        self._plot_frame = ctk.CTkFrame(self._tab, width=500)
        self._menu_frame = ctk.CTkFrame(self._tab, width=100)
        self._menu_frame.grid(row=0, column=0, padx=5, pady=5)
        self._plot_frame.grid(row=1, column=0, padx=5, pady=5)
        


        #Инициализируем combobox
        self._side_combo_box = ctk.CTkComboBox(self._menu_frame, values=["PID", "Name", "CPU", "Memory"])
        self._side_combo_box.grid(row=0, column=0, padx=5, pady=5)

        #Инициализируем canvas
        self._fig, self._ax = plt.subplots(figsize=(6,5))
        self._canvas = FigureCanvasTkAgg(self._fig, self._plot_frame)
        self._canvas.get_tk_widget().grid(row=0, column=0, padx=5, pady=5)