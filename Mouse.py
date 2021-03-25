import pyautogui
from tkinter import *
from time import sleep
import tkinter as tk

a = 0
x = ""

root = Tk()
root.wm_attributes("-topmost", 1)
root.title("Mouse") # title bar
root.configure(background="white")
root.geometry("320x90")
label = Label(root, text=x, font=("Arial Bold", 10))
label.configure(background="white")
label.place(x=10, y=10)
str_var = tk.StringVar(value="Default")


while a == 0:
    x = pyautogui.position()
    x = str(x)
    x = x.replace("Point"," ").replace("(","").replace(")"," ").replace(",","")
    label = Label(root, text=x, font=("Arial Bold", 20))
    label.configure(background="white")
    label.place(x=10, y=10)
    root.update()
    label.destroy()

root.mainloop()
