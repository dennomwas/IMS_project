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
    #show the item in a table
    #if not there, give feedback
    # ask if to try again
    print("Enter the name of the item to view\n")
    item_to_view = input("Enter item ID: ")
    conn.execute("SELECT * FROM inventory_items WHERE item_id = ?",(item_to_view,))
    get_item = conn.fetchone()
    x = str(get_item)
    if item_to_view not in x:
        print("Item is not in the database")
        
        print("View another item? 'YES' to continue 'NO' to quit")
        yes = set(['y','ye','yes',''])
        no = set(['no','n'])
        
        view_again = input(": ")
        if view_again in yes:
            view_item()
        elif view_again in no:
            print("Thank you")
        else:
            print("invalid input")
    else:
        print(get_item)

def remove_item():
    #remove an item from the database
    print("To Delete an item/n")
    get_item_id = input("Enter Item Id: ")
    conn.execute("SELECT * FROM inventory_items WHERE item_id = ?",(get_item_id,))
    get_del_1 = conn.fetchone()
    x=str(get_del_1)
    if get_item_id not in x:
        print("item not found")
        print("Do you want to search again? yes to continue no to quit")
        
        yes = set(['y','ye','yes',''])
        no = set(['no','n'])
        
        search_again = input(": ")
        if search_again in yes:
            remove_item()
        elif search_again in no:
            print("Thank you")
        else:
            print("invalid input")
    else:
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
    print("SEARCH FOR AN ITEM")
    print("--------------------\n")
    search_item =input("Enter item name to search: ")
    conn.execute("SELECT item_id, name, description FROM inventory_items WHERE name LIKE '%"+search_item+"%'")
    items_found = conn.fetchall()
    x = str(items_found)
    if search_item not in x:
        print("Item is not in the database")
        
        yes = set(['y','ye','yes',''])
        no = set(['no','n'])
        search_again = input("Search another item? 'YES' to continue 'NO' to quit: ")
        if search_again in yes:
            search_items()
        elif search_again in no:
            print("Thank you for your time!")
        else:
            print("invalid input, please enter y/n")
    else:
        print("ITEMS FOUND:")
        print("-------------")
        print(items_found)  















