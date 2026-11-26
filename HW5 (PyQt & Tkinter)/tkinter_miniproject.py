import sqlite3
import tkinter as tk
from tkinter import messagebox

DATA = "users_db.db"
conn = sqlite3.connect(DATA)

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Информация")
        self.root.geometry("600x400")
        self.root.configure(bg="blue")
        self.root.resizable(False, False)

        self.saved_name = ""
        self.saved_surname = ""

        self.about = tk.Text(
            self.root,
            bg="white",
            fg="black",
            font=("Arial", 16),
            wrap="word"
        )
        self.about.place(x=10, y=220, width=500, height=120)
        self.about.config(state="disabled")

        self.info_label = tk.Label(
            self.root,
            text="После сохранения имени и фамилии тут\n"
                 "появится найденная информация о Вас",
            bg="blue",
            fg="white",
            font=("Arial", 16, "bold"),
            justify="left")
        self.info_label.place(x=10, y=170)

        self.success = tk.Label(
            self.root,
            text="",
            bg="blue",
            fg="white",
            font=("Arial", 16, "bold"))
        self.success.place(x=10, y=350)

        self.hello_label = tk.Label(
            self.root,
            text="Напишите свои имя и фамилию в окна ниже",
            bg="blue",
            fg="white",
            font=("Arial", 16, "bold"))
        self.hello_label.place(x=10, y=10)

        self.name = tk.Entry(
            self.root,
            bg="white",
            fg="black",
            font=("Arial", 16))
        self.name.place(x=10, y=50, width=400, height=30)
        self.name.insert(0, "")
        self.name.config()

        self.name_label = tk.Label(self.root,
                                   text="Имя",
                                   bg="blue",
                                   fg="white",
                                   font=("Arial", 16, "bold"),
                                   justify="left")
        self.name_label.place(x=420, y=50)

        self.surname = tk.Entry(
            self.root,
            bg="white",
            fg="black",
            font=("Arial", 16))
        self.surname.place(x=10, y=90, width=400, height=30)

        self.surname_label = tk.Label(self.root,
                                   text="Фамилия",
                                   bg="blue",
                                   fg="white",
                                   font=("Arial", 16, "bold"),
                                   justify="left")
        self.surname_label.place(x=420, y=90)

        self.save = tk.Button(
            self.root,
            text="Сохранить",
            command=self.save_data,
            fg="#000000",
            font=("Arial", 14, "italic"),
            highlightbackground="#0000FF")
        self.save.place(x=10, y=130)

        self.save2 = tk.Button(
            self.root,
            text="Сохранить информацию",
            command=self.save2_data,
            fg="#000000",
            font=("Arial", 14, "italic"),
            highlightbackground="#0000FF")
        self.save2.place(x=10, y=340)
        self.save2.place_forget()

    def save_data(self):
        self.about.config(state="normal")
        self.about.delete("1.0", tk.END)

        name = self.name.get().strip()
        surname = self.surname.get().strip()
        about = "Ничего неизвестно"

        if not name or not surname:
            messagebox.showwarning("Ошибка","Пожалуйста, заполните оба поля!")
            return

        cursor = conn.cursor()
        cursor.execute("SELECT about FROM people WHERE name = ? AND surname = ?",
            (name, surname))
        result = cursor.fetchone()

        if result is not None:
            self.info_label.config(text=f"Привет, {name}! Ниже информация о Вас, которую мы нашли.\n"
                     "Вы можете дополнить или изменить ее:")
            about_text = result[0] if result[0] else ""
            self.about.insert("1.0", about_text)
        else:
            cursor.execute("INSERT INTO people (name, surname, about) VALUES (?, ?, ?)",
                (name, surname, about))

            self.info_label.config(text=f"Привет, {name}! Что расскажете о себе?")

        self.save2.place(x=10, y=340)
        self.about.config(state="normal")
        self.saved_name = name
        self.saved_surname = surname
        conn.commit()

    def save2_data(self):
        new_about = self.about.get("1.0", tk.END).strip()
        if not new_about:
            new_about = "Ничего неизвестно"

        name = self.name.get().strip()
        surname = self.surname.get().strip()

        if name != self.saved_name or surname != self.saved_surname:
            messagebox.showwarning("Ошибка!","Имя или фамилия были изменены! "
                "Сначала нажмите Сохранить")
            return

        cursor = conn.cursor()

        cursor.execute("UPDATE people SET about = ? WHERE name = ? AND surname = ?",
            (new_about, name, surname))

        conn.commit()
        self.success.config(text="Данные успешно сохранены!")

        self.root.after(5000, lambda: self.success.config(text=""))
        self.name.delete(0, tk.END)
        self.surname.delete(0, tk.END)
        self.about.config(state="normal")
        self.about.delete("1.0", tk.END)
        self.about.config(state="disabled")

        self.save2.place_forget()

        self.info_label.config(text="После сохранения имени и фамилии тут\n"
                 "появится найденная информация о Вас")

        self.saved_name = ""
        self.saved_surname = ""


app = tk.Tk()
window = MainWindow(app)
app.mainloop()
conn.close()
