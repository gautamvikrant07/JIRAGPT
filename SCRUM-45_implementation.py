Certainly! Here is a sample Python code that demonstrates how to create a database connection using Oracle using the `cx_Oracle` library:

```python
import cx_Oracle

# Establish a connection to the Oracle database
connection = cx_Oracle.connect('username', 'password', 'hostname:port/service_name')

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Execute a sample query to fetch data
cursor.execute("SELECT * FROM your_table")
rows = cursor.fetchall()

# Iterate over the result set and print each row
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()
```

Make sure to replace `'username'`, `'password'`, `'hostname:port/service_name'`, and `'your_table'` with the appropriate values specific to your Oracle database setup.