Certainly! Here's a sample Python code for a user registration page for an AI chatbot using Flask web framework:

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Add code here to save the user registration data to a database
        
        return 'Registration successful for user: {}'.format(username)
    
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
```

You can create a simple HTML template named `register.html` in the same directory as your Python script to display the registration form. Here is an example of `register.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>User Registration</title>
</head>
<body>
    <h1>User Registration</h1>
    <form method="post">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br><br>
        
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br><br>
        
        <input type="submit" value="Register">
    </form>
</body>
</html>
```

You can run this Flask application and access the registration page at `http://localhost:5000/register`. Users can fill out the form and submit to register for the AI chatbot.