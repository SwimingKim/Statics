import tkinter as tk
window = tk.Tk()
box = tk.Listbox(window, width=17, height=12, fg="black")
data = 0
box.grid(row=0, column=0)
box.insert(tk.END, data)

def monitor():
    global data

    print(data)

    data = data + 1
    # Update the listbox
    # 1. clear all
    box.delete(0, tk.END)
    # 2. insert new data
    box.insert(tk.END, data)
    window.after(1000, monitor)

window.after(10, monitor)
window.mainloop()