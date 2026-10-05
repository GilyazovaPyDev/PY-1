import requests
# import json
# import pprint
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb


def update_currency_t_label(event):
    code = target_combobox.get()
    name = currencies[code]
    currency_t_label.config(text=name)


def update_currency_b1_label(event):
    code = base1_combobox.get()
    name = currencies[code]
    currency_b1_label.config(text=name)


def update_currency_b2_label(event):
    code = base2_combobox.get()
    name = currencies[code]
    currency_b2_label.config(text=name)


def exchange():
    # code = entry.get().strip().upper()
    target_code = target_combobox.get()
    base1_code = base1_combobox.get()
    base2_code = base2_combobox.get()
    if target_code and base1_code and base2_code:
        try:
            result1 = requests.get(f"https://open.er-api.com/v6/latest/{base1_code}")
            result1.raise_for_status()
            # data = json.loads(result.text)
            data1 = result1.json()

            result2 = requests.get(f"https://open.er-api.com/v6/latest/{base2_code}")
            result2.raise_for_status()
            data2 = result2.json()
            if target_code in data1['rates'] and target_code in data2['rates']:
                exchange_rate1 = data1['rates'][target_code]
                base1 = currencies[base1_code]
                target1 = currencies[target_code]
                exchange_rate2 = data2['rates'][target_code]
                base2 = currencies[base1_code]
                target2 = currencies[target_code]

                mb.showinfo('Курс обмена',
                            f'Курс '
                            f' {exchange_rate1:.1f} {target_code} за 1 {base1}'
                            f' {exchange_rate2:.1f} {target_code} за 1 {base2}')
            else:
                mb.showerror('Ошибка', f'Валюта {target_code} не найдена')


        except Exception as e:
            mb.showerror('Ошибка', f'error 400 {e}')

    if target_code and base1_code:
        try:
            result = requests.get(f"https://open.er-api.com/v6/latest/{base1_code}")
            result.raise_for_status()
            # data = json.loads(result.text)
            data = result.json()
            if target_code in data['rates']:
                exchange_rate = data['rates'][target_code]
                base = currencies[base1_code]
                target = currencies[target_code]

                mb.showinfo('Курс обмена',
                            f'Курс '
                            f' {exchange_rate:.1f} {target} за 1 {base}')
            else:
                mb.showerror('Ошибка', f'Валюта {target_code} не найдена')

        except Exception as e:
            mb.showerror('Ошибка', f'error 400 {e}')


# result = requests.get("https://open.er-api.com/v6/latest/USD")
# data = json.loads(result.text)
# # print(data)
# # print(type(data))
# # for item in data.items():
# #     print(item)
# p = pprint.PrettyPrinter(indent=4)
# p.pprint(data)
currencies = {
    "USD": "Доллар США",
    "EUR": "Евро",
    "CNY": "Юань",
    "RUB": "Российский рубль",
}

# pop_curr = ['EUR', 'USD', 'RUB', 'CNY']

root = Tk()
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
Xx = 300
Yy = 400
root.geometry(f"{Xx}x{Yy}+{WIDTH // 2 - Xx // 2}"
              f"+{HEIGHT // 2 - Yy // 2}")
# root.title("Курс валют по отношению к доллару США")
root.title("Курс обмена валют")
#root.geometry("300x400")

Label(text='Базовая валюта').pack(pady=10, padx=10)
base1_combobox = ttk.Combobox(values=list(currencies.keys()))
base1_combobox.pack()
currency_b1_label = ttk.Label()
currency_b1_label.pack(pady=10, padx=10)
base1_combobox.bind("<<ComboboxSelected>>", update_currency_b1_label)

Label(text='Вторая базовая валюта').pack(pady=10, padx=10)
base2_combobox = ttk.Combobox(values=list(currencies.keys()))
base2_combobox.pack()
currency_b2_label = ttk.Label()
currency_b2_label.pack(pady=10, padx=10)
base2_combobox.bind("<<ComboboxSelected>>", update_currency_b2_label)

Label(text='Целевая валюта').pack(pady=10, padx=10)
target_combobox = ttk.Combobox(values=list(currencies))
target_combobox.pack()

currency_t_label = ttk.Label()
currency_t_label.pack(pady=10, padx=10)
# entry = Entry(width=10)
# entry.pack()
button = Button(text='Получить курс', command=exchange)
button.pack()
target_combobox.bind("<<ComboboxSelected>>", update_currency_t_label)


root.mainloop()
