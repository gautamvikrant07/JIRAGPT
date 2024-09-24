Certainly! Here is an example of a simple Python Flask application that serves a basic webpage for a chatbot:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('chatbot.html')

if __name__ == '__main__':
    app.run(debug=True)
```

You will need to create a `chatbot.html` file in a `templates` folder in the same directory as your Python file. Here is an example of `chatbot.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Chatbot</title>
</head>
<body>
    <h1>Welcome to the Chatbot!</h1>
    <div id="chat-container">
        <div id="chat-messages"></div>
        <input type="text" id="user-input" placeholder="Type your message...">
        <button id="send-btn">Send</button>
    </div>
    <script>
        // Add your chatbot functionality here
    </script>
</body>
</html>
```

This code sets up a basic Flask server that serves the `chatbot.html` file. You can further enhance the chatbot functionality by adding JavaScript code within the `<script>` tag in the HTML file to handle user interactions and chatbot responses.