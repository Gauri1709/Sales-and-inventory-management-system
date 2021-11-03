
import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from main import *

tkWindow = Tk()

def dashboard():

    global dashboardPage
    dashboardpage = Toplevel(tkWindow)
    dashboardpage.title("Dashboard")
    dashboardpage.geometry("300x300")

    user_button = Button(register_page, text="User", width=10, height=1, bg="black", command=new_user)
    user_button.pack(side=LEFT)

    employee_button = Button(register_page, text="Employee", width=10, height=1, bg="black", command=new_user)
    employee_button.pack(side=RIGHT)

    product_button = Button(register_page, text="product", width=10, height=1, bg="black", command=new_user)
    product_button.pack(side=RIGHT)

    category_button = Button(register_page, text="category", width=10, height=1, bg="black", command=new_user)
    category_button.pack(side=LEFT)

    brands_button = Button(register_page, text="Brands", width=10, height=1, bg="black", command=new_user)
    brands_button.pack(side=BOTTOM)


def login():
    global login_page
    login_page = Toplevel(tkWindow)
    login_page.title("Login")
    login_page.geometry("300x250")
    bg = PhotoImage(file = "img.png")


    global login_username
    global login_password
    global login_username_enter
    global login_password_enter
    global userid
    userid = 1
    login_username = StringVar()
    login_password = StringVar()

    Label(login_page, text="Please detail if you already registerd").pack()
    Label(login_page, text="").pack()
    Label(login_page, text="Username:-").pack()
    login_username_enter = Entry(login_page, textvariable=login_username).pack()
    Label(login_page, text="Password:-").pack()
    login_password_enter = Entry(login_page, textvariable=login_password, show="*").pack()
    Label(login_page, text="").pack()
    Button(login_page, text="Login", width=10, height=1, bg="blue", command=exist_user).pack()



def register():
    global register_page
    register_page = Toplevel(tkWindow)
    register_page.title("Register")
    register_page.geometry("300x300")

    global userid
    global username
    global password
    global username_enter
    global password_enter
    global userid
    userid = IntVar()
    username = StringVar()
    password = StringVar()
    Label(register_page, text="Please enter User Details", bg="grey").pack()
    Label(register_page, text="").pack()
    Label(register_page, text="Userid:-").pack()
    username_enter = Entry(register_page, textvariable=userid).pack()
    Label(register_page, text="Username:-").pack()
    username_enter = Entry(register_page, textvariable=username).pack()
    Label(register_page, text="Password:-").pack()
    password_enter = Entry(register_page, textvariable=password, show="*").pack()
    Label(register_page, text="").pack()
    register_button = Button(register_page, text="Register", width=10, height=1, bg="black", command=new_user)
    register_button.pack()


def display_list():
    global display_list
    display_list = Toplevel(login_page)
    display_list.title("what you want")
    display_list.geometry("380x250")
    B1 = Button(display_list, text="Users", width=20, height=3, bg="blue", command= lambda m =None:display_users())
    B2 = Button(display_list, text="Brand", width=20, height=3, bg="cyan", command=lambda m =None:display_brand())
    B3 = Button(display_list, text="Category", width=20, height=3, bg="magenta",command=lambda m =None:display_category())
    B4 = Button(display_list, text="Products", width=20, height=3, bg="yellow",command=lambda m =None:display_products())
    B5 = Button(display_list, text="Order", width=20, height=3, bg="red",command=lambda m =None:display_order())
    B6 = Button(display_list, text="Department", width=20, height=3, bg="blue",command=lambda m =None:display_department())
    B7 = Button(display_list, text="SHOW INVENTORY", width=20, height=3, bg="grey",command=lambda m =None:display_department())

    B1.grid(row=1, column=0)
    B2.grid(row=1, column=1)
    B3.grid(row=2, column=0)
    B4.grid(row=2,column=1)
    B5.grid(row=3, column = 0)
    B6.grid(row=3,column=1)
    B7.place(relx=0.5, rely=0.905, anchor=CENTER)


