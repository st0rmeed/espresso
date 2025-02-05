import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import sys

from UI.converted_main import Ui_MainWindow as Ui_MainWindow1
from UI.converted_addEditCoffeeForm import Ui_MainWindow as Ui_MainWindow2


class CoffeeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow1()
        self.ui.setupUi(self)

        self.ui.coffeeButton.clicked.connect(self.open_new_chapter)

        self.load_coffee_data()

    def open_window(self, x, y):
        self.move(x, y)
        self.show()

    def open_new_chapter(self):
        frame_geometry = self.frameGeometry()
        frame_x = frame_geometry.x()
        frame_y = frame_geometry.y()

        self.hide()

        self.ui.edit_info = AddEditCoffeeForm()
        self.ui.edit_info.open_window(frame_x, frame_y)

    def load_coffee_data(self):
        conn = sqlite3.connect('./data/coffee.sqlite')
        cursor = conn.cursor()

        rows = cursor.execute('''
            SELECT
                ID, Название_сорта, Степень_обжарки, Молотый_в_зернах, Описание_вкуса, Цена, Объем_упаковки 
            FROM 
                coffee''').fetchall()

        conn.close()

        self.ui.tableWidget.setRowCount(len(rows))
        self.ui.tableWidget.setColumnCount(7)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ["ID", "Название сорта", "Степень обжарки", "Молотый/в зернах", "Описание вкуса", "Цена", "Объем упаковки"]
        )

        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))

        self.ui.tableWidget.resizeColumnsToContents()


class AddEditCoffeeForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui2 = Ui_MainWindow2()
        self.ui2.setupUi(self)

        self.ui2.exitButton.clicked.connect(self.open_new_chapter)
        self.ui2.applyButton.clicked.connect(self.change_coffee_table)

        self.ui2.idEdit.setPlaceholderText('ID')
        self.ui2.nameEdit.setPlaceholderText('Название')
        self.ui2.degreeEdit.setPlaceholderText('Степень обжарки')
        self.ui2.typeEdit.setPlaceholderText('Молотый/в зернах')
        self.ui2.descriptionEdit.setPlaceholderText('Описание вкуса')
        self.ui2.priceEdit.setPlaceholderText('Цена')
        self.ui2.volumeEdit.setPlaceholderText('Объем упаковки')

    def change_coffee_table(self):
        coffee_id = self.ui2.idEdit.text()
        name = self.ui2.nameEdit.text()
        degree = self.ui2.degreeEdit.text()
        coffee_type = self.ui2.typeEdit.text()
        description = self.ui2.descriptionEdit.text()
        price = self.ui2.priceEdit.text()
        volume = self.ui2.volumeEdit.text()

        conn = sqlite3.connect('./data/coffee.sqlite')
        cursor = conn.cursor()

        cursor.execute('SELECT ID FROM coffee WHERE ID = ?', (coffee_id,))
        existing_entry = cursor.fetchone()

        if existing_entry:
            cursor.execute('''
                UPDATE coffee
                SET
                    Название_сорта = ?, Степень_обжарки = ?, Молотый_в_зернах = ?, 
                    Описание_вкуса = ?, Цена = ?, Объем_упаковки = ?
                WHERE ID = ?
            ''', (name, degree, coffee_type, description, price, volume, coffee_id))
        else:
            cursor.execute('''
                INSERT INTO coffee (ID, Название_сорта, Степень_обжарки, Молотый_в_зернах, 
                Описание_вкуса, Цена, Объем_упаковки)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (coffee_id, name, degree, coffee_type, description, price, volume))

        conn.commit()
        conn.close()

    def open_window(self, x, y):
        self.move(x, y)
        self.show()

    def open_new_chapter(self):
        frame_geometry = self.frameGeometry()
        frame_x = frame_geometry.x()
        frame_y = frame_geometry.y()

        self.hide()

        self.menu = CoffeeApp()
        self.menu.open_window(frame_x, frame_y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec())
