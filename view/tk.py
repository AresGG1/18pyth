import tkinter as tk
from tkinter import ttk


# class Grid(ttk.Treeview):


class App(tk.Tk):
  def __init__(self):
    super().__init__()

    self.title('My Awesome App')
    self.geometry('600x480')



main = App()
tabControl = ttk.Notebook(main)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tabs = (tab1, tab2, tab3)

count = 1
for tab in tabs:
    tabControl.add(tab, text=f"tab {count}")
    for c in range(4): tab.columnconfigure(index=c, weight=30)
    for r in range(4): tab.rowconfigure(index=r, weight=30)
    count += 1
    btn = ttk.Button(tab1)
    btn.pack()
tabControl.pack(expand=1, fill="both")



main.mainloop()