import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QHeaderView


class CoffeShop(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect('coffe.sqlite')
        self.cur = self.con.cursor()
        self.initUI()

    def renew(self):
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'name', 'roasting', 'type', 'description', 'price', 'size(portions)'])
        res = self.cur.execute("""
        SELECT * FROM main
        """).fetchall()
        self.tableWidget.setRowCount(len(res))
        for i in range(len(res)):
            el = res[i]
            for g in range(7):
                self.tableWidget.setItem(i, g, QTableWidgetItem(str(el[g])))

    def initUI(self):
        self.setWindowTitle('Coffe_shop')
        self.renew()
        for i in range(7):
            self.tableWidget.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CoffeShop()
    ex.show()
    sys.exit(app.exec_())
