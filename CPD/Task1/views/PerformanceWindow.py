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
        self.__tab = tab
        self.__tab.columnconfigure(0, weight=1)

        #Инициализируем и размещаем фреймы
        self.__plot_frame = ctk.CTkFrame(self.__tab, width=500)
        self.__menu_frame = ctk.CTkFrame(self.__tab, width=100)
        self.__menu_frame.grid(row=0, column=0, padx=5, pady=5)
        self.__plot_frame.grid(row=1, column=0, padx=5, pady=5)

        #Инициализируем combobox
        self.__side_combo_box = ctk.CTkComboBox(self.__menu_frame, values=["CPU", "Memory", "Network Dowload", "Network Upload"])
        self.__side_combo_box.grid(row=0, column=0, padx=5, pady=5)

        #Инициализируем canvas
        self.__fig, self.__ax = plt.subplots(figsize=(6,5))
        self.__ax.set_ylim(1, 100)
        self.__ax.set_xlim(1, 100)
        self.__canvas = FigureCanvasTkAgg(self.__fig, self.__plot_frame)
        self.__canvas.get_tk_widget().grid(row=0, column=0, padx=5, pady=5)