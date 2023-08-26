import tkinter
from tkinter import *

conversion_rates = {"USD": 1,
        "AED": 3.67,
        "AFN": 84.82,
        "ALL": 94.18,
        "AMD": 386.58,
        "ANG": 1.79,
        "AOA": 831.97,
        "ARS": 284.21,
        "AUD": 1.53,
        "AWG": 1.79,
        "AZN": 1.7,
        "BAM": 1.78,
        "BBD": 2,
        "BDT": 109.47,
        "BGN": 1.78,
        "BHD": 0.376,
        "BIF": 2831.86,
        "BMD": 1,
        "BND": 1.35,
        "BOB": 6.92,
        "BRL": 4.9,
        "BSD": 1,
        "BTN": 82.89,
        "BWP": 13.52,
        "BYN": 2.95,
        "BZD": 2,
        "CAD": 1.34,
        "CDF": 2436.6,
        "CHF": 0.877,
        "CLP": 862.15,
        "CNY": 7.22,
        "COP": 4088.64,
        "CRC": 538.91,
        "CUP": 24,
        "CVE": 100.51,
        "CZK": 22.12,
        "DJF": 177.72,
        "DKK": 6.8,
        "DOP": 56.54,
        "DZD": 135.94,
        "EGP": 30.91,
        "ERN": 15,
        "ETB": 55.24,
        "EUR": 0.912,
        "FJD": 2.23,
        "FKP": 0.786,
        "FOK": 6.8,
        "GBP": 0.786,
        "GEL": 2.61,
        "GGP": 0.786,
        "GHS": 11.2,
        "GIP": 0.786,
        "GMD": 62.89,
        "GNF": 8583.32,
        "GTQ": 7.87,
        "GYD": 209.54,
        "HKD": 7.82,
        "HNL": 24.6,
        "HRK": 6.87,
        "HTG": 136.72,
        "HUF": 354.02,
        "IDR": 15229.99,
        "ILS": 3.7,
        "IMP": 0.786,
        "INR": 82.89,
        "IQD": 1320.67,
        "IRR": 41950.23,
        "ISK": 131.76,
        "JEP": 0.786,
        "JMD": 154.49,
        "JOD": 0.709,
        "JPY": 143.54,
        "KES": 143.49,
        "KGS": 87.9,
        "KHR": 4143.85,
        "KID": 1.53,
        "KMF": 448.45,
        "KRW": 1314.62,
        "KWD": 0.308,
        "KYD": 0.833,
        "KZT": 445.95,
        "LAK": 19350.48,
        "LBP": 15000,
        "LKR": 319.65,
        "LRD": 186.57,
        "LSL": 18.97,
        "LYD": 4.8,
        "MAD": 9.77,
        "MDL": 17.7,
        "MGA": 4447.41,
        "MKD": 56.18,
        "MMK": 2101.76,
        "MNT": 3460.41,
        "MOP": 8.05,
        "MRU": 37.9,
        "MUR": 45.35,
        "MVR": 15.46,
        "MWK": 1086.49,
        "MXN": 17.08,
        "MYR": 4.57,
        "MZN": 63.94,
        "NAD": 18.97,
        "NGN": 763.08,
        "NIO": 36.61,
        "NOK": 10.22,
        "NPR": 132.63,
        "NZD": 1.65,
        "OMR": 0.384,
        "PAB": 1,
        "PEN": 3.71,
        "PGK": 3.58,
        "PHP": 56.33,
        "PKR": 287.91,
        "PLN": 4.07,
        "PYG": 7277.22,
        "QAR": 3.64,
        "RON": 4.51,
        "RSD": 106.8,
        "RUB": 97.05,
        "RWF": 1188.77,
        "SAR": 3.75,
        "SBD": 8.51,
        "SCR": 13.23,
        "SDG": 556.12,
        "SEK": 10.69,
        "SGD": 1.35,
        "SHP": 0.786,
        "SLE": 22.03,
        "SLL": 22028.36,
        "SOS": 569.82,
        "SRD": 38.15,
        "SSP": 1001.11,
        "STN": 22.33,
        "SYP": 13026.74,
        "SZL": 18.97,
        "THB": 35.03,
        "TJS": 10.94,
        "TMT": 3.5,
        "TND": 3.08,
        "TOP": 2.34,
        "TRY": 27.02,
        "TTD": 6.77,
        "TVD": 1.53,
        "TWD": 31.76,
        "TZS": 2497.3,
        "UAH": 36.83,
        "UGX": 3639.46,
        "UYU": 38.11,
        "UZS": 11681.51,
        "VES": 31.24,
        "VND": 23733.02,
        "VUV": 120.27,
        "WST": 2.75,
        "XAF": 597.93,
        "XCD": 2.7,
        "XDR": 0.747,
        "XOF": 597.93,
        "XPF": 108.78,
        "YER": 250.43,
        "ZAR": 18.97,
        "ZMW": 19.1,
        "ZWL": 4727.29
}

root =Tk()
root.title("Currency Converter")
root.geometry("600x400")
root.config(bg="#52595D")

def convert_currency():
    try:
        amount = float(entry_amount.get())
    except ValueError:
        label_result.config(text="Invalid input")
        return

    fromcurrency = combo_from.get()
    to_currency = combo_to.get()

    if fromcurrency in conversion_rates and to_currency in conversion_rates:
        converted_amount = amount * (conversion_rates[to_currency] / conversion_rates[fromcurrency])
        label_result.config(font=14,text=f"Converted: {converted_amount:.2f} {to_currency}")
    else:
        label_result.config(text="Invalid currency",font=14)

label_amount =Label(root, text="Enter amount:",font=14)
label_from =Label(root, text="From currency:",font=14)
label_to =Label(root, text="To currency:",font=14)
label_result =Label(root, text="Result:",font=14)

label_amount.grid(row=0, column=0, padx=30, pady=10)
label_from.grid(row=1, column=0, padx=30, pady=10)
label_to.grid(row=2, column=0, padx=30, pady=10)
label_result.grid(row=4, column=0, padx=30, pady=10, columnspan=2)

entry_amount =Entry(root)
entry_amount.grid(row=0, column=1, padx=30, pady=10)

currencies = list(conversion_rates.keys())
combo_from =StringVar()
combo_to =StringVar()

combo_from.set(currencies[0])
combo_to.set(currencies[1])

dropdown_from =OptionMenu(root, combo_from, *currencies)
dropdown_to =OptionMenu(root, combo_to, *currencies)

dropdown_from.grid(row=1, column=1, padx=30, pady=10)
dropdown_to.grid(row=2, column=1, padx=30, pady=10)

convert_button =Button(root, text="Convert",font=14, command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2, padx=70, pady=20)

# Run the GUI event loop
root.mainloop()