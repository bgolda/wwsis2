import mysql.connector
db_connection = mysql.connector.connect(
	host= "localhost",
	user= "root",
	passwd= ""
	)

db_cursor = db_connection.cursor()

decision = input('What would you like to do? (create_db, create_tbl, get_data, delete_tbl, alter_tbl, drop_tbl, drop_db): ')

if decision == 'create_db':
	db_name = input('Please provide new Database name: ')
	db_cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name};")
	db_cursor.execute("SHOW DATABASES;")

	for db in db_cursor:
		print(db)

elif decision == 'create_tbl':
	db_name = input('Please provide name of the Database where you would like to create a table: ')
	table_name = input('Please provide name of the Table that you would like to create: ')
	col_num = input('Please provide number of columns: ')
	db_cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (ID INT PRIMARY KEY);")
	for i in col_num:
		column_name = input('Please provide name of the column: ')
		column_type = input('Please provide column  data type: ')
		db_cursor.execute(f"ALTER TABLE {table_name} ADD {column_name} {column_type};")

elif decision == 'get_data':
	table_name = input('Please provide name of the table: ')
	is_sorted = input('Would you like your data to be sorted? (Y/N): ')
	if is_sorted == 'Y':
		db_cursor.execute(f'SHOW COLUMNS FROM {table_name};')
		column_name = input('Please select name of the column you want to order by: ')
		db_cursor.execute(f'SELECT * FROM {table_name} ORDER BY {column_name};')
	elif is_sorted == 'N':
		db_cursor.execute(f'SELECT * FROM {table_name};')

elif decision == 'delete_tbl':
	table_name = input('Please provide name of the table you would like to delete: ')
	db_cursor.execute(f'DELETE * FROM TABLE {table_name};')
	db_cursor.execute(f'SHOW TABLES;')

elif decision == 'alter_tbl':
	table_name = input('Please provide name of the table you would like to alter: ')
	alter_operation = input('Please provide alter operation you would like to perform (ADD, DROP, MODIFY): ')
	if alter_operation == 'ADD':
		column_name = input('Please provide name of the column to add: ')
		column_type = input('Please provide column data type: ')
		db_cursor.execute(f"ALTER TABLE {table_name} ADD {column_name} {column_type};")
	elif alter_operation == 'DROP':
		column_name = input('Please provide name of the column to drop: ')
		db_cursor.execute(f"ALTER TABLE {table_name} DROP COLUMN {column_name};")
	elif alter_operation == 'MODIFY':
		column_name = input('Please provide name of the column to modify: ')
		column_type = input('Please provide column data type: ')
		db_cursor.execute(f"ALTER TABLE {table_name} MODIFY COLUMN {column_name} {column_type};")

elif decision == 'drop_tbl':
	table_name = input('Please provide name of the table you would like to drop: ')
	db_cursor.execute(f"DROP TABLE {table_name};")

elif decision == 'drop_db':
	db_name = input('Please provide name of the Database you would like to drop: ')
	db_cursor.execute(f"DROP DATABASE IF EXISTS {db_name};")
	db_cursor.execute("SHOW DATABASES;")

else:
	print('Ooops, something went wrong :(')
