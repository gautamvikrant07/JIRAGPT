Here is a sample Python script that monitors system resources (CPU, memory, disk) and sends an alert email when usage exceeds certain thresholds:

```python
import psutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Function to get system resource usage
def get_system_resources():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    
    return cpu_usage, memory_usage, disk_usage

# Function to send email alert
def send_alert_email(subject, body):
    sender_email = 'your_email@gmail.com'
    receiver_email = 'recipient_email@gmail.com'
    password = 'your_email_password'
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

# Set the thresholds for CPU, memory, and disk usage
cpu_threshold = 80
memory_threshold = 80
disk_threshold = 80

# Monitor system resources and send alert if thresholds are exceeded
cpu_usage, memory_usage, disk_usage = get_system_resources()

if cpu_usage > cpu_threshold:
    send_alert_email('High CPU Usage Alert', f'CPU usage is at {cpu_usage}%')

if memory_usage > memory_threshold:
    send_alert_email('High Memory Usage Alert', f'Memory usage is at {memory_usage}%')

if disk_usage > disk_threshold:
    send_alert_email('High Disk Usage Alert', f'Disk usage is at {disk_usage}%')
```

Please make sure to replace the placeholder email addresses and passwords with your actual email credentials. Also, note that you may need to enable "less secure apps" access in your email account settings to send emails using this script.