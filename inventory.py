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
    conn.execute("INSERT INTO inventory_items VALUES (null, ? , ? , ? , ?, DATETIME('now','localtime'),0);",\
                 (name, description, quantity, item_cost))
    db_con.commit()
<<<<<<< HEAD
    print("Item has been added successfully\n")
    print("Add another item")+ add_items()
=======
>>>>>>> d22aeef6220dc5a9ece7c6802ffe9f7c696048ab

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
<<<<<<< HEAD
=======
	print("Successfully exported items to 'exported_items.csv' file on the computer!")
>>>>>>> d22aeef6220dc5a9ece7c6802ffe9f7c696048ab
        
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
    print("To Delete an item/n")
    
    del_by_id = set([1])
    del_by_name = set([2])
    
    item_to_del = int(input("Enter 1 to delete item by item id or 2 to delete by name: "))
    
    if item_to_del in del_by_id:
        get_item_id = input("Enter Item Id: ")
        conn.execute("SELECT * FROM inventory_items WHERE item_id = ?",(get_item_id,))
        get_del_1 = conn.fetchone()
        print(get_del_1)
        
        yes = set(['y','ye','yes',''])
        no = set(['no','n'])
        prompt_to_delete = input("Delete? Enter yes or no :")
        if prompt_to_delete in yes:
            conn.execute("DELETE FROM inventory_items WHERE item_id = ?",(get_item_id,))
            db_con.commit()
            print("Deleted Successfully")
        elif prompt_to_delete in no:
            print("thank you")
        else:
            print("invalid input")

def asset_value():
    #get the total value of assets(item_cost * quantity)
    #total for each item
    #get total sum
    #display items in a list
    conn.execute("SELECT item_id,name,SUM(item_cost*quantity) from inventory_items group by item_id")
    get_total = conn.fetchone()
    print(get_total)
def search_items():
    #search for a word in name and description columns
    search_item =input("Enter item to search ")
    conn.execute("SELECT item_id, name, description FROM inventory_items WHERE name LIKE '%"+search_item+"%'")
    items_found = conn.fetchall()
    print(items_found)
    #list in a table















