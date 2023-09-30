import tkinter as tk
from tkinter import filedialog
from services.CsvService import CsvService
class TableService:
    def __init__(self, date_field, category_field, price_field, table) -> None:
        '''В конструктор необходимо передать ссылку на объект календаря, поля категории, поля стоимости 
        и ссылку на таблицу, для отобраэения'''
        self._table = table
        self._date_field = date_field
        self._categroy_field= category_field 
        self._price_filed = price_field
        self.csv_service = CsvService(self._table)
        
        

    def add_entry(self):
        '''Добавляет в таблицу новую запись'''
        self._table.insert("", tk.END, values=(f"{self._date_field.get_date()}", f"{self._categroy_field.get()}", f"{self._price_filed.get()}"))

    def delete_entry(self):
        '''Удаляет выбранную запись'''
        selected_item = self._table.selection()[0]
        self._table.delete(selected_item)
    
    def save_table(self):
        '''Сохраняет расходы в формат csv'''
        self.csv_service.write_csv("Expense accounting.csv")
    
    def load_table(self):
        '''Подгружает старые csv-файлы'''
        filename = filedialog.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=(('csv files', '*.csv'), ('All files', '*.*'))
        )
        self.csv_service.read_csv(filename=filename)
        