import csv
import tkinter as tk
class CsvService:
    def __init__(self, table) -> None:
        self._table = table

    def write_csv(self, filename):
        with open(filename, mode='w', encoding='utf-8') as csv_file:
            file_writer = csv.writer(csv_file, delimiter = ",", lineterminator="\r")
            for item in self._table.get_children():
                file_writer.writerow(self._table.item(item)['values'])
    
    def read_csv(self, filename):
        with open(filename, encoding='utf-8') as csv_file:
             file_reader = csv.reader(csv_file, delimiter = ",", lineterminator="\r")
             self._table.delete(*self._table.get_children())
             for rows in file_reader:
                 self._table.insert("", tk.END, values=rows)