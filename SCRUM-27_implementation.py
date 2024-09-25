Sure! Here is a sample Python code that demonstrates how to implement a basic authentication system using Flask-Login:

```python
from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

login_manager = LoginManager()
login_manager.init_app(app)

# Mock user database
users = {'user1': {'password': 'password1'}, 'user2': {'password': 'password2'}}

class User(UserMixin):
    pass

@login_manager.user_loader
def load_user(user_id):
    user = User()
    user.id = user_id
    return user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        if username in users and request.form['password'] == users[username]['password']:
            user = User()
            user.id = username
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    return 'You are logged in as: ' + UserMixin.get_id()

if __name__ == '__main__':
    app.run(debug=True)
```

In this code snippet, we define a basic Flask application with routes for login, logout, and index pages. We use Flask-Login to manage user authentication and session management. The `users` dictionary serves as a mock user database for demonstration purposes. The `User` class extends `UserMixin` to represent a user object. The `login` route handles user login, while the `logout` route logs out the current user. The `index` route is a protected route that requires authentication to access.