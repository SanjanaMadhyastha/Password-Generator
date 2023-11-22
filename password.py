import random
import string
import tkinter as tk


def generate_password():
    length = int(length_entry.get())
    if length < 1:
        password_result.set("Invalid length!")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_result.set(password)



window = tk.Tk()
window.title("Password Generator")


length_label = tk.Label(window, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()


generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()


password_result = tk.StringVar()
password_label = tk.Label(window, textvariable=password_result)
password_label.pack()


window.mainloop()
