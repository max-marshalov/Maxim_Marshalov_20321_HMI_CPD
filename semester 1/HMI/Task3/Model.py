from PySide6.QtCore import QAbstractTableModel
class Model(QAbstractTableModel):
    def __init__(self, date=None, category=None, total=None) -> None:
        super(QAbstractTableModel, self).__init__()
        self.__date = date
        self.__category = category
        self.__total = total
    
    @property
    def date(self):
        return self.__date
    
    @property
    def category(self):
        return self.__category
    
    @property
    def total(self):
        return self.__total