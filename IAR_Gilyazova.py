import requests
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb

# Глобальные переменные
name_crypto = []  # Список для имен криптовалют
symb_crypto = []  # Список для симводов криптовалют
index_crypto = []  # Список индексов для извлечения данных
cryptocurrencies = {} # словари {имя: символ}
index_cryptocurrencies = {} # и {имя: индекс}
data = {}

#Функция получения/обновления данных (реализация запроса к API)
def update():
    global cryptocurrencies, index_cryptocurrencies, data
    try:
        # Обработка запроса с API
        url = "https://pro-api.coinmarketcap.com/public-api/v3/cryptocurrency/listings/latest?start=1&limit=100&convert=USD"
        result = requests.get(url, timeout=10)
        result.raise_for_status()
        data = result.json()
        # Получение 5 популярных криптовалют
        for i in range(5):
            name_crypto.append(data['data'][i]['name'])
            symb_crypto.append(data['data'][i]['symbol'])
            index_crypto.append(i)
        # Преобразование списков в словари {имя: символ} и {имя: индекс}
        cryptocurrencies = dict(zip(name_crypto, symb_crypto))
        index_cryptocurrencies = dict(zip(name_crypto, index_crypto))

    # Обработка ошибки исполнения запроса
    except Exception as e:
        if str(e)[:3] == '429':
            mb.showinfo("Лимит исчерпан",
                        "Лимит исчерпан!\nПожалуйста, подождите 60 секунд.")

        mb.showerror('Ошибка!', f'error {e}')

    return data, name_crypto, symb_crypto, index_crypto, cryptocurrencies, index_cryptocurrencies

#Функция очистки данных
def clear():
    #Очищаем данные изменения цены
    result_label1.config(text="")
    percent_1h.deselect()
    result_label2.config(text="")
    percent_24h.deselect()
    result_label3.config(text="")
    percent_7d.deselect()
    result_label4.config(text="")
    percent_30d.deselect()
    #Очищаем выбор криптовалюты
    target_combobox.set('')


#Функция выбора чекбокса для периода изменения цены
def select(period):
    if target_combobox.get(): # Крипта должна быть выбрана
        # Выбор периода в 1 час
        if period == 1:
            if var_1h.get() == 1:
                time_unit = "1 час"
                key = "percent_change_1h"
                index = index_cryptocurrencies[target_combobox.get()]
                percent_change = data["data"][index]["quote"][0][key]
                result_label1.config(text=f'Цена {target_combobox.get()} изменилась за {time_unit} на: {percent_change:.2f}%')
            else:
                result_label1.config(text="")
        # Выбор периода в 24 часа
        elif period == 2:
            if var_24h.get() == 1:
                time_unit = "24 часа"
                key = "percent_change_24h"
                index = index_cryptocurrencies[target_combobox.get()]
                percent_change = data["data"][index]["quote"][0][key]
                result_label2.config(
                    text=f'Цена {target_combobox.get()} изменилась за {time_unit} на: {percent_change:.2f}%')
            else:
                result_label2.config(text="")
        # Выбор периода в 7 дней
        elif period == 3:
            if var_7d.get() == 1:
                time_unit = "7 дней"
                key = "percent_change_7d"
                index = index_cryptocurrencies[target_combobox.get()]
                percent_change = data["data"][index]["quote"][0][key]
                result_label3.config(
                    text=f'Цена {target_combobox.get()} изменилась за {time_unit} на: {percent_change:.2f}%')
            else:
                result_label3.config(text="")
        # Выбор периода в 30 дней
        elif period == 4:
            if var_30d.get() == 1:
                time_unit = "30 дней"
                key = "percent_change_30d"
                index = index_cryptocurrencies[target_combobox.get()]
                percent_change = data["data"][index]["quote"][0][key]
                result_label4.config(
                    text=f'Цена {target_combobox.get()} изменилась за {time_unit} на: {percent_change:.2f}%')
            else:
                result_label4.config(text="")
    # Обработка ошибки, если крипта не выбрана
    else:
        mb.showerror('Ошибка!',
                     "Выберите целевую криптовалюту из\n"
                     "списка популярных криптовалют!")


