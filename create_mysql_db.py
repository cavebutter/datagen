import mysql.connector
from mysql.connector import Error
import csv

config = input("Use 'localhost', 'root', 'root'? (y/n) ")
if config == 'y':
    host = 'localhost'
    user = 'root'
    password = 'root'
else:
    host = input('host: ')
    user = input('user: ')
    password = input('password: ')
db_name = input('What is your database name? (Hint: the output directory name) ')
create_db = 'CREATE DATABASE ' + db_name

#  Create tables
manufacturers = '''CREATE TABLE IF NOT EXISTS `manufacturers`(
`manufacturerID` INT PRIMARY KEY,
`manufacturer` VARCHAR(30)
)'''
        
products = """CREATE TABLE IF NOT EXISTS products(
`category` VARCHAR(10),
`currency` VARCHAR(5),
`manufacturerID` INT,
`price` FLOAT,
`product` VARCHAR(20),
`productID` INT,
`segment` VARCHAR(20),
PRIMARY KEY (`productID`),
FOREIGN KEY (`manufacturerID`)
    REFERENCES manufacturers (`manufacturerID`)
)"""
        
customers = """CREATE TABLE IF NOT EXISTS customers(
`cust_id` INT,
`first_name` VARCHAR(30),
`last_name` VARCHAR(30),
`address` VARCHAR(200),
`city` VARCHAR(30),
`state` VARCHAR(3),
`zip` VARCHAR(9),
PRIMARY KEY (`cust_id`)
)"""

regions = """CREATE TABLE IF NOT EXISTS regions(
`state` VARCHAR(3),
`region` VARCHAR(30),
PRIMARY KEY (`state`, `region`)
)"""

sales_mgrs = """CREATE TABLE IF NOT EXISTS sales_mgrs(
`mgr_id` INT,
`first_name` VARCHAR(30),
`last_name` VARCHAR(30),
`region` VARCHAR(30),
PRIMARY KEY (`mgr_id`),
INDEX `mgr_region` (`region`)
)"""

sales_reps = """CREATE TABLE IF NOT EXISTS sales_reps(
`rep_id` INT,
`first_name` VARCHAR(30),
`last_name` VARCHAR(30),
`region` VARCHAR(30),
PRIMARY KEY (`rep_id`),
INDEX `rep_region` (`region`)
)"""

transactions = """CREATE TABLE IF NOT EXISTS transactions(
`tx_id` INT,
`cust_id` INT,
`rep_id` INT,
`prod_id` INT,
`price` FLOAT,
`qty` INT,
`cost` FLOAT,
`tx_date` DATETIME,
PRIMARY KEY (`tx_id`),
INDEX tx1 (`cust_id`),
INDEX tx2 (`rep_id`),
INDEX tx3 (`prod_id`)
)"""

table_list = [manufacturers, products, customers, regions, sales_mgrs, sales_reps, transactions]
mydb = mysql.connector.connect(host=host,user=user,password=password)

mycursor = mydb.cursor()

mycursor.execute('DROP DATABASE IF EXISTS ' + db_name)

mycursor.execute(create_db)

mycursor.execute('USE ' + db_name)

for table in table_list:
    mycursor.execute(table)

with open('output\\' + db_name + '\\customers.csv', 'r') as f:
    reader = csv.reader(f)
    customers = list(reader)
    customers.pop(0)

ins_customer = "INSERT INTO customers (cust_id, first_name, last_name, address, city, state, zip) VALUES (%s, %s, %s, %s, %s, %s, %s)"

mycursor.executemany(ins_customer, customers)
mydb.commit()

with open('output\\' + db_name + '\\manufacturers.csv', 'r') as f:
    reader = csv.reader(f)
    manufacturers = list(reader)
    manufacturers.pop(0)

ins_manufacturer = "INSERT INTO manufacturers (manufacturerID, manufacturer) VALUES (%s, %s)"

mycursor.executemany(ins_manufacturer, manufacturers)
mydb.commit()

with open('output\\' + db_name + '\\products.csv', 'r') as f:
    reader = csv.reader(f)
    products = list(reader)
    products.pop(0)

ins_products = "INSERT INTO products (category, currency, manufacturerID, price, product, productID, segment) VALUES (%s, %s, %s, %s, %s, %s, %s)"

mycursor.executemany(ins_products, products)
mydb.commit()

with open('output\\' + db_name + '\\regions.csv', 'r') as f:
    reader = csv.reader(f)
    regions = list(reader)
    regions.pop(0)
    regions.pop(0)

ins_regions = "INSERT INTO regions (state, region) VALUES (%s, %s)"

mycursor.executemany(ins_regions, regions)
mydb.commit()

with open('output\\' + db_name + '\\sales_mgrs.csv', 'r') as f:
    reader = csv.reader(f)
    sales_mgrs = list(reader)
    sales_mgrs.pop(0)

ins_mgr = "INSERT INTO sales_mgrs (mgr_id, first_name, last_name, region) VALUES (%s, %s, %s, %s)"

mycursor.executemany(ins_mgr, sales_mgrs)
mydb.commit()

with open('output\\' + db_name + '\\sales_reps.csv', 'r') as f:
    reader = csv.reader(f)
    sales_reps = list(reader)
    sales_reps.pop(0)

ins_rep = "INSERT INTO sales_reps (rep_id, first_name, last_name, region) VALUES (%s, %s, %s, %s)"

mycursor.executemany(ins_rep, sales_reps)
mydb.commit()

with open('output\\' + db_name + '\\transactions.csv', 'r') as f:
    reader = csv.reader(f)
    tx = list(reader)
    tx.pop(0)

ins_tx = "INSERT INTO transactions (tx_id, cust_id, rep_id, prod_id, price, qty, cost, tx_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

mycursor.executemany(ins_tx, tx)
mydb.commit()

mycursor.close()
mydb.close()