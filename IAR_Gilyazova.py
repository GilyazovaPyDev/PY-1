import requests
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb


def exchange():
    if (target_combobox.get() == '' or
            target_combobox.get() not in list(cryptocurrencies.keys())):
        mb.showerror('Ошибка!',
                     "Выберите целевую криптовалюту из\n"
                     "списка популярных криптовалют!")
    else:
        base_code = "usd"
        target_code = cryptocurrencies[target_combobox.get()]
        url = "https://pro-api.coinmarketcap.com/public-api/v2/simple/price"
        params = {
            "convert": base_code,
            "symbol": target_code,
            "include_24h_change": "true",
            "precision": 3
        }
        try:
            result = requests.get(url, params=params)
            result.raise_for_status()
            data = result.json()
            print(data)
            exchange_rate = data["data"][0]["quotes"][0]["price"]

            mb.showinfo('Курс обмена криптовалюты',
                        f'Курс: {exchange_rate} Долларов США за 1 {target_combobox.get()}')

        except Exception as e:
            mb.showerror('Ошибка!', f'error 400 {e}')


cryptocurrencies = {
    "Bitcoin" : "BTC",
    "Ethereum" : "ETH",
    "Tether": "USDT",
    "BNB" : "BNB",
    "XRP" : "XRP"
}

root = Tk()
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
Xx = 300
Yy = 200
root.geometry(f"{Xx}x{Yy}+{WIDTH // 2 - Xx // 2}"
              f"+{HEIGHT // 2 - Yy // 2}")
root.title("Курс обмена криптовалют по отношению к доллару")

Label(text='Выберите целевую криптовалюту:').pack(pady=10, padx=10)
target_combobox = ttk.Combobox(values=list(cryptocurrencies.keys()))
target_combobox.pack()

Label(text='Базовая валюта:').pack(pady=10, padx=10)
Label(text="Доллар США").pack()

button = Button(text='Получить курс', command=exchange)
button.pack(pady=10)


root.mainloop()
