from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from googletrans import LANGUAGES
from textblob import TextBlob

root = Tk()
root.geometry("800x500")
root.title("LANGUAGE TRANSLATOR")

def translate():
    translated_text.delete(1.0, END)
    try:
        from_lang = language_key[original_combo.get()]
        to_lang = language_key[translate_combo.get()]
        
        words = TextBlob(original_text.get(1.0, END))
        translated_words = words.translate(from_lang=from_lang, to=to_lang)
        
        translated_text.insert(1.0, translated_words)
    except Exception as e:
        messagebox.showerror("Translator", e)

def clear():
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)

language = LANGUAGES
language_key = {value: key for key, value in language.items()}
language_list = list(language.values())


original_combo = Combobox(root, width=20, values=language_list)
original_combo.set("ENGLISH")
original_combo.grid(row=1, column=0, padx=10)

translate_combo = Combobox(root, width=20, values=language_list)
translate_combo.set("HINDI")
translate_combo.grid(row=1, column=1, padx=10)

original_text = Text(root, height=10, width=40)
original_text.grid(row=0, column=0, padx=10, pady=10)

translated_text = Text(root, height=10, width=40)
translated_text.grid(row=0, column=1, padx=10, pady=10)


translate_button = Button(root, text="Translate", font=("arial", 15), command=translate)
translate_button.grid(row=2, column=0, columnspan=2, pady=10)

clear_button = Button(root, text="Clear", command=clear)
clear_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()