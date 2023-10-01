##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-01 3:26:47 pm
 # @copyright SMTU
 #
import customtkinter as ctk
from tkinter import ttk
import tkcalendar
from controllers.AppController import AppController
from services.ValidationService import ValidationService
class App(ctk.CTk):
    '''Данный класс инициализирует приложение и его основные views'''
    def __init__(self):
        super().__init__()
        self.title("Expense accounting")
        self.geometry("600x600")
        ctk.set_appearance_mode("dark")

        # Инициализация валидаций
        self.validation_service = ValidationService()
        self.category_validate = (self.register(self.validation_service.only_symbols_validation), '%P')
        self.price_validate = (self.register(self.validation_service.only_numbers_validation), '%P')

        # Инициализация фреймов
        self.input_frame = ctk.CTkFrame(self, width=600)
        self.table_frame = ctk.CTkFrame(self, width=600)
        self.crud_frame = ctk.CTkFrame(self, width=600)

        # Размещение фреймов
        self.input_frame.grid(row=0, column=0, padx=5, pady=5)
        self.table_frame.grid(row=1, column=0, padx=5, pady=5)
        self.crud_frame.grid(row=2, column=0, padx=5, pady=5)

        # Инициализация надписей во фрейме для ввода
        self.date_label = ctk.CTkLabel(self.input_frame, text="Дата")
        self.category_label = ctk.CTkLabel(self.input_frame, text="Категория")
        self.price_label = ctk.CTkLabel(self.input_frame, text="Сумма")

        #Инициализация полей для ввода
        self.calendar = tkcalendar.Calendar(self.input_frame, selectmode='day',showweeknumbers=False, cursor="hand2", date_pattern= 'y-mm-dd',borderwidth=0, bordercolor='white',)
        self.category_entry = ttk.Entry(self.input_frame, validate='key', validatecommand=self.category_validate)
        self.price_entry = ttk.Entry(self.input_frame, validate='key', validatecommand=self.price_validate)

        #Размещение внутри фрейма ввода
        self.date_label.grid(row=0, column=0, padx=5, pady=5)
        self.category_label.grid(row=1, column=0, padx=5, pady=5)
        self.price_label.grid(row=2, column=0, padx=5, pady=5)

        self.calendar.grid(row=0, column=1, padx=5, pady=5)
        self.category_entry.grid(row=1, column=1, padx=5, pady=5)
        self.price_entry.grid(row=2, column=1, padx=10, pady=5)
        
        #Добавление и размещение скролбара и таблицы для фрейма таблицы
        self.scrollbar = ctk.CTkScrollbar(self.table_frame, orientation="vertical")
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        
        self.table = ttk.Treeview(self.table_frame, columns=("Date", "Category", "Price"), yscrollcommand=self.scrollbar.set, show="headings")
        self.table.heading("Date", text="Дата")
        self.table.heading("Category", text="Категория")
        self.table.heading("Price", text="Сумма")

        self.table.column("Date", width=150)
        self.table.column("Category", width=150)
        self.table.column("Price", width=150)

        self.table.grid(row=0, column=0, sticky="nsew")
        

        self.app_controller = AppController(self.calendar, self.category_entry, self.price_entry, self.table)

        # Инициализация CRUD фрейма (Create, Read, Update, Delete), в нем располагаются кнопки для добавления данных, удаления, загрузки, сохранения
        # Также есть возможность просмотра общей суммы
        
        
        self.add_button = ctk.CTkButton(self.crud_frame, text="Добавить", command=self.app_controller.add_entry)
        self.remove_button = ctk.CTkButton(self.crud_frame, text="Удалить", command=self.app_controller.delete_entry)
        self.save_button = ctk.CTkButton(self.crud_frame, text="Сохранить таблицу",command=self.app_controller.save_table)
        self.load_button = ctk.CTkButton(self.crud_frame, text="Загрузить", command=self.app_controller.load_table)

        self.add_button.bind('<ButtonPress-1>', self.app_controller.calculate_total)
        self.remove_button.bind('<ButtonPress-1>', self.app_controller.calculate_total)
        self.load_button.bind('<ButtonPress-1>', self.app_controller.calculate_total)

        self.total_label = ctk.CTkLabel(self.crud_frame, text="Общая сумма")
        self.total_message = ctk.CTkLabel(self.crud_frame, textvariable=self.app_controller.total_message)

        self.add_button.grid(row=0, column=0, padx=5, pady=5)
        self.remove_button.grid(row=0, column=1, padx=5, pady=5)
        self.save_button.grid(row=0, column=2, padx=5, pady=5)
        self.load_button.grid(row=0, column=3, padx=5, pady=5)
        self.total_label.grid(row=2, column=0, padx=5, pady=5)
        self.total_message.grid(row=2, column=1, padx=5, pady=5)

