Sure! Here is a sample Python code that fulfills the user story:

```python
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite database
conn = sqlite3.connect('your_database.db')

# Query data for the monthly report
query = "SELECT * FROM your_table WHERE date BETWEEN '2022-01-01' AND '2022-01-31'"
df = pd.read_sql(query, conn)

# Create charts using matplotlib
plt.figure(figsize=(10, 6))
plt.bar(df['date'], df['sales'], color='skyblue')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Monthly Sales Report - January 2022')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the chart as an image
plt.savefig('monthly_sales_report_january_2022.png')

# Show the chart
plt.show()

# Close the database connection
conn.close()
```

Make sure to replace `'your_database.db'`, `'your_table'`, `'date'`, and `'sales'` with your actual database file, table name, date column, and sales column respectively. You can customize the query to fetch the data you need for the monthly report.