import pyodbc

# SQL Server ma'lumotlarini o'zgartiring
server = 'WIN-248HJOPPDI5\SQLEXPRESS'
database = 'SQL_tutorial'
trusted_connection = 'yes'

# Pyodbc orqali SQL Server ga bog'lanish uchun connection string
connection_string = f'Driver=SQL Server;Server={server};Database={database};Trusted_Connection={trusted_connection}'
cnxn = pyodbc.connect(connection_string)

cursor = cnxn.cursor()

# O'chirishni istagan jadva nomi
table_to_delete = 'sysdiagrams'

# O'chirish so'rovi
delete_query = f"DROP TABLE {table_to_delete}"

# O'chirish so'rovni bajarish
cursor.execute(delete_query)

# Tranzaksiyani tasdiqlash
cnxn.commit()

print(f"{table_to_delete} jadvasi o'chirildi.")

# Qolgan jadvallarni chiqarish
remaining_tables_query = "SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_TYPE = 'BASE TABLE'"

cursor.execute(remaining_tables_query)

# Barcha jadvallarni olish
remaining_tables = cursor.fetchall()

# Barcha jadvallarni chiqarish
print("Qolgan jadvallar:")
for table in remaining_tables:
    print(f"Jadva nomi: {table.TABLE_NAME}")

cnxn.close()
