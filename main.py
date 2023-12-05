import io
import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QHeaderView

first = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>coffe_shop</class>
 <widget class="QMainWindow" name="coffe_shop">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1144</width>
    <height>534</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>40</y>
      <width>771</width>
      <height>421</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="add">
    <property name="geometry">
     <rect>
      <x>880</x>
      <y>60</y>
      <width>121</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>Add</string>
    </property>
   </widget>
   <widget class="QPushButton" name="change">
    <property name="geometry">
     <rect>
      <x>880</x>
      <y>120</y>
      <width>121</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>Change</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1144</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""
second = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>AddCoffee</class>
 <widget class="QMainWindow" name="AddCoffee">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>394</width>
    <height>570</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="gridLayoutWidget">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>0</y>
      <width>341</width>
      <height>481</height>
     </rect>
    </property>
    <layout class="QGridLayout" name="gridLayout">
     <item row="3" column="0">
      <widget class="QLabel" name="label_4">
       <property name="text">
        <string>Description</string>
       </property>
      </widget>
     </item>
     <item row="0" column="2">
      <widget class="QLineEdit" name="name"/>
     </item>
     <item row="0" column="0">
      <widget class="QLabel" name="label_2">
       <property name="text">
        <string>Name</string>
       </property>
      </widget>
     </item>
     <item row="1" column="0">
      <widget class="QLabel" name="label">
       <property name="text">
        <string>Roast</string>
       </property>
      </widget>
     </item>
     <item row="2" column="2">
      <widget class="QComboBox" name="type"/>
     </item>
     <item row="4" column="0">
      <widget class="QLabel" name="label_5">
       <property name="text">
        <string>Price</string>
       </property>
      </widget>
     </item>
     <item row="3" column="2">
      <widget class="QTextEdit" name="description"/>
     </item>
     <item row="1" column="2">
      <widget class="QComboBox" name="roasting"/>
     </item>
     <item row="5" column="0">
      <widget class="QLabel" name="label_6">
       <property name="text">
        <string>Size</string>
       </property>
      </widget>
     </item>
     <item row="2" column="0">
      <widget class="QLabel" name="label_3">
       <property name="text">
        <string>Type</string>
       </property>
      </widget>
     </item>
     <item row="4" column="2">
      <widget class="QDoubleSpinBox" name="price"/>
     </item>
     <item row="5" column="2">
      <widget class="QSpinBox" name="size"/>
     </item>
    </layout>
   </widget>
   <widget class="QPushButton" name="save">
    <property name="geometry">
     <rect>
      <x>90</x>
      <y>490</y>
      <width>171</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>Save</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>394</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

class CoffeShop(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(first)
        uic.loadUi(f, self)
        self.con = sqlite3.connect('coffe.sqlite')
        self.cur = self.con.cursor()
        self.add_button = AddCoffee(self)
        self.change_button = AddCoffee(self)
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

    def Red(self):
        row = self.tableWidget.currentRow()
        if row > -1:
            item = self.tableWidget.item(row, 0).text()
            self.change_button = AddCoffee(self, item_id=item)
            self.change_button.show()

    def initUI(self):
        self.setWindowTitle('Coffe_shop')
        self.renew()
        for i in range(7):
            self.tableWidget.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)
        self.add.clicked.connect(self.Add)
        self.change.clicked.connect(self.Red)


class AddCoffee(QMainWindow):
    def __init__(self, parent=None, item_id=None):
        super().__init__(parent)
        f = io.StringIO(second)
        uic.loadUi(f, self)
        self.item_id = item_id
        self.con = sqlite3.connect('coffe.sqlite')
        self.cur = self.con.cursor()
        self.price.setValue(1.00)
        self.size.setValue(30)
        self.initUI()

    def run(self):
        name = self.name.text()
        roasting = self.roasting.currentText()
        ttype = self.type.currentText()
        desc = self.description.toPlainText()
        price = self.price.value()
        size = self.size.value()
        if name and roasting and ttype and desc and price and size:
            if len(name) > 1 and price > 0.00 and size > 0:
                if not self.item_id:
                    self.cur.execute(f"""
                    INSERT OR REPLACE INTO MAIN(name, roasting, type, description, price, size)
                    VALUES{(name, roasting, ttype, desc, price, size)}
                    """)
                else:
                    self.cur.execute(f"""
                    UPDATE main
                    SET name='{name}', roasting='{roasting}', type='{ttype}',
                    description='{desc}', price={price}, size={size}
                    WHERE ID = {self.item_id}
                    """)
                self.con.commit()
                self.parent().renew()
                self.close()

    def initUI(self):
        self.save.clicked.connect(self.run)
        for i in ['roasted', 'beans']:
            self.type.addItem(i)
        for i in ['not roasted', 'low roasted', 'middle roasted', 'high roasted']:
            self.roasting.addItem(i)
        if self.item_id:
            res = self.cur.execute(f"""
            SELECT * FROM MAIN 
            WHERE ID = {self.item_id} 
            """).fetchone()
            self.name.setText(res[1])
            self.roasting.setCurrentText(res[2])
            self.type.setCurrentText(res[3])
            self.description.insertPlainText(res[4])
            self.price.setValue(float(res[5]))
            self.size.setValue(int(res[6]))

        self.price.setSuffix(' $')
        self.size.setSuffix(' portions')
        self.price.setRange(1, 100000000)
        self.size.setRange(1, 10000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CoffeShop()
    ex.show()
    sys.exit(app.exec_())
