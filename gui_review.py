import tkinter as tk
from tkinter import messagebox


#Функция для проверки логина и пароля
def loggin():
    user_name = entry_log.get()
    user_password = entry_password.get()

    if user_name and user_password:
        root.withdraw() #Скрываем окно входа
        
        #Открытие личного кабинета
        open_dashboard()
    else:
        messagebox.showerror("Ошибка", "Логин не был введен!")

#Открытие окна личного кабинета
def open_dashboard():
    dashboard = tk.Toplevel()
    dashboard.title("Личный кабинет")
    dashboard.geometry("600x400")

    #Заголовок в окне
    library_info_text = tk.Label(dashboard, text="Библиотека")
    library_info_text.pack(anchor="center", side="top")



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
