#import database 
import sqlite3
#library for system-specific parameters and functions
import sys
#library for time and date parameters
import datetime
#library to get comma separated values for external export
import csv
#library to style data in tables
from prettytable import PrettyTable

#connect to database
db_connect = sqlite3.connect("inventory.db")
#create a temporary memory to store data
connect = db_connect.cursor()


def add_items():
    #create table in the database
    connect.execute("CREATE TABLE IF NOT EXISTS inventory_items( \
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
    connect.execute("INSERT INTO inventory_items VALUES (null, ? , ? , ? , ?, DATETIME('now','localtime'),'');",\
                 (name, description, quantity, item_cost))
    db_connect.commit()

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
        print("invalid input, please enter y/n")


def items_list():
    #select all items from the database
    connect.execute("SELECT * FROM inventory_items")
    for items in connect.fetchall():
            print([items])
        #display the items
        #print(items) 
        #print tabulate([items], headers = ['id','name','description','quantity','item_cost','date_added','status'], tablefmt = 'psql')

def export_data():
    #export data to an external file
    with open('exported_items.csv','w',newline = '') as csvfile:
        a = csv.writer(csvfile,delimiter = ',')
        connect.execute("SELECT * FROM inventory_items")
        data_to_export = connect.fetchall()
        a.writerows(data_to_export) 
            #print("Successfully exported items to 'exported_items.csv' file on the computer!")
        #else:
            #print("Not exported")

        
def view_item():
    #view a single item from the database
    #show the item in a table
    #if not there, give feedback
    # ask if to try again
    print("Enter the name of the item to view\n")
    item_to_view = input("Enter item ID: ")
    connect.execute("SELECT * FROM inventory_items WHERE item_id = ?",(item_to_view,))
    get_item = [connect.fetchone()]
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
            print("Thank you, Perform another action or quit system")
        else:
            print("invalid input, please enter y/n")
    else:
        table
        print([get_item])

def remove_item():
    #remove an item from the database
    print("To Delete an item/n")
    get_item_id = input("Enter Item Id: ")
    connect.execute("SELECT * FROM inventory_items WHERE item_id = ?",(get_item_id,))
    get_item_to_remove = connect.fetchone()
    x=str(get_item_to_remove)
    if get_item_id not in x:
        print("item not found")
        print("Do you want to search again? yes to continue no to quit")
        
        yes = set(['y','ye','yes',''])
        no = set(['no','n'])
        
        search_again = input(": ")
        if search_again in yes:
            remove_item()
        elif search_again in no:
            print("Thank you, Perform another action or quit system")
        else:
            print("invalid input, please enter y/n")
    else:
        print(get_item_to_remove)
        yes = set(['y','ye','yes',''])
        no = set(['no','n'])
        prompt_to_delete = input("Delete? Enter yes or no :")
        if prompt_to_delete in yes:
            connect.execute("DELETE FROM inventory_items WHERE item_id = ?",(get_item_id,))
            db_connect.commit()
            print("Deleted Successfully")
        elif prompt_to_delete in no:
            print("Thank you, Perform another action or quit system")
        else:
            print("invalid input, please enter y/n")

def asset_value():
    #get the total value of assets(item_cost * quantity)
    #total for each item
    #get total sum
    #display items in a list
    print("ASSET VALUE PER ITEM")
    print("______________________\n")
    connect.execute("SELECT item_id,name,SUM(item_cost*quantity) from inventory_items group by item_id")
    get_total = connect.fetchall()
    print(get_total)
    print("TOTAL ASSET VALUE: ")
    print("____________________\n")
    connect.execute("SELECT SUM(item_cost*quantity) from inventory_items")
    get_sum = connect.fetchone()
    print(get_sum)

def search_items():
    #search for a word in name and description columns
    print("SEARCH FOR AN ITEM")
    print("--------------------")
    search_item =input("Enter item name to search: ")
    connect.execute("SELECT item_id, name, description FROM inventory_items WHERE name LIKE '%"+search_item+"%'")
    items_found = connect.fetchall()
    x = str(items_found)
    if search_item not in x:
        print("Item is not in the database")
        
        yes = set(['y','ye','yes',''])
        no = set(['no','n'])
        search_again = input("Search another item? 'YES' to continue 'NO' to quit: ")
        if search_again in yes:
            search_items()
        elif search_again in no:
            print("Thank you, Perform another action or quit system")
        else:
            print("invalid input, please enter y/n")
    else:
        print("ITEMS FOUND:")
        print("-------------")
        print(items_found) 
        print("") 


def inventory_console():
    while True:

        console = PrettyTable(['','SELECT AN OPTION'])
        console.add_row(['1','Add an Item'])
        console.add_row(['2','View an Item'])
        console.add_row(['3','Remove an Item'])
        console.add_row(['4','List all Items'])
        console.add_row(['5','Export Items'])
        console.add_row(['6','Search Items'])
        console.add_row(['7','Check Asset Value'])
        console.add_row(['0','QUIT'])
        print(console)

        x =input("Please select an option: ")
        x = int(x)
        if x == 0:
            #exit the system
            console = PrettyTable(['THANK YOU!'])
            console.add_row(['We value your feedback: githinji.mwangi@gmail.com\n'])
            console.add_row(['We Appreciate your support: MPESA No. 0723 042 098\n'])
            print(console)
            break
        elif x == 1:
            #call function to add items
            add_items()
        elif x == 2:
            #call function to list all items
            view_item()
        elif x == 3:
            #call function to export items
            remove_item()
        elif x == 4:
            #view a single item
            items_list()
        elif x == 5:
            #remove an item
            export_data()
        elif x == 6:
            #check asset value
            search_items()
        elif x == 7:
            #check asset value
            asset_value()
        else:
            print("Invalid input, Enter No. between 0 - 9")





"""
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
"""
#export_data()
#items_list()
inventory_console()