def display_users():

    user = USER()
    users = user.display_users()
    global user_table
    global display_user
    display_user = Toplevel(display_list)
    display_user.title("Users")
    display_user.geometry("300x250")
    user_table = ttk.Treeview(display_user, column=("c1", "c2", "c3"), show='headings')

    for user in users:
        user_table.insert("", tk.END, values=user)
        # print("password: " + user[2])
    user_table.column("#1", anchor=tk.CENTER)
    user_table.heading("#1", text="userid")
    user_table.column("#2", anchor=tk.CENTER)
    user_table.heading("#2", text="username")
    user_table.column("#3", anchor=tk.CENTER)
    user_table.heading("#3", text="password")
    user_table.bind('<ButtonRelease-1>', selectUsr)
    user_table.grid()
    user_table.pack()


def display_employess():

    emp = Employee()
    employee = emp.display_employees()
    global emp_table
    global display_emp
    display_emp = Toplevel(display_list)
    display_emp.title("Employee")
    display_emp.geometry("300x250")
    emp_table = ttk.Treeview(display_emp, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7"), show='headings')

    for emp in employee:
        emp_table.insert("", tk.END, values=emp)
        # print("password: " + user[2])
    emp_table.column("#1", anchor=tk.CENTER)
    emp_table.heading("#1", text="emp_id")
    emp_table.column("#2", anchor=tk.CENTER)
    emp_table.heading("#2", text="First name")
    emp_table.column("#3", anchor=tk.CENTER)
    emp_table.heading("#3", text="Last name")
    emp_table.column("#4", anchor=tk.CENTER)
    emp_table.heading("#4", text="birth date")
    emp_table.column("#5", anchor=tk.CENTER)
    emp_table.heading("#5", text="salary")
    emp_table.column("#6", anchor=tk.CENTER)
    emp_table.heading("#6", text="dept_name")
    emp_table.column("#7", anchor=tk.CENTER)
    emp_table.heading("#7", text="dept_id")
    emp_table.bind('<ButtonRelease-1>', selectEmp)
    emp_table.grid()
    emp_table.pack()


def display_brand():
    brnd = Brand()
    brand = brnd.display_brands()
    global brand_table
    global display_brand
    display_brand = Toplevel(display_list)
    display_brand.title("Brand")
    display_brand.geometry("300x250")
    brand_table = ttk.Treeview(display_brand, column=("c1", "c2", "c3"), show='headings')

    for b in brand:
        brand_table.insert("", tk.END, values=b)
        # print("password: " + user[2])
    brand_table.column("#1", anchor=tk.CENTER)
    brand_table.heading("#1", text="brandid")
    brand_table.column("#2", anchor=tk.CENTER)
    brand_table.heading("#2", text="brand name")
    brand_table.column("#3", anchor=tk.CENTER)
    brand_table.heading("#3", text="brand status")
    brand_table.bind('<ButtonRelease-1>', selectBrand)
    brand_table.grid()
    brand_table.pack()


def display_category():
    cat = Category()
    category =cat.display_categorys()
    global category_table
    global display_category
    display_category = Toplevel(display_list)
    display_category.title("Category")
    display_category.geometry("300x250")
    category_table = ttk.Treeview(display_category, column=("c1", "c2", "c3"), show='headings')

    for c in category:
        category_table.insert("", tk.END, values=c)
    category_table.column("#1", anchor=tk.CENTER)
    category_table.heading("#1", text="categoryid")
    category_table.column("#2", anchor=tk.CENTER)
    category_table.heading("#2", text="category name")
    category_table.column("#3", anchor=tk.CENTER)
    category_table.heading("#3", text="category status")
    category_table.bind('<ButtonRelease-1>', selectCategory)
    category_table.grid()
    category_table.pack()


def display_products():
    prdt = Product()
    products = prdt.display_products()
    global product_table
    global display_product
    display_product = Toplevel(display_list)
    display_product.title("Employee")
    display_product.geometry("300x250")
    product_table = ttk.Treeview(display_product, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7"), show='headings')

    for p in products:
        product_table.insert("", tk.END, values=p)
    product_table.column("#1", anchor=tk.CENTER)
    product_table.heading("#1", text="Product_id")
    product_table.column("#2", anchor=tk.CENTER)
    product_table.heading("#2", text="Product name")
    product_table.column("#3", anchor=tk.CENTER)
    product_table.heading("#3", text="Quantity")
    product_table.column("#4", anchor=tk.CENTER)
    product_table.heading("#4", text="Rate")
    product_table.column("#5", anchor=tk.CENTER)
    product_table.heading("#5", text="user_id")
    product_table.column("#6", anchor=tk.CENTER)
    product_table.heading("#6", text="brand_id")
    product_table.column("#7", anchor=tk.CENTER)
    product_table.heading("#7", text="categoty_id")
    product_table.bind('<ButtonRelease-1>', selectProduct)
    product_table.grid()
    product_table.pack()

def display_orders():
    orde = Order()
    orders = orde.display_order()
    global order_table
    global display_order
    display_order = Toplevel(display_list)
    display_order.title("Employee")
    display_order.geometry("300x250")
    product_table = ttk.Treeview(display_product, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7"), show='headings')

    for o in orders:
        order_table.insert("", tk.END, values=o)
    order_table.column("#1", anchor=tk.CENTER)
    order_table.heading("#1", text="order_id")
    order_table.column("#2", anchor=tk.CENTER)
    order_table.heading("#2", text="client name")
    order_table.column("#3", anchor=tk.CENTER)
    order_table.heading("#3", text="No of items")
    order_table.column("#4", anchor=tk.CENTER)
    order_table.heading("#4", text="Total")
    order_table.column("#5", anchor=tk.CENTER)
    order_table.heading("#5", text="Payement status")
    order_table.column("#6", anchor=tk.CENTER)
    order_table.heading("#6", text="due")
    order_table.column("#7", anchor=tk.CENTER)
    order_table.heading("#7", text="paid")
    order_table.bind('<ButtonRelease-1>', selectProduct)
    order_table.grid()
    order_table.pack()

def display_department():
    dep = Department()
    dept =dep.display_department()
    global dept_table
    global display_dept
    display_dept = Toplevel(display_list)
    display_dept.title("department")
    display_dept.geometry("300x250")
    dept_table = ttk.Treeview(display_dept, column=("c1", "c2", "c3"), show='headings')

    for c in dept:
        dept_table.insert("", tk.END, values=c)
    dept_table.column("#1", anchor=tk.CENTER)
    dept_table.heading("#1", text="dept_id")
    dept_table.column("#2", anchor=tk.CENTER)
    dept_table.heading("#2", text="dept name")
    dept_table.column("#3", anchor=tk.CENTER)
    dept_table.heading("#3", text="manager id")
    dept_table.bind('<ButtonRelease-1>', selectdept)
    dept_table.grid()
    dept_table.pack()

def new_user():
    user = USER()
    userId = userid.get()
    userName = username.get()
    pwd = password.get()
    print(userName)
    print(pwd)
    user.insert_user(userId, userName, pwd)

def exist_user():
    user = login_username.get()
    pwd = login_password.get()
    print(user)
    print(pwd)
    Exist(connect(), user)


def Exist(mydb, user):
    mycursor = mydb.cursor()
    mycursor.execute('select* from users where username =\'' + user + '\';')
    users = mycursor.fetchall()
    if (len(users) > 0):
        display_list()

def selectUsr(a):
    curItem = user_table.focus()
    return user_table.item(curItem)
def selectEmp(a):
    curItem = emp_table.focus()
    return emp_table.item(curItem)
def selectBrand(a):
    curItem = brand_table.focus()
    return brand_table.item(curItem)
def selectCategory(a):
    curItem = category_table.focus()
    return category_table.item(curItem)
def selectProduct(a):
    curItem = product_table.focus()
    return product_table.item(curItem)
def selectdept(a):
    curItem = dept_table.focus()
    return dept_table.item(curItem)
def all_count():
    user = USER()
    users = user.count_user()
    emp = Employee()
    employee = emp.count_employee()
    cat = Category()
    category =cat.count_category()
    brnd = Brand()
    brand = brnd.count_brand()
    #dep = Department()
    #dept =dep.count_department()
    prdt = Product()
    products = prdt.count_product()
    print(users,employee,category,brand,products)


def main():
    all_count()
    tkWindow.geometry("300x250")
    tkWindow.title("Account Login")
    bg = PhotoImage(file = "img.png")
    label1 = Label(tkWindow,image = bg)
    label1.place(x = 0,y = 0)


    Button(text="Register", height="2", width="30", command=register).pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    tkWindow.mainloop()

if __name__ == "__main__":
    main()


