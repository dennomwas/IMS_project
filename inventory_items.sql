BEGIN TRANSACTION;
CREATE TABLE inventory_items(
			id INTEGER PRIMARY KEY AUTOINCREMENT, 
			name TEXT,
			description TEXT, 
			quantity INTEGER, 
			item_cost REAL, 
			date_added NUMERIC, 
			status NUMERIC 
);
COMMIT;
