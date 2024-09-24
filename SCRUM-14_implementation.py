Sure! Here is a sample Python code that creates an email functionality dashboard for a chatbot:

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, message, to_email):
    from_email = 'your_email@example.com'
    password = 'your_email_password'
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

# Sample usage
subject = 'Chatbot Email Dashboard'
message = 'This is your email functionality dashboard for the chatbot.'
to_email = 'recipient@example.com'

send_email(subject, message, to_email)
```

In this code snippet, we define a `send_email` function that takes the subject, message, and recipient email address as input parameters. The function creates an email message using `MIMEMultipart` and `MIMEText` classes, then sends the email using the `smtplib` library. Finally, we demonstrate how to use the `send_email` function with a sample subject, message, and recipient email address.