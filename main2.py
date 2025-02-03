import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt6 import uic

import sys


class CoffeeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Информация о кофе")
        self.setGeometry(100, 100, 800, 600)
        uic.loadUi('main.ui', self)

        self.coffeeButton.clicked.connect(self.open_new_chapter)

        self.load_coffee_data()

    def open_window(self, x, y):
        self.move(x, y)
        self.show()

    def open_new_chapter(self):
        frame_geometry = self.frameGeometry()
        frame_x = frame_geometry.x()
        frame_y = frame_geometry.y()

        self.hide()

        if not hasattr(self, "minesweeper_settings"):
            self.edit_info = addEditCoffeeForm()
        self.edit_info.open_window(frame_x, frame_y)

    def load_coffee_data(self):
        conn = sqlite3.connect('coffee.sqlite')
        cursor = conn.cursor()

        rows = cursor.execute('''
            SELECT
                ID, Название_сорта, Степень_обжарки, Молотый_в_зернах, Описание_вкуса, Цена, Объем_упаковки 
            FROM 
                coffee''').fetchall()

        conn.close()

        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(
            ["ID", "Название сорта", "Степень обжарки", "Молотый/в зернах", "Описание вкуса", "Цена", "Объем упаковки"])

        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))

        self.tableWidget.resizeColumnsToContents()


class addEditCoffeeForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Информация о кофе")
        self.setGeometry(100, 100, 800, 600)
        uic.loadUi('addEditCoffeeForm.ui', self)

        self.exitButton.clicked.connect(self.open_new_chapter)
        self.applyButton.clicked.connect(self.change_coffee_table)

        self.idEdit.setPlaceholderText('ID')
        self.nameEdit.setPlaceholderText('Название')
        self.degreeEdit.setPlaceholderText('Степень обжарки')
        self.typeEdit.setPlaceholderText('Молотый/в зернах')
        self.descriptionEdit.setPlaceholderText('Описание вкуса')
        self.priceEdit.setPlaceholderText('Цена')
        self.volumeEdit.setPlaceholderText('Объем упаковки')

    def change_coffee_table(self):
        changes = True

        id = self.idEdit.text()
        name = self.nameEdit.text()
        degree = self.degreeEdit.text()
        type = self.typeEdit.text()
        description = self.descriptionEdit.text()
        price = self.priceEdit.text()
        volume = self.volumeEdit.text()

        conn = sqlite3.connect('coffee.sqlite')
        cursor = conn.cursor()

        rows = list(cursor.execute('''
            SELECT
                ID, Название_сорта, Степень_обжарки, Молотый_в_зернах, Описание_вкуса, Цена, Объем_упаковки 
            FROM 
                coffee''').fetchall())

        for i in range(len(rows)):
            if rows[i][0] == int(id):
                cursor.execute('''
                UPDATE 
                    coffee
                SET
                    Название_сорта = ?, Степень_обжарки = ?, Молотый_в_зернах = ?, Описание_вкуса = ?, Цена = ?, Объем_упаковки = ?
                WHERE
                    id = ?
                ''', (name, degree, type, description, price, volume, id))
                changes = False
                break

        if changes:
            cursor.execute('''
            INSERT INTO
                coffee(ID, Название_сорта, Степень_обжарки, Молотый_в_зернах, Описание_вкуса, Цена, Объем_упаковки)
            VALUES
                (?, ?, ?, ?, ?, ?, ?)
            ''', (id, name, degree, type, description, price, volume))

        conn.commit()

    def open_window(self, x, y):
        self.move(x, y)
        self.show()

    def open_new_chapter(self):
        frame_geometry = self.frameGeometry()
        frame_x = frame_geometry.x()
        frame_y = frame_geometry.y()

        self.hide()

        if not hasattr(self, "minesweeper_settings"):
            self.menu = CoffeeApp()
        self.menu.open_window(frame_x, frame_y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec())
