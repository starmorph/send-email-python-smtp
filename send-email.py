import smtplib

# Set the email parameters
from_addr = "your_email@example.com"
to_addr = "recipient_email@example.com"
subject = "Email Subject"
body = "Email Body"

# Construct the email message
msg = f"Subject: {subject}\n\n{body}"

# Set the SMTP server and login credentials
smtp_server = "smtp.example.com"
username = "your_username"
password = "your_password"

# Send the email
server = smtplib.SMTP(smtp_server)
server.login(username, password)
server.sendmail(from_addr, to_addr, msg)
server.quit()

print("Email sent successfully!")
