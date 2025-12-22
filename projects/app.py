from tkinter import PhotoImage, Tk, Label, Button
def on_button_click():
    label.config(text="Button Clicked!")
root = Tk()
root.title("Simple Tkinter App")
label = Label(root, text="Hello, Tkinter!")
label.pack(pady=10)
button = Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)
root.geometry("1200x600")
root.resizable(False, False)
root.configure(bg="#D1EDF3",
                cursor="arrow",
                bd=5, relief="sunken", highlightthickness=2)
root.mainloop()