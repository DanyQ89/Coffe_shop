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
        self.add_button = AddCoffee(self)
        self.initUI()

    def renew(self):
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'name', 'roasting', 'type', 'description', 'price', 'size'])
        res = self.cur.execute("""
        SELECT * FROM main
        """).fetchall()
        self.tableWidget.setRowCount(len(res))
        for i in range(len(res)):
            el = res[i]
            for g in range(7):
                self.tableWidget.setItem(i, g, QTableWidgetItem(str(el[g])))

    def Add(self):
        self.add_button = AddCoffee(self)
        self.add_button.show()

    def initUI(self):
        self.setWindowTitle('Coffe_shop')
        self.renew()
        for i in range(7):
            self.tableWidget.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)
        self.add.clicked.connect(self.Add)


class AddCoffee(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.con = sqlite3.connect('coffe.sqlite')
        self.cur = self.con.cursor()
        self.price.setValue(1.00)
        self.size.setValue(30)
        self.initUI()

    def run(self):
        res = self.cur.execute("""
        SELECT * FROM MAIN
        """).fetchall()
        name = self.name.text()
        roasting = self.roasting.currentText()
        ttype = self.type.currentText()
        desc = self.description.toPlainText()
        price = self.price.value()
        size = self.size.value()
        if name and roasting and ttype and desc and price and size:
            if len(name) > 1 and price > 0.00 and size > 0:
                print(f'{i} {type(i)}' for i in [name, roasting, ttype, desc, price, size])
                self.cur.execute(f"""
                INSERT OR REPLACE INTO MAIN(name, roasting, type, description, price, size)
                VALUES{(name, roasting, ttype, desc, price, size)}
                """)
                print(2)
                self.con.commit()
                self.parent().renew()
                print(3)
                self.close()

    def initUI(self):
        self.pushButton.clicked.connect(self.run)
        for i in ['roasted', 'beans']:
            self.type.addItem(i)
        for i in ['not roasted', 'low roasted', 'middle roasted', 'high roasted']:
            self.roasting.addItem(i)
        self.price.setSuffix(' $')
        self.size.setSuffix(' portions')
        self.price.setRange(1, 100000000)
        self.size.setRange(1, 10000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CoffeShop()
    ex.show()
    sys.exit(app.exec_())
