import mysql.connector
import pandas as pd

DB_HOST = '34.101.194.111'
DB_USER = "dafafikra"
DB_PASSWORD = 'Dafafikra123'
DB_NAME = 'myfirstdb'

# Connect to the database
connection = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)

# Create a cursor to execute SQL queries
cursor = connection.cursor()

# Example SQL query
query1 = '''SELECT order_id, 
                  customer_id, 
                  product_id, 
                  quantity, 
                  order_date, 
                  status 
           FROM orders; '''

query2 = 'SELECT status, COUNT(*) FROM orders group by status'
query3 = 'SELECT * from users'
# Execute the query
cursor.execute(query3)

# insert_query = "INSERT INTO employees (first_name, last_name, department, salary) VALUES (%s, %s, %s, %s)"
# new_employee = ('Jane', 'Doe', 'Marketing', 60000)
# cursor.execute(insert_query, new_employee)


# Fetch and print the results
#for row in cursor.fetchall():
#    print(row)


# Fetch the results as a list of tuples
results = cursor.fetchall()
print(results)

# Get column names from cursor's description
columns = [column[0] for column in cursor.description]

# Create a DataFrame from the results
df = pd.DataFrame(results, columns=columns)

# Export the DataFrame to an Excel file
output_file = 'orders.xlsx'
df.to_excel(output_file, index=False)

# Close the cursor and connection
cursor.close()
connection.close()

print(f'Exported {len(df)} rows to {output_file}')
# This code retrieves the column names dynamically from the cursor's description, making it more flexible in case the column names change in the future.

# Close the cursor and connection
cursor.close()
connection.close()