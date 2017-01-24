import sqlite3
import datetime
import csv

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

def items_list():
    #select all items from the database
    conn.execute("SELECT * FROM inventory_items")
    items = conn.fetchall()
    #display the items 
    return(items)

def export_data():
    #export data to an external file
    with open('exported_items.csv','w',newline = '') as fp:
        a = csv.writer(fp,delimiter = ',')
        a.writerows(items_list())
	print("Successfully exported items to 'exported_items.csv' file on the computer!")
        
def view_item():
    #view a single item from the database
    print("Enter the name of the item to view")
    print("")
    name = input("Enter item name: ")
    conn.execute("SELECT * FROM inventory_items WHERE name = ?",(name,))
    get_item = conn.fetchone()
    print(get_item)

def remove_item():
    #remove a single item from the database
    print("Enter the name of the item to Delete")
    print("")
    name = input("Enter name of item to delete: ")
    conn.execute("DELETE FROM inventory_items WHERE name = ?",(name,))
    db_con.commit()
    print("Successfully removed item from the database!")
















