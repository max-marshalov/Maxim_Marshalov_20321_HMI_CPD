##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-13 11:14:36 am
 # @copyright SMTU
 #
from typing import Optional
import os
import PySide6.QtGui
from MainWin import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QHeaderView, QTableWidgetItem, QMenu
from PySide6.QtCore import QAbstractTableModel
import sys
from Model import Model
import icons


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui_window = Ui_MainWindow()
        self.ui_window.setupUi(self)
        self.date = ""
        self.headers = ('Дата', 'Категория', 'Сумма')

        self.ui_window.tableWidget.setSortingEnabled(True)
        self.ui_window.tableWidget.setShowGrid(True)
        self.ui_window.tableWidget.setColumnCount(3)
        self.ui_window.tableWidget.setColumnWidth(0, 154)
        self.ui_window.tableWidget.setColumnWidth(1, 154)
        self.ui_window.tableWidget.setColumnWidth(2, 154)
        self.ui_window.tableWidget.setHorizontalHeaderLabels(self.headers)

        self.ui_window.add_btn.clicked.connect(self.grab_data)
        self.ui_window.date_widget.clicked.connect(self.get_date)
    
    def get_date(self, qDate):
        self.date = '{0}-{1}-{2}'.format(qDate.month(), qDate.day(), qDate.year())

    def grab_data(self):
        try:
            self.get_date(self.ui_window.date_widget.selectedDate())
            category = self.ui_window.category_place.text()
            total = self.ui_window.total_place.text()
            self.show_data(category, total)
        except Exception as e:
            print(e)
    def show_data(self, category, total):
        rowPosition = self.ui_window.tableWidget.rowCount()
        self.ui_window.tableWidget.insertRow(rowPosition)
        self.ui_window.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(self.date))
        self.ui_window.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(category))
        self.ui_window.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(total))
    
    def contextMenuEvent(self, event) -> None:
        contextMenu = QMenu()
        upload_action = contextMenu.addAction("Выгрузить данные")
        download_action = contextMenu.addAction("Загрузить данные")
        action = contextMenu.exec_(event.globalPos())
        return super().contextMenuEvent(event)
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())