Sure! Here is a sample Python script that monitors system resources and sends an alert email when usage exceeds certain thresholds:

```python
import psutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Function to get system resource usage
def get_system_resources():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    return cpu_usage, memory_usage, disk_usage

# Function to send email alert
def send_email_alert(subject, message):
    sender_email = "your_email@example.com"
    receiver_email = "recipient_email@example.com"
    password = "your_email_password"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login(sender_email, password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

# Main function
def main():
    cpu_threshold = 80
    memory_threshold = 80
    disk_threshold = 80

    cpu_usage, memory_usage, disk_usage = get_system_resources()

    if cpu_usage > cpu_threshold:
        send_email_alert("CPU Usage Alert", f"CPU usage is {cpu_usage}%")

    if memory_usage > memory_threshold:
        send_email_alert("Memory Usage Alert", f"Memory usage is {memory_usage}%")

    if disk_usage > disk_threshold:
        send_email_alert("Disk Usage Alert", f"Disk usage is {disk_usage}%")

if __name__ == "__main__":
    main()
```

Please make sure to replace the placeholder email addresses, password, and SMTP server details with your actual information before running the script.