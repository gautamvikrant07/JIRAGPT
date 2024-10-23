Sure! Here is a sample Python code that creates a database connection with Oracle DB using the `cx_Oracle` library:

```python
import cx_Oracle

# Set up connection details
username = 'your_username'
password = 'your_password'
dsn = cx_Oracle.makedsn('hostname', 'port', service_name='service_name')

# Create a connection
connection = cx_Oracle.connect(username, password, dsn)

# Create a cursor
cursor = connection.cursor()

# Execute a sample query
cursor.execute('SELECT * FROM your_table')
for row in cursor:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()
```

Make sure to replace `your_username`, `your_password`, `hostname`, `port`, `service_name`, and `your_table` with your actual Oracle DB connection details. Also, you need to have the `cx_Oracle` library installed in order to run this code.