# Функция для получения курса обмена к 1 Доллару США
def exchange():
    # Обработка ошибки, если крипта не выбрана
    if (target_combobox.get() == '' or
            target_combobox.get() not in name_crypto):
        mb.showerror('Ошибка!',
                     "Выберите целевую криптовалюту из\n"
                     "списка популярных криптовалют!")
    # Получение курса обмена
    else:
        index = index_cryptocurrencies[target_combobox.get()]
        exchange_rate = data["data"][index]["quote"][0]["price"]
        mb.showinfo('Курс обмена криптовалюты',
                    f'Курс: {exchange_rate:.2f} Долларов США за 1 {target_combobox.get()}')


# НАЧАЛО ПРОГРАММЫ
# Вызываем функцию обработки запроса
update()
# Создание интерфейса программы, пар-ры окна
root = Tk()
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
Xx = 320
Yy = 400
root.geometry(f"{Xx}x{Yy}+{WIDTH // 2 - Xx // 2}"
              f"+{HEIGHT // 2 - Yy // 2}")
root.title("Курс обмена криптовалют")

# Фреймы для
frame1 = Frame(root) # Информации о списке криптовалют
frame1.pack(expand=True, fill="both")
frame2 = Frame(root) # Выбора валюты
frame2.pack(expand=True, fill="both")
frame3 = Frame(root) # Выбора периода изменения цены и Кнопки очистить данные
frame3.pack(expand=True, fill="both")

# Информационный лейбл
Label(frame1, text="Отображаются топ-5 криптовалют\nв рейтинге по капитализации").pack(side=TOP)

# Размещение виджетов для целевой валюты
Label(frame2, text='Выберите целевую\nкриптовалюту:').grid(row=0, column=0, padx=20, pady=5)
target_combobox = ttk.Combobox(frame2, values=name_crypto, width=15)
target_combobox.grid(row=1, column=0, padx=20, pady=5)

# Cтрелочка, указывающая на базовую валюту
Label(frame2, text="\u27A1").grid(row=1, column=1)

# Размещение виджетов для базовой валюты
Label(frame2, text='Базовая валюта:').grid(row=0, column=2, padx=20, pady=5)
Label(frame2, text="\u0024Доллар США").grid(row=1, column=2, padx=20)

# Кнопка получить курс
button_ex = Button(frame2, text='Получить курс', command=exchange)
button_ex.grid(row=2, column=0, padx=5, pady=5)

# Кнопка Обновить данные
button_upd = Button(frame2, text='Обновить данные', command=update)
button_upd.grid(row=2, column=2, padx=5, pady=5)

# Новый фрейм для выбора периода изменения цены и его виджеты
Label(frame3, text='Выберите период изменения цены (%):').pack()

# Изменение цены за 1 час
var_1h = IntVar()
percent_1h = Checkbutton(frame3, text="Изменение за 1 час", variable=var_1h, command=lambda:select(1))
percent_1h.pack()
result_label1 = Label(frame3, text="")
result_label1.pack()

# Изменение цены за 24 часа
var_24h = IntVar()
percent_24h = Checkbutton(frame3, text="Изменение за 24 часа", variable=var_24h, command=lambda:select(2))
percent_24h.pack()
result_label2 = Label(frame3, text="")
result_label2.pack()

# Изменение цены за 7 дней
var_7d = IntVar()
percent_7d = Checkbutton(frame3, text="Изменение за 7 дней", variable=var_7d, command=lambda:select(3))
percent_7d.pack()
result_label3 = Label(frame3, text="")
result_label3.pack()

# Изменение цены за 30 дней
var_30d = IntVar()
percent_30d = Checkbutton(frame3, text="Изменение за 30 дней",variable=var_30d, command=lambda:select(4))
percent_30d.pack()
result_label4 = Label(frame3, text="")
result_label4.pack()

# Кнопка для очистки чекбоксов и комбобокса с криптовалютами
button_clr = Button(frame3, text='Очистить данные', command=clear)
button_clr.pack(pady=5, padx=5)


root.mainloop()

