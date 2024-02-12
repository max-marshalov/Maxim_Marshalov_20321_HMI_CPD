##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-01 3:26:24 pm
 # @copyright SMTU
 #
import csv
import tkinter as tk
class CsvService:
    '''Сервис, предназначенный для чтения и записи csv файлов'''
    def __init__(self, table) -> None:
        '''Принимает ссылку на таблицу, для отображения'''
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