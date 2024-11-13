import tkinter as tk
from tkinter import messagebox
from library_code import main as lb
import database as db

library = lb.Library()


#Функция для проверки логина и пароля
def loggin():
    global user_name

    user_get_name = entry_log.get()
    user_name = lb.Reader(user_get_name)
    user_password = entry_password.get()

    user = db.get_user(user_get_name)

    if user and user[2] == user_password:
        if user[3] == 'admin':
            root.withdraw()
            messagebox.showinfo("Вы вошли в систему как админ")
            opem_admin_dashboard()
        elif user[3] == 'user':
            root.withdraw()
            messagebox.showinfo("Вы вошли в систему!")
            open_dashboard()
    else:
        messagebox.showerror("Проблема со входом, попробуйте еще раз!")
        
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

#Личный кабинет админа
def opem_admin_dashboard():
    global admin_dashboard
    global get_title
    global get_author
    global get_year

    admin_dashboard = tk.Toplevel()
    admin_dashboard.title("Личный кабинет админа")
    admin_dashboard.geometry("600x400")

    #Информации о пользователе в правом верхнем углу
    user_info_text = tk.Label(admin_dashboard, text=f"Вы вошли как админ под логином: {user_name.name}")
    user_info_text.pack(anchor="ne", side="top")

    #Кнопка выхода с личного кабинета
    log_out_button = tk.Button(admin_dashboard, text="Выход", command=lambda: log_out(admin_dashboard))
    log_out_button.pack(anchor="ne", side="top")

    #Заголовок в окне
    library_info_text = tk.Label(admin_dashboard, text="Добавление книги в библиотеку")
    library_info_text.pack(anchor="center", side="top")

    title_text = tk.Label(admin_dashboard, text="Введите название книги")
    get_title = tk.Entry(admin_dashboard, fg="black", bg="white")
    title_text.pack(anchor="center", side="left")
    get_title.pack(anchor="center", side="left")

    author_text = tk.Label(admin_dashboard, text="Введите автора книги")
    get_author = tk.Entry(admin_dashboard, fg="black", bg="white")
    author_text.pack(anchor="center", side="left")
    get_author.pack(anchor="center", side="left")

    year_text = tk.Label(admin_dashboard, text="Введите год выпуска книги")
    get_year = tk.Entry(admin_dashboard, fg="black", bg="white")
    year_text.pack(anchor="center", side="left")
    get_year.pack(anchor="center", side="left")

    send_info = tk.Button(admin_dashboard, text="Press", command=add_book)
    send_info.pack(anchor="center", side="left")

    cb = tk.Button(admin_dashboard, text="тест", command=tester)
    cb.pack(anchor="center", side="left")

#Добавления книги в библиотеку
def add_book():
    #Достаем данные которые ввел пользователь
    title = get_title.get()
    author = get_author.get()
    year = get_year.get()
    book = lb.Book(title, author, int(year))#Создаем из полученой информации класс

    library.add_book(book)

    #Чистим поля ввода
    get_title.delete(0, 'end')
    get_author.delete(0, 'end')
    get_year.delete(0, 'end')

    #При вовыде получем ссылку на список,  нужно это исправить


#Проверка на добавление книг в список
def tester():
    for i in library.get_list:
        print(i)

def open_borrow_book():
    dashboard.destroy()

    borrow_book = tk.Toplevel()
    borrow_book.title("Взять книгу")
    borrow_book.geometry("600x400")

    #Информации о пользователе в правом верхнем углу
    user_info_text = tk.Label(borrow_book, text=f"Вы вошли под логином: {user_name.name}")
    user_info_text.pack(anchor="ne", side="top")

    #Кнопка выхода с личного кабинета
    log_out_button = tk.Button(borrow_book, text="Выход", command=lambda: log_out(borrow_book))
    log_out_button.pack(anchor="ne", side="top")

    #Заголовок в окне
    borrow_book_title = tk.Label(borrow_book, text="Выберите книгу которую хотите взять")
    borrow_book_title.pack(anchor="center", side="top")

    #Создание листа
    """
    1. Поробовать создать отдельный списко для теста из книг
    2. В случае работы, попытатся подключить работу класов, если это возможно
    3. Если это будет не возможно тогда делаем так:
        1. Оставляем лист для одолжения книг работать на основе информации с отдельного списками книг
        2. Так как для реализации работы листа со списком добавленых книг будет не возможна, 
         нужно начать работу над окном админа для добавления книг
        3. Протестировать работу кода, добавить сохранения паролей и логинов в базу данных
    """
    brw_books_list = tk.Listbox(borrow_book)
    for i in lb.Library.get_list:
        for x in len(lb.library.books_list):
            brw_books_list.insert(x, i.title)
    


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
