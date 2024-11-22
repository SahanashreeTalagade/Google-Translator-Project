from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES
from PIL import Image, ImageTk

root = Tk()
root.title("Google Translator")
root.geometry("1080x400")
root.configure(bg="white")

# Icon
image_icon = PhotoImage(file="google.png")
root.iconphoto(False, image_icon)

# Languages
languages = LANGUAGES
languageV = list(languages.values())

# Function to translate text
def translate_text():
    text = text_input.get(1.0, END)
    source_lang = combo1.get().lower()
    target_lang = combo2.get().lower()
    if text.strip():
        try:
            print("Translating from:", source_lang, "to", target_lang)  # Debug line
            print("Original text:", text.strip())  # Debug line
            translator = Translator()
            translated = translator.translate(text.strip(), src=source_lang, dest=target_lang)
            print("Translated text:", translated.text)  # Debug line
            text_output.delete(1.0, END)
            text_output.insert(END, translated.text)
        except Exception as e:
            messagebox.showerror("Translator", str(e))
            print("Error:", e)  # Debug line
    else:
        messagebox.showerror("Translator", "Please enter text to translate")

combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="readonly")
combo1.place(x=110, y=20)
combo1.set("english")

combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="readonly")
combo2.place(x=730, y=20)
combo2.set("spanish")

text_input = Text(root, font="Roboto 14", height=10, wrap=WORD, padx=5, pady=5, width=50)
text_input.place(x=10, y=60)

translate_button = Button(root, text="Translate", font="Roboto 14", command=translate_text, bg="blue", fg="white")
translate_button.place(x=460, y=200)

text_output = Text(root, font="Roboto 14", height=10, wrap=WORD, padx=5, pady=5, width=50)
text_output.place(x=600, y=60)

root.mainloop()
