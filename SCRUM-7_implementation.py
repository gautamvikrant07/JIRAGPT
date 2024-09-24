Sure! Here is a sample Python code for creating a login page for an AI chatbot using Flask framework:

```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Check if the username and password are correct
    if username == 'admin' and password == 'password':
        return redirect(url_for('chatbot'))
    else:
        return "Invalid username or password"

@app.route('/chatbot')
def chatbot():
    return "Welcome to the AI chatbot!"

if __name__ == '__main__':
    app.run(debug=True)
```

In this code, we have defined two routes: `/` for the login page and `/login` for handling the login form submission. The `login()` function checks if the username and password are correct and redirects to the chatbot page if they are. Otherwise, it displays an error message.

You can create a `login.html` file in the `templates` folder of your Flask project to design the login form.