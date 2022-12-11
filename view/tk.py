import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from db.models.customer import Customer
from db.models.order import Order
from db.models.product import Product

from db.db_connection import Session


# class Grid(ttk.Treeview):


class App(tk.Tk):
  def __init__(self):
    super().__init__()

    self.title('My Awesome App')
    self.geometry('1000x640')



main = App()
tabControl = ttk.Notebook(main)
tabCustomer = ttk.Frame(tabControl)
tabItem = ttk.Frame(tabControl)
tabOrder = ttk.Frame(tabControl)
tabs = (tabCustomer, tabItem, tabOrder)

count = 1
for tab in tabs:
    tabControl.add(tab, text=f"tab {count}")
    for c in range(4): tab.columnconfigure(index=c, weight=30)
    for r in range(4): tab.rowconfigure(index=r, weight=30)
    count += 1
columnsCustomer = ('customer_id', 'name', 'email', 'age', 'address')
columnsItem = ('product_id', 'name', 'sku', 'price', 'category')
columnsOrder = ('order_id', 'created_at', 'quantity', 'customer_id', 'item_id')
gridCustomer = ttk.Treeview(tabCustomer, columns=columnsCustomer, show='headings')
gridItem = ttk.Treeview(tabItem, columns=columnsItem, show='headings')
gridOrder = ttk.Treeview(tabOrder, columns=columnsOrder, show='headings')
for column in columnsCustomer:
    gridCustomer.heading(column, text=column)
for column in columnsItem:
    gridItem.heading(column, text=column)
for column in columnsOrder:
    gridOrder.heading(column, text=column)

buttons = ('add', 'update', 'delete', 'search')

buttons_list = [[],[],[]]

col = 0

def click00():
    name = entries[0][0].get()
    email = entries[0][1].get()
    try:
        age = int(entries[0][2].get())
    except:
        messagebox.showinfo("Message", "Wrong age")
        return
    address = entries[0][3].get()
    with Session as db:
        customer = Customer()
        customer.name = name
        customer.email = email
        customer.age = age
        customer.address = address
        db.add(customer)
        db.commit()


func = [click00]


gridCustomer.pack()
gridItem.pack()
gridOrder.pack()
for i in tabs:
    for btn in buttons:
        button = ttk.Button(i, text=btn, command=func[0])
        button.pack()
        buttons_list[col].append(button)
    col += 1

count = 0
entries = [[],[],[]]
for i in columnsCustomer:
    if count == 0:
        count += 1
        continue
    entry = tk.Entry(tabCustomer)
    entry.place(relx=0.07 + 0.15*count, rely=0.7)
    entries[0].append(entry)
    count += 1

count = 0
for i in columnsItem:
    if count == 0:
        count += 1
        continue
    entry = tk.Entry(tabItem)
    entry.place(relx=0.07 + 0.15*count, rely=0.7)
    entries[1].append(entry)
    count += 1

count = 0
for i in columnsOrder:
    if count == 0:
        count += 1
        continue
    entry = tk.Entry(tabOrder)
    entry.place(relx=0.07 + 0.2*count, rely=0.7)
    entries[2].append(entry)
    count += 1
tabControl.pack(expand=1, fill="both")


# buttons_list[0][0].


main.mainloop()