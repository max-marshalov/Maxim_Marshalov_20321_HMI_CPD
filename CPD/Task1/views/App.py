##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-01 4:01:02 pm
 # @copyright SMTU
 #

import customtkinter as ctk
from views.ProcessWindow import ProccessWindow
from views.PerformanceWindow import PerformanceWindow
from services.AsyncService import AsyncService
class App(ctk.CTk):
    '''Даннный класс реализует в себе механизм отображения различных окон приложения'''
    def __init__(self, loop):
        self.loop = loop
        super().__init__()
        self.title("Task manager")
        self.geometry("600x600")
        
        ctk.set_appearance_mode("dark")

        #Инициализируем и размещаем вкладки
        self.tab_view = ctk.CTkTabview(master=self, width=600, height=600)
        self.process_tab = self.tab_view.add("Процессы")
        self.performance_tab = self.tab_view.add("Производительность")
        self.tab_view.grid(row=0, column=0, padx=5, pady=5)

        #Инициализируем окна
        self.process_window = ProccessWindow(self.process_tab)
        self.performance_tab = PerformanceWindow(self.performance_tab)
        
        self.async_service = AsyncService(self)
        self.protocol("WM_DELETE_WINDOW", self.async_service.close)
