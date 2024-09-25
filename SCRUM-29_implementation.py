Sure! Here is a sample Python code that creates a connection to a SQLite database and displays the data on an HTML page using Flask:

```python
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('sample.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
```

Make sure you have a SQLite database file named `sample.db` with a `users` table in the same directory as your Python script. The `index.html` file should be in a `templates` folder in the same directory as your Python script.

Here is a simple `index.html` template to display the user data:

```html
<!DOCTYPE html>
<html>
<head>
    <title>User Data</title>
</head>
<body>
    <h1>User Data</h1>
    <ul>
        {% for user in users %}
            <li>{{ user }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

Remember to install Flask by running `pip install Flask` in your terminal before running the Python script.