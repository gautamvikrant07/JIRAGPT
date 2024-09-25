Sure! Here is a sample Python code using Flask-Login to implement a basic authentication system for a web application:

```python
from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)

# User class for storing user information
class User(UserMixin):
    def __init__(self, id):
        self.id = id

# User database (in memory for demo purposes)
users = {'1': {'username': 'user1', 'password': 'password1'}}

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/')
def home():
    return 'Welcome to the home page!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        for user_id, user in users.items():
            if user['username'] == username and user['password'] == password:
                user_obj = User(user_id)
                login_user(user_obj)
                return redirect(url_for('home'))
        
        return 'Invalid username or password'
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
```

In this code snippet, we define a basic Flask application with routes for the home page, login, and logout. We use Flask-Login to handle user authentication. The User class represents a user object, and the users dictionary stores user information. The login route handles user login logic, and the logout route logs the user out. The `login.html` template can be created to render the login form.

Please note that this is a basic example and may need to be expanded for a production application, such as adding user registration, password hashing, and error handling.