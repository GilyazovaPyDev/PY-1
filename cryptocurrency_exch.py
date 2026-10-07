import requests
# import json
# import pprint
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb

def exchange():
    target_code = "usd"
    base_code = base_combobox.get().lower()
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "vs_currencies": target_code,
        "ids": base_code,
    }

    if target_code and base_code:
        try:
            result = requests.get(url, params=params)
            result.raise_for_status()
            data = result.json()
            print(data)

            exchange_rate = data.get(base_code).get(target_code)

            mb.showinfo('Курс обмена криптовалюты',
                        f'Курс {exchange_rate} {base_code} за 1 {target_code}')

        except Exception as e:
            mb.showerror('Ошибка!', f'error 400 {e}')

    else:
        mb.showerror('Ошибка!', "Выберите базовую валюту!")


cryptocurrencies = ["Bitcoin", "Ethereum", "Tether", "BNB", "XRP"]


root = Tk()
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
Xx = 300
Yy = 200
root.geometry(f"{Xx}x{Yy}+{WIDTH // 2 - Xx // 2}"
              f"+{HEIGHT // 2 - Yy // 2}")
root.title("Курс обмена криптовалют по отношению к доллару")

Label(text='Базовая валюта:').pack(pady=10, padx=10)
Label(text="Доллар США").pack()

Label(text='Выберите целевую криптовалюту:').pack(pady=10, padx=10)
base_combobox = ttk.Combobox(values=cryptocurrencies)
base_combobox.pack()


button = Button(text='Получить курс', command=exchange)
button.pack(pady=10)


root.mainloop()


#
#
# print(data)
# print(data.keys())
# print(data.get("bitcoin").get("usd"))
