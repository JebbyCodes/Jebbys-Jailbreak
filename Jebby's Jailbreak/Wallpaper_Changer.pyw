import tkinter as tk, base64
from tkinter import *


def command1():
    resolution = textbox.get("1.0", tk.END).lower().strip()   
    imagedirectory = textbox2.get("1.0", tk.END).strip()

    
    window.destroy()
    
    root = tk.Tk()
    root.title("Wallpaper bro")
    root.geometry(str(resolution))
    root.overrideredirect(True)

    bg = PhotoImage(file=str(imagedirectory))
    frame = Label(root, image=bg)
    frame.pack(fill=tk.BOTH, expand=True)

    def lower_window(event):
        root.lower()

    root.bind('<FocusIn>', lower_window)

    root.mainloop()


window=tk.Tk()
window.geometry("500x750")
window.title("Wallpaper.giggle")


label=tk.Label(window, text="Wallpaper Changer", font=("times new roman", 32))
label.pack(padx=50, pady=25)

label=tk.Label(window, text="", font=("times new roman", 16))
label.pack(padx=50, pady=25)

label=tk.Label(window, text="Screen resolution", font=("times new roman", 16))
label.pack(padx=50, pady=0)

textbox=tk.Text(window, height=1, font=("times new roman", 18))
textbox.pack(padx=50, pady=5)

label=tk.Label(window, text="", font=("times new roman", 16))
label.pack(padx=50, pady=25)

label=tk.Label(window, text="Image Directory", font=("times new roman", 16))
label.pack(padx=50, pady=0)

textbox2=tk.Text(window, height=1, font=("times new roman", 18))
textbox2.pack(padx=50, pady=5)


button=tk.Button(window, text="Apply", font=("times new roman", 18), command=command1)
button.pack(padx=5, pady=50)


window.mainloop()
