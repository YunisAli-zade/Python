from tkinter import Tk
import tkinter as tk
import time

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

i = 0
j = 0
k = 0

def counter():
    global i
    i += 1
    label1.config(text=f"{i}")

def refresh():
    global i
    i = 0
    label1.config(text=f"{i}")


def factorial():
    global j
    memo = {}
    def fac(j):
        if j in memo:
            return memo[j]
        if j == 1:
            return 1
        if j == 0:
            return 1
        memo[j] = j * fac(j - 1)
        return memo[j]
    label2.config(text = f"Number: {j} \nFactorial: {fac(j)}")
    j += 1



def fibonachi():
    global k
    memo = {}
    def fib(k):
        if k in memo:
            return memo[k]
        if k == 0:
            return 0
        if k == 1:
            return 1
        memo[k] = fib(k - 1) + fib (k -2)
        return memo[k]
    label3.config(text = f"{k} = {fib(k)}")
    k += 1

root = Tk()
root.geometry('1280x1024')

button1 = tk.Button(root, text="Click!", command=counter, width=10, height=5)
label1 = tk.Label(root, text="0")
button1_1 = tk.Button(root, text="Refresh", command=refresh, width=10, height=5)
label2 = tk.Label(root, text = "")
button2 = tk.Button(root, text="factorial", command=factorial, width=10, height=5)
label3 = tk.Label(root, text = "")
button3 = tk.Button(root, text="Fibonachi", command=fibonachi, width=10, height=5)
center_window(root)

button1.grid(row=0, column=0, padx=10, pady=10)
label1.grid(row=0, column=1, padx=10, pady=10)
button1_1.grid(row=0, column=2, padx=10, pady=10)
label2.grid(row=0, column=4, padx=10, pady=10)
button2.grid(row=0, column=3, padx=10, pady=10)
label3.grid(row=1, column=1, padx=10, pady=10)
button3.grid(row=1, column=0, padx=10, pady=10)
root.mainloop()
