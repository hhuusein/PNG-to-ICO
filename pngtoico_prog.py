from PIL import Image
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("PNG to ICO")
root.iconbitmap("icon.ico")
root.geometry("230x110")
root.resizable(False, False)

png_path = ""
ico_path = ""

def png_select():
    global png_path
    png_path = filedialog.askopenfilename()

def ico_select():
    global ico_path
    ico_path = filedialog.asksaveasfilename(defaultextension=".ico")

def png_converter():
    png = Image.open(png_path)
    png.save(ico_path)

png_button_label = tk.Label(root, text="Dönüştürülecek Dosya:")
png_button_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

png_button = tk.Button(root, text="PNG File", command=png_select)
png_button.grid(row=0, column=1, padx=5, pady=5,)

ico_button_label =tk.Label(root, text="Kaydedilecek Yer")
ico_button_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

ico_button = tk.Button(root, text="ICO Path", command=ico_select)
ico_button.grid(row=1, column= 1,padx=5, pady=5)

conver_button = tk.Button(root, text="Dönüştür", command=png_converter)
conver_button.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

root.mainloop()