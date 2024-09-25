To create an Oracle database connection using REST API in Python, you can use the `requests` library to make HTTP requests to the Oracle REST Data Services (ORDS) endpoint. Here's a sample Python code that demonstrates how to achieve this:

```python
import requests

# Define the Oracle REST Data Services (ORDS) endpoint URL
ords_url = "http://your-ords-endpoint-url"

# Define the Oracle database credentials
db_username = "your-db-username"
db_password = "your-db-password"

# Define the SQL query to execute
sql_query = "SELECT * FROM your_table"

# Define the headers for the HTTP request
headers = {
    "Content-Type": "application/json"
}

# Define the data payload for the HTTP request (if needed)
payload = {
    "username": db_username,
    "password": db_password,
    "sql": sql_query
}

# Make a POST request to the ORDS endpoint to execute the SQL query
response = requests.post(ords_url, headers=headers, json=payload)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Failed to execute SQL query. Status code:", response.status_code)
```

Please make sure to replace the placeholder values with your actual ORDS endpoint URL, database credentials, and SQL query. Additionally, you may need to adjust the code based on the specific requirements and authentication mechanisms of your Oracle database and REST API.