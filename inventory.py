import sqlite3
import datetime

#connect to database
db_con = sqlite3.connect("inventory.db")
#create a temporary memory to store data
conn = db_con.cursor()

def add_items():
    #create table
    conn.execute("CREATE TABLE IF NOT EXISTS inventory_items( \
                    id INTEGER PRIMARY KEY, name TEXT, \
                    description TEXT, quantity INTEGER, item_cost REAL, \
                    date_added NUMERIC, status NUMERIC ) ")
    
    #get user input
    print("Enter an Item")
    print("")
    #id = input("Enter ID: ")
    name = input("Enter item name: ")
    description = input("Enter desc: ")
    quantity = input("Enter Quantity: ")
    item_cost = input("Enter amount: ")
    #date_added = input("Enter date: ")
    status = input("Enter Status: ")
    #run sql command and commit data to db
    conn.execute("INSERT INTO inventory_items VALUES (null,?,?,?,?,DATETIME('now','localtime'),?);",\
                 (name, description, quantity, item_cost, status ))
    db_con.commit()
    
add_items()

















"""class InventoryManagement():
	def __init__(self, id, name, desc, quantity, cost_per_item, date_added, status):
		self.id = id
		self.name = name
		self.desc = desc
		self.quantity = quantity
		self.cost_per_item = cost_per_item
		self.date_added = date_added
		self.status = status

	#add items
	def item_details():
"""

