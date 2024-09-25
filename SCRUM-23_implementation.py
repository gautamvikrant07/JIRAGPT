To create a Oracle database connection from a webpage using REST API in Python, you can use the `cx_Oracle` library for connecting to Oracle databases and the `requests` library for making REST API calls. Here's a sample code snippet that demonstrates how you can achieve this:

```python
import cx_Oracle
import requests
import json

# Define the Oracle database connection details
db_host = 'YOUR_DB_HOST'
db_port = 'YOUR_DB_PORT'
db_service = 'YOUR_DB_SERVICE'
db_user = 'YOUR_DB_USER'
db_password = 'YOUR_DB_PASSWORD'

# Define the REST API endpoint for fetching data
api_url = 'YOUR_REST_API_URL'

# Create a connection to the Oracle database
dsn = cx_Oracle.makedsn(db_host, db_port, service_name=db_service)
connection = cx_Oracle.connect(db_user, db_password, dsn)

# Create a cursor to execute SQL queries
cursor = connection.cursor()

# Sample SQL query to fetch data from the Oracle database
sql_query = 'SELECT * FROM YOUR_TABLE'

# Execute the SQL query
cursor.execute(sql_query)

# Fetch the results
results = cursor.fetchall()

# Close the cursor and connection
cursor.close()
connection.close()

# Make a REST API call to send the fetched data
response = requests.post(api_url, data=json.dumps(results))

# Print the response status code
print(response.status_code)
```

In this code snippet, you first establish a connection to the Oracle database using the `cx_Oracle` library. You then execute a sample SQL query to fetch data from the database. After fetching the data, you can use the `requests` library to make a POST request to the specified REST API endpoint with the fetched data in JSON format.

Make sure to replace `'YOUR_DB_HOST'`, `'YOUR_DB_PORT'`, `'YOUR_DB_SERVICE'`, `'YOUR_DB_USER'`, `'YOUR_DB_PASSWORD'`, `'YOUR_REST_API_URL'`, and `'YOUR_TABLE'` with your actual Oracle database connection details, REST API endpoint, and table name.

Please note that you may need to install the `cx_Oracle` and `requests` libraries if you haven't already. You can install them using `pip`:

```
pip install cx_Oracle requests
```