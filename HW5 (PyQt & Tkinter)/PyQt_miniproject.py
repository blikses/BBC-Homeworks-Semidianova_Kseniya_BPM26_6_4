import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox, QTextEdit
from PyQt6.QtCore import QTimer

import sqlite3

DATA = "users_db.db"
conn = sqlite3.connect(DATA)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Информация")
        self.setGeometry(500, 500, 600, 400)
        self.style()
        self.saved_name = ""
        self.saved_surname = ""

        self.about = QTextEdit(self)
        self.about.move(10, 195)
        self.about.resize(500, 120)
        self.about.setReadOnly(True)

        self.info_label = QLabel("После сохранения имени и фамилии тут \n"
                                 "появится найденная информация о Вас", self)
        self.info_label.move(10, 145)
        self.info_label.adjustSize()

        self.success = QLabel(self)
        self.success.move(10, 350)
        self.success.adjustSize()

        self.hello_label = QLabel(self)
        self.hello_label.setText("Напишите свои имя и фамилию в окна ниже")
        self.hello_label.move(10, 10)
        self.hello_label.resize(self.hello_label.sizeHint())

        self.name = QLineEdit(self)
        self.name.move(10, 30)
        self.name.resize(400, 30)
        self.name.setPlaceholderText("Ваше имя")

        self.surname = QLineEdit(self)
        self.surname.move(10, 60)
        self.surname.resize(400, 30)
        self.surname.setPlaceholderText("Ваша фамилия")

        self.save = QPushButton("Сохранить", self)
        self.save.move(10, 100)
        self.save.adjustSize()
        self.save.clicked.connect(self.save_data)

        self.save2 = QPushButton("Сохранить информацию", self)
        self.save2.move(10, 315)
        self.save2.hide()
        self.save2.adjustSize()
        self.save2.clicked.connect(self.save2_data)

    def style(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: blue;
            }
            QLabel {
                color: #FFFFFF;
                font-family: Arial;
                font-size: 16px;
                font-weight: bold;
            }
            QLineEdit, QTextEdit {
                background-color: #FFFFFF;
                color: #000000;
                border: 2px solid #00008B;
                border-radius: 5px;
                padding: 4px 6px;
                font-family: Arial;
                font-size: 16px;
            }
            QTextEdit {
                border-radius: 8px;
            }
            QPushButton {
                background-color: #808080;
                color: #FFFFFF;
                font-style: italic;
                font-size: 14px;
                border-radius: 5px;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #696969;
            }
            
            QMessageBox QLabel {
                color: #000000;
                font-size: 14px;
                font-weight: normal;
            }
        """)


    def save_data(self):
        self.about.clear()
        name = self.name.text().strip()
        surname = self.surname.text().strip()
        about = "Ничего неизвестно"
        if not name or not surname:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните оба поля!")
            return
        cursor = conn.cursor()
        cursor.execute("SELECT about FROM people WHERE name = ? AND surname = ?", (name, surname))
        result = cursor.fetchone()
        if result is not None:
            self.info_label.setText(f"Привет, {name}! Ниже информация о Вас, которую мы нашли.\n"
                                    f"Вы можете дополнить или изменить ее:")
            self.info_label.resize(self.info_label.sizeHint())
            about_text = result[0] if result[0] else ""
            self.about.setPlainText(about_text)

        else:
            cursor.execute("INSERT INTO people (name, surname, about) VALUES (?, ?, ?)",
                (name, surname, about))
            self.info_label.setText(f"Привет, {name}! Что расскажете о себе?")

        self.info_label.resize(self.info_label.sizeHint())
        self.save2.show()
        self.about.setReadOnly(False)
        self.saved_name = name
        self.saved_surname = surname
        conn.commit()

    def save2_data(self):
        new_about = self.about.toPlainText().strip()
        if not new_about:
            new_about = "Ничего неизвестно"
        name = self.name.text().strip()
        surname = self.surname.text().strip()
        if name != self.saved_name or surname != self.saved_surname:
            QMessageBox.warning(self,"Ошибка!", "Имя или фамилия были изменены! Сначала нажмите Сохранить")
            return
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE people SET about = ? WHERE name = ? AND surname = ?",
            (new_about, name, surname)
        )
        self.success.setText("Данные успешно сохранены!")
        QTimer.singleShot(5000, self.success.clear)
        self.success.resize(self.success.sizeHint())
        self.name.clear()
        self.surname.clear()
        self.about.clear()
        self.save2.hide()
        self.info_label.setText("После сохранения имени и фамилии тут \n"
                                 "появится найденная информация о Вас")
        self.info_label.resize(self.info_label.sizeHint())
        self.about.setReadOnly(True)
        self.saved_name = ""
        self.saved_surname = ""
        conn.commit()

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
conn.close()