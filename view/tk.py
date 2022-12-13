import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from db.models.customer import Customer
from sqlalchemy.orm import Session
from db.models.order import Order
from db.models.product import Product
from db.db_connection import create_tables, engine


# class Grid(ttk.Treeview):


class App(tk.Tk):
  def __init__(self):
    super().__init__()

    self.title('My Awesome App')
    self.geometry('1000x640')



main = App()
create_tables(engine)
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


def table1GetData():
    for customer in gridCustomer.get_children():
        gridCustomer.delete(customer)
    with Session(autoflush=False, bind=engine) as db:
        items = db.query(Customer).all()
        for customer in items:
            gridCustomer.insert('', 0, values=(customer.customer_id, customer.name, customer.email, customer.age, customer.address))

table1GetData()

def table3GetData():
    for item in gridItem.get_children():
        gridItem.delete(item)
    with Session(autoflush=False, bind=engine) as db:
        products = db.query(Order).all()
        for product in products:
            gridItem.insert('', 0, values=(product.product_id, product.name, product.sku, product.price, product.category))
# table3GetData()

def table2GetData():
    for item in gridItem.get_children():
        gridItem.delete(item)
    with Session(autoflush=False, bind=engine) as db:
        products = db.query(Product).all()
        for product in products:
            gridItem.insert('', 0, values=(product.product_id, product.name, product.sku, product.price, product.category))
table2GetData()

def click11():
    name = entries[1][0].get()
    sku = entries[1][1].get()
    try:
        price = int(entries[1][2].get())
    except:
        price = 0
    category = entries[1][3].get()
    with Session(autoflush=False, bind=engine) as db:
        item = gridItem.focus()
        if item == '':
            messagebox.showinfo("Message", "Select user")
            return

        item = gridItem.item(item)
        item = db.query(Product).filter(Product.product_id == item['values'][0]).first()
        if name != "":
            item.name = name
        if sku != "":
            item.sku = sku
        if price != 0:
            item.price = price
        if category != "":
            item.category = category
        db.commit()

    table2GetData()


def click10():
    name = entries[1][0].get()
    sku = entries[1][1].get()
    try:
        price = int(entries[1][2].get())
    except:
        messagebox.showinfo("Message", "Wrong age")
        return
    category = entries[1][3].get()
    with Session(autoflush=False, bind=engine) as db:
        customer = Product()
        customer.name = name
        customer.sku = sku
        customer.price = price
        customer.category = category
        db.add(customer)
        db.commit()
    table2GetData()
def click12():
    with Session(autoflush=False, bind=engine) as db:
        cust = gridItem.focus()
        cust = gridItem.item(cust)
        customer = db.query(Product).get(cust['values'][0])
        db.delete(customer)
        db.commit()
    table2GetData()
def click13():
    name = entries[1][0].get()
    sku = entries[1][1].get()
    try:
        price = int(entries[1][2].get())
    except:
        price = 0
    address = entries[1][3].get()
    with Session(autoflush=False, bind=engine) as db:
        customers = db.query(Product)
        if name != "":
            customers = customers.filter(Product.name == name)
        if sku != "":
            customers = customers.filter(Product.sku == sku)
        if price != 0:
            customers = customers.filter(Product.price == price)
        if address != "":
            customers = customers.filter(Product.category == address)
        for item in gridItem.get_children():
            gridItem.delete(item)
        for customer in customers:
            gridItem.insert('', 0, values=(customer.product_id, customer.name, customer.sku, customer.price, customer.category))


def click01():
    name = entries[0][0].get()
    email = entries[0][1].get()
    try:
        age = int(entries[0][2].get())
    except:
        age = 0
    address = entries[0][3].get()
    with Session(autoflush=False, bind=engine) as db:
        cust = gridCustomer.focus()
        if cust == '':
            messagebox.showinfo("Message", "Select user")
            return

        cust = gridCustomer.item(cust)
        customer = db.query(Customer).filter(Customer.customer_id == cust['values'][0]).first()
        if name != "":
            customer.name = name
        if email != "":
            customer.email = email
        if age != 0:
            customer.age = age
        if address != "":
            customer.address = address
        db.commit()

    table1GetData()


def click00():
    name = entries[0][0].get()
    email = entries[0][1].get()
    try:
        age = int(entries[0][2].get())
    except:
        messagebox.showinfo("Message", "Wrong age")
        return
    address = entries[0][3].get()
    with Session(autoflush=False, bind=engine) as db:
        customer = Customer()
        customer.name = name
        customer.email = email
        customer.age = age
        customer.address = address
        db.add(customer)
        db.commit()
    table1GetData()
def click02():
    with Session(autoflush=False, bind=engine) as db:
        cust = gridCustomer.focus()
        cust = gridCustomer.item(cust)
        customer = db.query(Customer).get(cust['values'][0])
        db.delete(customer)
        db.commit()
    table1GetData()
def click03():
    name = entries[0][0].get()
    email = entries[0][1].get()
    try:
        age = int(entries[0][2].get())
    except:
        age = 0
    address = entries[0][3].get()
    with Session(autoflush=False, bind=engine) as db:
        customers = db.query(Customer)
        if name != "":
            customers = customers.filter(Customer.name == name)
        if email != "":
            customers = customers.filter(Customer.email == email)
        if age != 0:
            customers = customers.filter(Customer.age == age)
        if age != 0:
            customers = customers.filter(Customer.age == age)
        for item in gridCustomer.get_children():
            gridCustomer.delete(item)
        for customer in customers:
            gridCustomer.insert('', 0, values=(customer.customer_id, customer.name, customer.email, customer.age, customer.address))


func = [click00, click01, click02, click03,click10, click11, click12, click13, click10, click11, click12, click13]
func1 = []
# func2 = [click20, click21, click22, click23]


gridCustomer.pack()
gridItem.pack()
gridOrder.pack()

cl = 0
col = 0
for i in tabs:
    for btn in buttons:
        button = ttk.Button(i, text=btn, command=func[col])
        button.pack()
        buttons_list[cl].append(button)
        col += 1
    cl += 1

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
    entry.place(relx=0.07 + 0.15*count, rely=0.7)
    entries[2].append(entry)
    count += 1
tabControl.pack(expand=1, fill="both")


# buttons_list[0][0].


main.mainloop()