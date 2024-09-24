Sure! Here is a sample Python code using Flask to create a simple webpage for a chatbot:

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('chatbot.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_message']
    
    # Your chatbot logic here
    bot_response = "You said: " + user_message
    
    return bot_response

if __name__ == '__main__':
    app.run(debug=True)
```

In this code, we have defined two routes: 
1. The '/' route renders the `chatbot.html` template, which will contain the chatbot interface.
2. The '/get_response' route is a POST route that receives the user's message, processes it with your chatbot logic, and returns the bot's response.

You will need to create a `chatbot.html` template file in the `templates` folder in your Flask project directory to display the chatbot interface.