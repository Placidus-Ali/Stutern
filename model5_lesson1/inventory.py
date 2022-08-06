import sqlite3

#check
print("sqlite3 imported successfully")

conn = sqlite3.connect("inventory.db")

#check
print("connection created successfully")

#create a cursor object
cursor = conn.cursor()

#check
print("cursor object created successfully")

#create a table
# cursor.execute(
#     """
#     CREATE TABLE  stationery_info(
#         item_name text,
#         item_id integer,
#         cost_price integer,
#         quantity_in_stcok integer
#     )
#     """
# )
#check
print("Table created successfully")

# # create list of items
item_list =[ ('Stapler', '123', '2000', '20'), ('Eraser', '234', '200', '50'), 
            ('Paper Clip', '345', '300', '10'), ('Push Pin', '456', '500', '3'),
            ('Rubber Stamp', '567', '1000', '10'), ('Pen', '678', '200', '1'), 
            ('Pencil', '789', '100', '4'), ('Marker', '890', '150', '7'), 
            ('Sharpener', '901', '300', '30'), ('Calculator', '902', '4000', '5'), 
            ('Paper', '903', '1000', '2'), ('Envelope', '904', '50', '15'), 
            ('Notebook', '905', '250', '2')
]
#check 
print("List of items created")

# cursor.executemany(
#     """
#     INSERT INTO stationery_info
#     VALUES (?, ?, ?, ?)
#     """,
#     item_list
#     )

# conn.commit()


# # #check
# print("Items inserted successfully")


# #query data
cursor.execute(
    """
    SELECT * FROM stationery_info
    """
    )

items = cursor.fetchall()
print(item_list)

#querying the databsae using ORDER BY
item = cursor.execute(""" SELECT * FROM stationery_info
                ORDER BY cost_price DESC;
""")

for row in item:
    print(row)

# format output to display in a tabular form
print("Item Name"+ "\t Item ID"+ "\t Cost Price"+ "\t Quantity In Stock \n" f"{'.' * 100}" )

# Loop through the items
for item in items:
    item_name, item_id, cost_price, quantity_in_stock = item
    print(f"{item_name:12}{item_id:10}{cost_price:16}{quantity_in_stock:15}")
