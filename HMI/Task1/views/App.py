import customtkinter as ctk
from tkinter import ttk
import tkcalendar
from services.TableService import TableService
class App(ctk.CTk):
    "Данный класс инициализирует приложение и его основные views"
    def __init__(self):
        super().__init__()
        self.title("Expense accounting")
        self.geometry("600x600")
        ctk.set_appearance_mode("dark")
        '''Инициализация фреймов'''
        self.input_frame = ctk.CTkFrame(self, width=600)
        self.table_frame = ctk.CTkFrame(self, width=600)
        self.crud_frame = ctk.CTkFrame(self, width=600)
        '''Размещение фреймов'''
        self.input_frame.grid(row=0, column=0, padx=5, pady=5)
        self.table_frame.grid(row=1, column=0, padx=5, pady=5)
        self.crud_frame.grid(row=2, column=0, padx=5, pady=5)
        '''Инициализация надписей во фрейме для ввода'''
        self.date_label = ctk.CTkLabel(self.input_frame, text="Дата")
        self.category_label = ctk.CTkLabel(self.input_frame, text="Категория")
        self.price_label = ctk.CTkLabel(self.input_frame, text="Сумма")
        '''Инициализация полей для ввода'''
        self.calendar = tkcalendar.Calendar(self.input_frame, selectmode='day',showweeknumbers=False, cursor="hand2", date_pattern= 'y-mm-dd',borderwidth=0, bordercolor='white',)
        self.category_entry = ctk.CTkEntry(self.input_frame)
        self.price_entry = ctk.CTkEntry(self.input_frame)
        '''Размещение внутри фрейма ввода'''
        self.date_label.grid(row=0, column=0, padx=5, pady=5)
        self.category_label.grid(row=1, column=0, padx=5, pady=5)
        self.price_label.grid(row=2, column=0, padx=5, pady=5)

        self.calendar.grid(row=0, column=1, padx=5, pady=5)
        self.category_entry.grid(row=1, column=1, padx=5, pady=5)
        self.price_entry.grid(row=2, column=1, padx=10, pady=5)
        '''Добавление и размещение скролбара и таблицы для фрейма таблицы'''
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

        '''Инициализация сервисов'''
        self.table_service = TableService(self.calendar, self.category_entry, self.price_entry, self.table)

        '''Инициализация CRUD фрейма (Create, Read, Update, Delete), в нем располагаются кнопки для добавления данных, удаления, загрузки, сохранения
        А также есть возможность просмотра Общей суммы'''

        self.add_button = ctk.CTkButton(self.crud_frame, text="Добавить", command=self.table_service.add_entry)
        self.remove_button = ctk.CTkButton(self.crud_frame, text="Удалить", command=self.table_service.delete_entry)
        self.save_button = ctk.CTkButton(self.crud_frame, text="Сохранить таблицу",command=self.table_service.save_table)
        self.load_button = ctk.CTkButton(self.crud_frame, text="Загрузить", command=self.table_service.load_table)

        self.add_button.grid(row=0, column=0, padx=5, pady=5)
        self.remove_button.grid(row=0, column=1, padx=5, pady=5)
        self.save_button.grid(row=0, column=2, padx=5, pady=5)
        self.load_button.grid(row=0, column=3, padx=5, pady=5)
        

