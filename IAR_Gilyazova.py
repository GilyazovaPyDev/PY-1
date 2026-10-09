import requests
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb


def select_1h():
    answer_1h = selected_1h.get()
    if answer_1h == 1:
        index = index_cryptocurrencies[target_combobox.get()]
        percent_change = data["data"][index]["quote"][0]["percent_change_1h"]
        l1 = Label(frame4,text=f'Цена изменилась за 1 час на: {percent_change:.2f}%')
        l1.pack()

def select_24h():
    answer_24h = selected_24h.get()
    if answer_24h == 1:
        index = index_cryptocurrencies[target_combobox.get()]
        percent_change = data["data"][index]["quote"][0]["percent_change_24h"]
        Label(frame4,text=f'Цена изменилась за 24 часа на: {percent_change:.2f}%').pack()


def select_7d():
    answer_7d = selected_7d.get()
    if answer_7d == 1:
        index = index_cryptocurrencies[target_combobox.get()]
        percent_change = data["data"][index]["quote"][0]["percent_change_7d"]
        Label(frame4,text=f'Цена изменилась за 7 дней на: {percent_change:.2f}%').pack()


def select_30d():
    answer_30d = selected_30d.get()
    if answer_30d == 1:
        index = index_cryptocurrencies[target_combobox.get()]
        percent_change = data["data"][index]["quote"][0]["percent_change_30d"]
        Label(frame4,text=f'Цена изменилась за 30 дней на: {percent_change:.2f}%').pack()


def exchange():
    if (target_combobox.get() == '' or
            target_combobox.get() not in name_crypto):
        mb.showerror('Ошибка!',
                     "Выберите целевую криптовалюту из\n"
                     "списка популярных криптовалют!")
    else:
        index = index_cryptocurrencies[target_combobox.get()]
        exchange_rate = data["data"][index]["quote"][0]["price"]


        mb.showinfo('Курс обмена криптовалюты',
                    f'Курс: {exchange_rate:.2f} Долларов США за 1 {target_combobox.get()}')


try:
    url = "https://pro-api.coinmarketcap.com/public-api/v3/cryptocurrency/listings/latest?start=1&limit=100&convert=USD"
    result = requests.get(url)
    result.raise_for_status()
    data = result.json()

    name_crypto = []
    symb_crypto = []
    index_crypto = []

    for i in range(5):
        name_crypto.append(data['data'][i]['name'])
        symb_crypto.append(data['data'][i]['symbol'])
        index_crypto.append(i)

    cryptocurrencies = dict(zip(name_crypto, symb_crypto))
    index_cryptocurrencies = dict(zip(name_crypto, index_crypto))


    root = Tk()
    WIDTH = root.winfo_screenwidth()
    HEIGHT = root.winfo_screenheight()
    Xx = 300
    Yy = 320
    root.geometry(f"{Xx}x{Yy}+{WIDTH // 2 - Xx // 2}"
                  f"+{HEIGHT // 2 - Yy // 2}")
    root.title("Курс обмена криптовалют по отношению к доллару")

    frame1 = Frame(root)
    frame1.pack(expand=True, fill="both")
    frame2 = Frame(root)
    frame2.pack(expand=True, fill="both")
    frame4 = Frame(root)
    frame4.pack(expand=True, fill="both")
    frame3 = Frame(root)
    frame3.pack(expand=True, fill="both")

    Label(frame1, text='Выберите целевую\nкриптовалюту:').grid(row=0, column=0, padx=20, pady=5)
    target_combobox = ttk.Combobox(frame1, values=name_crypto, width=15)
    target_combobox.grid(row=1, column=0, padx=20, pady=5)

    Label(frame1, text="\u27A1").grid(row=1, column=1)

    Label(frame1, text='Базовая валюта:').grid(row=0, column=2, padx=20, pady=5)
    Label(frame1, text="Доллар США").grid(row=1, column=2, padx=20)

    Label(frame2, text='Выберите период изменения цены (%):').grid(row=0, column=0, padx=20)

    selected_1h = IntVar()
    percent_1h = Checkbutton(frame2, text="Изменение за 1 час", variable=selected_1h, command=select_1h)
    percent_1h.grid(row=1, column=0, sticky=W, padx=20)

    selected_24h = IntVar()
    percent_24h = Checkbutton(frame2, text="Изменение за 24 часа", variable=selected_24h, command=select_24h)
    percent_24h.grid(row=2, column=0, sticky=W, padx=20)

    selected_7d = IntVar()
    percent_7d = Checkbutton(frame2, text="Изменение за 7 дней", variable=selected_7d, command=select_7d)
    percent_7d.grid(row=3, column=0, sticky=W, padx=20)

    selected_30d = IntVar()
    percent_30d = Checkbutton(frame2, text="Изменение за 30 дней",variable=selected_30d, command=select_30d)
    percent_30d.grid(row=4, column=0, sticky=W, padx=20)

    button = Button(frame3, text='Получить курс', command=exchange)
    button.pack()

    root.mainloop()

except Exception as e:
    mb.showerror('Ошибка!', f'error 400 {e}')

