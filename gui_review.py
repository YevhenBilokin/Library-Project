import tkinter as tk
from tkinter import messagebox
from library_code import main as lb

#Функция для проверки логина и пароля
def loggin():
    global user_name

    user_name = lb.Reader(entry_log.get())
    user_password = entry_password.get()

    if user_name and user_password:
        root.withdraw() #Скрываем окно входа
        
        #Открытие личного кабинета
        open_dashboard()
    else:
        messagebox.showerror("Ошибка", "Логин не был введен!")

#Функция для возвращения к меню авторизации
def log_out(dashboard):
    dashboard.destroy()
    root.deiconify()

#Открытие окна личного кабинета
def open_dashboard():
    global dashboard

    dashboard = tk.Toplevel()
    dashboard.title("Личный кабинет")
    dashboard.geometry("600x400")

    #Информации о пользователе в правом верхнем углу
    user_info_text = tk.Label(dashboard, text=f"Вы вошли под логином: {user_name.name}")
    user_info_text.pack(anchor="ne", side="top")

    #Кнопка выхода с личного кабинета
    log_out_button = tk.Button(dashboard, text="Выход", command=lambda: log_out(dashboard))
    log_out_button.pack(anchor="ne", side="top")

    #Заголовок в окне
    library_info_text = tk.Label(dashboard, text="Библиотека")
    library_info_text.pack(anchor="center", side="top")
    
    
    button_frame = tk.Frame(dashboard)
    button_frame.pack(pady=20)

    borrow_book_button = tk.Button(button_frame, text="Взять книгу", command=open_borrow_book)
    return_book_button = tk.Button(button_frame, text="Вернуть книгу")
    borrow_book_list_button = tk.Button(button_frame, text="Список взятых книг")

    borrow_book_button.pack(side="left", padx=10)
    return_book_button.pack(side="left", padx=10)
    borrow_book_list_button.pack(side="left", padx=10)


def open_borrow_book():
    dashboard.destroy()

    borrow_book = tk.Toplevel()
    borrow_book.title("Взять книгу")
    root.geometry("600x400")

    #Информации о пользователе в правом верхнем углу
    user_info_text = tk.Label(borrow_book, text=f"Вы вошли под логином: {user_name.name}")
    user_info_text.pack(anchor="ne", side="top")

    #Кнопка выхода с личного кабинета
    log_out_button = tk.Button(borrow_book, text="Выход", command=lambda: log_out(borrow_book))
    log_out_button.pack(anchor="ne", side="top")

    borrow_book_title = tk.Label(borrow_book, text="Выберите книгу которую хотите взять")
    borrow_book_title.pack(anchor="center", side="top")





root = tk.Tk()

#Окно входа
root.title("Вход в личный кабинет")
root.geometry("600x400")
root.configure(bg="grey")


#Ввод логина
loigin_frame = tk.Frame(root, bg="grey")
loigin_frame.pack(pady=20)

log_text = tk.Label(loigin_frame, text="Введите логин: ", fg="black", bg="white")
entry_log = tk.Entry(loigin_frame, fg="black", bg="white",width=15)

log_text.pack(anchor="center", pady=5)
entry_log.pack(anchor="center", pady=5)

#Ввод пароля
password_frame = tk.Frame(root, bg="grey")
password_frame.pack(pady=20)

password_test = tk.Label(password_frame, text="Введите пароль: ", fg="black", bg="white")
entry_password = tk.Entry(password_frame, show="*", fg="black", bg="white",width=15)

password_test.pack(anchor="center", pady=5)
entry_password.pack(anchor="center", pady=5)

#Кнопка для входа
enter_button = tk.Button(root, text="Press", command=loggin).pack(anchor="center")


# Запуск основного цикла
root.mainloop()
