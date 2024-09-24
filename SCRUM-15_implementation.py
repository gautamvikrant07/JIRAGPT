```python
import chatbot
import xbrl

def xbrl_dashboard(chatbot):
    while True:
        user_input = chatbot.get_user_input()
        
        if user_input.lower() == 'view xbrl data':
            xbrl_data = xbrl.fetch_data()
            chatbot.display_message("Xbrl Data:")
            chatbot.display_data(xbrl_data)
        elif user_input.lower() == 'analyze xbrl data':
            xbrl_data = xbrl.fetch_data()
            analysis = xbrl.analyze_data(xbrl_data)
            chatbot.display_message("Xbrl Data Analysis:")
            chatbot.display_data(analysis)
        elif user_input.lower() == 'exit':
            chatbot.display_message("Exiting Xbrl Dashboard")
            break
        else:
            chatbot.display_message("Invalid input. Please try again.")

# Create a Chatbot instance
my_chatbot = chatbot.Chatbot()

# Display Xbrl functionality dashboard for the chatbot
xbrl_dashboard(my_chatbot)
```
This sample Python code demonstrates a basic Xbrl functionality dashboard for a chatbot. The dashboard allows users to view Xbrl data, analyze Xbrl data, and exit the dashboard. The `chatbot` and `xbrl` modules are assumed to contain the necessary functions for interacting with the chatbot and fetching/analyzing Xbrl data.