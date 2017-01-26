import sqlite3
import datetime
import csv
from tabulate import tabulate

#connect to database
db_con = sqlite3.connect("inventory.db")
#create a temporary memory to store data
conn = db_con.cursor()


def add_items():
    #create table
    conn.execute("CREATE TABLE IF NOT EXISTS inventory_items( \
                    id INTEGER PRIMARY KEY UNIQUE, name TEXT, \
                    description TEXT, quantity INTEGER, item_cost REAL, \
                    date_added NUMERIC, status NUMERIC ) ")

    #get user input
    print("Enter an Item\n")
    name = input("Enter item name     : ")
    description = input("Enter item description: ")
    quantity = input("Enter Quantity  : ")
    item_cost = input("Enter amount   : ")

    #run sql command and commit data to db
    conn.execute("INSERT INTO inventory_items VALUES (null, ? , ? , ? , ?, DATETIME('now','localtime'),'');",\
                 (name, description, quantity, item_cost))
    db_con.commit()

    print("Item has been added successfully\n")
    print("Add another item (y/n)")
    yes = set(['y','ye','yes',''])
    no = set(['no','n'])
    add_again = input(": ")
    if add_again in yes:
        add_items()
    elif add_again in no:
        print("Thank you, Perform another action or quit system")
    else:
        print("Invalid input, enter 'y/n'")


def items_list():
    #select all items from the database
    conn.execute("SELECT * FROM inventory_items")
    for items in conn.fetchall():
    #display the items 
        print([items])

def export_data():
    #export data to an external file
    with open('exported_items.csv','w',newline = '') as fp:
        a = csv.writer(fp,delimiter = ',')
        a.writerows(items_list())
	print("Successfully exported items to 'exported_items.csv' file on the computer!")

        
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
    get_total = conn.fetchall()
    print(get_total)
    print("Your total asset value is: ")
    conn.execute("SELECT SUM(item_cost*quantity) from inventory_items")
    get_sum = conn.fetchone()
    print(get_sum)

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


def inventory_console():
    while True:
        print tabulate(["INVENTORY MANAGEMENT SYSTEM"], tablefmt = 'rst')
        print tabulate([[1,'Add an Item'], [2, 'View an Item'], [3, 'Remove an Item'],\
                        [4, 'List all Items'], [5,'Export Items'], [6, 'Check Asset Value'],\
                        [0.,'Quit']], headers = ['','Select an Option'], tablefmt = 'psql') 
   
        input("Please select an option: ")
        x = int(x)
        if x == 0:
            #exit the system
            print tabulate([['Thank you for interacting with our system'],\
                ['We value your feedback: githinji.mwangi@gmail.'],\
                ['We Appreciate your support: MPESA No. 0723 042 098']], tablefmt = 'psql')
            break

add_items()










