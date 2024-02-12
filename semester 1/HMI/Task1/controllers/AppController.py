##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-01 3:26:37 pm
 # @copyright SMTU
 #
import tkinter as tk
from tkinter import filedialog, messagebox
from services.CsvService import CsvService
class AppController:
    def __init__(self, date_field, category_field, price_field, table) -> None:
        '''Контроллер приложения, обрабатывает все события от кнопок и полей ввода.\n
        В конструктор необходимо передать ссылку на объект календаря, поля категории, поля стоимости 
        и ссылку на таблицу для отображения'''
        self._table = table
        self._date_field = date_field
        self._categroy_field= category_field 
        self._price_filed = price_field
        self.csv_service = CsvService(self._table)
        self.total_message = tk.DoubleVar()
        self._total = 0

    def add_entry(self):
        '''Добавляет в таблицу новую запись'''
        self._table.insert("", tk.END, values=(f"{self._date_field.get_date()}", f"{self._categroy_field.get()}", f"{self._price_filed.get()}"))

    def delete_entry(self):
        '''Удаляет выбранную запись'''
        selected_item = self._table.selection()[0]
        self._table.delete(selected_item)
    
    def save_table(self):
        '''Сохраняет расходы в формат csv'''
        try:
            filename = filedialog.asksaveasfilename(title='Open a file', initialdir='/', filetypes=(('csv files', '*.csv'), ('All types', '*.*'))) + ".csv"
            self.csv_service.write_csv(filename=filename)
        except Exception:
            messagebox.showerror("Предупреждение", "Файл не был сохранен")
    
    def load_table(self):
        '''Подгружает старые csv-файлы'''
        try:
            filename = filedialog.askopenfilename(
                title='Open a file', initialdir='/', filetypes=(('csv files', '*.csv'), ('All files', '*.*'))
            )
            self.csv_service.read_csv(filename=filename)
        except FileNotFoundError:
            messagebox.showerror("Предупреждение", "Файл не был выбран")

    def calculate_total(self, event):
        '''Считает общую сумму'''
        self._total = 0
        for item in self._table.get_children():
            self._total += float(self._table.item(item)['values'][-1])
        self.total_message.set(self._total)
             
        