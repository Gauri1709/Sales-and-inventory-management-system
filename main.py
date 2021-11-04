import mysql.connector

#global variables
host = "localhost"
user = "root"
password = "Vrathod07@"
port = 3306
database = "inventory"

def connect():
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        port=port,
        database=database
    )
    return mydb


class USER:

    def display_users(self):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM users')
        users = mycursor.fetchall()
        for user in users:
            print(f"username: {user[0]}, userid: {user[1]}")
        mycursor.close()
        mydb.close()
        return users

    def insert_user(self, userid, username, password):
        mydb = connect()
        mycursor = mydb.cursor()
        sql = "INSERT INTO users (user_id, username, password) VALUES (%s, %s, %s)"
        val = (userid, username, password)
        mycursor.execute(sql, val)
        print("Succesfully added user")
        mydb.commit()
        mycursor.close()
        mydb.close()

    def remove_user(self, userid):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('DELETE FROM users  WHERE user_id = %s;' % (userid))
        print("Succesfully deleted user")
        mydb.commit()
        mycursor.close()
        mydb.close()

    def count_user(self):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('SELECT count(user_id) FROM users;')
        count = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        return count

    # def search_user(mydb, username):
    #      pass


class Employee:

    def display_employees(self):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM employee')
        employees = mycursor.fetchall()
        for employee in employees:
            print(f"Id: {employee[0]} Name: {employee[1]} {employee[2]} Salary {employee[4]}")
        mycursor.close()
        mydb.close()
        return employees

    def insert_employee(self, emp_id, first_name, last_name, birth_date, salary, dept_id):
        mydb = connect()
        mycursor = mydb.cursor()
        sql = "INSERT INTO employee (emp_id, first_name, last_name, birth_date, salary, dept_id) VALUES (%s, %s, %s,%s, %s, %s)"
        val = (emp_id, first_name, last_name, birth_date, salary, dept_id)
        mycursor.execute(sql, val)
        print("Succesfully added employee")
        mydb.commit()
        mycursor.close()
        mydb.close()

    def remove_employee(self, emp_id):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('DELETE FROM employee  WHERE emp_id = %s;' % (emp_id))
        print("Succesfully deleted employee")
        mydb.commit()
        mycursor.close()
        mydb.close()

    def count_employee(self):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('SELECT count(emp_id) FROM employee;')
        count = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        return count


class Department:

    def display_department(self):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM department')
        departments = mycursor.fetchall()
        for department in departments: #     dept_id, dept_name, manager_id
            print(f"Dept_ID {department[0]} DeptName: {department[1]} Manager_ID: {department[2]}")
        mycursor.close()
        mydb.close()
        return departments


class Product:

    def display_products(self):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM product')
        products = mycursor.fetchall()
        for product in products: #  product_id, product_name, quantity, rate
            print(f"Id: {product[0]} Name: {product[1]} Quantity: {product[2]} Rate: {product[3]}")
        mycursor.close()
        mydb.close()
        return products

    def insert_product(self, product_id, product_name, quantity, rate, category_id, brand_id): #product_id, product_name, quantity, rate, category_id, brand_id
        mydb = connect()
        mycursor = mydb.cursor()
        sql = "INSERT INTO product (product_id, product_name, quantity, rate, category_id, brand_id) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (product_id, product_name, quantity, rate,category_id, brand_id)
        mycursor.execute(sql, val)
        print("Succesfully added product")
        mydb.commit()
        mycursor.close()
        mydb.close()

    def remove_product(self, product_id):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('DELETE FROM product  WHERE product_id = %s;' % (product_id))
        print("Succesfully deleted product")
        mydb.commit()
        mycursor.close()
        mydb.close()

    def count_product(self):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('SELECT count(product_id) FROM product;')
        count = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        return count


class Category:

    def display_categorys(self):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM category')
        categorys = mycursor.fetchall()
        for category in categorys: #     category_id, category_name, category_active
            print(f"Id: {category[0]} Name: {category[1]} Active: {category[2]}")
        mycursor.close()
        mydb.close()
        return categorys

    def insert_category(self, category_id, category_name, category_active):
        mydb = connect()
        mycursor = mydb.cursor()
        sql = "INSERT INTO category (category_id, category_name, category_active) VALUES (%s, %s, %s)"
        val = (category_id, category_name, category_active)
        mycursor.execute(sql, val)
        print("Succesfully added category")
        mydb.commit()
        mycursor.close()
        mydb.close()

    def remove_category(self, category_id):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('DELETE FROM category  WHERE category_id = %s;' % (category_id))
        print("Succesfully deleted category")
        mydb.commit()
        mycursor.close()
        mydb.close()

    def count_category(self):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('SELECT count(category_id) FROM category;')
        count = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        return count


class Brand:
    def display_brands(self):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM brands')
        brands = mycursor.fetchall()
        for brand in brands: #branch_id, brand_name, brand_active
            print(f"Id: {brand[0]} Name: {brand[1]} Active: #{brand[2]}")
        mycursor.close()
        mydb.close()
        return brands

    def insert_brands(self, branch_id, brand_name, brand_active,category_id):
        mydb = connect()
        mycursor = mydb.cursor()
        sql = "INSERT INTO brands (branch_id, brand_name, brand_active,category_id) VALUES (%s, %s, %s, %s)"
        val = (branch_id, brand_name, brand_active,category_id)
        mycursor.execute(sql, val)
        print("Succesfully added brand")
        mydb.commit()
        mycursor.close()
        mydb.close()

    def remove_brands(self, branch_id):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('DELETE FROM brands WHERE branch_id = %s;' % (branch_id))
        print("Succesfully deleted brand")
        mydb.commit()
        mycursor.close()
        mydb.close()

    def count_brand(self):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('SELECT count(branch_id) FROM brands;')
        count = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        return count


class Orders:

    def display_order(self): #order_id, client_name, no_of_items, payment_status, due, paid, total, product_id, category_id, user_id
      mydb = connect()
      mycursor = mydb.cursor()
      mycursor.execute('SELECT * FROM orders')
      orders= mycursor.fetchall()
      for order in orders:
          print(f"Id: {orders[0]} Name: {order[1]} Total: {order[7]}")
      mycursor.close()
      mydb.close()

    def insert_brands(self,order_id, client_name, no_of_items, payment_status, due, paid, total, product_id, category_id, user_id):
      mydb = connect()
      mycursor = mydb.cursor()
      sql = "INSERT INTO brands (order_id, client_name, client_contact, no_of_items, payment_status, due, paid, total, product_id, category_id, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %S, %s, %s, %s)"
      val = (order_id, client_name, no_of_items, payment_status, due, paid, total, product_id, category_id, user_id)
      mycursor.execute(sql, val)
      print("Succesfully added order")
      mydb.commit()
      mycursor.close()
      mydb.close()

    def remove_brands(self, order_id):
      mydb = connect()
      mycursor = mydb.cursor()
      mycursor.execute('DELETE FROM brands WHERE order_id = %s;' % (order_id))
      print("Succesfully deleted order")
      mydb.commit()
      mycursor.close()
      mydb.close()


def main():
   prdt = Product()
   prdt.insert_product(2346,"brush",23,3465.7,5698,4444)

if __name__ == "__main__":
    main()

