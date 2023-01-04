# Send Email with SMTP Python Script 
## python script to send email with smtp using the `smtplib` library 

![Image SEO Optimizer Starmorph](https://i.imgur.com/XmHkQVS.png)
Created by [Starmorph Web Design](https://starmorph.com)


## Features

- Sends an email from a specified sender to a specified recipient.
- Allows you to set the subject and body of the email.
- Uses an SMTP server to send the email.

## Usage

To use the script, set the email parameters in the following lines of code:

```
from_addr = "your_email@example.com"
to_addr = "recipient_email@example.com"
subject = "Email Subject"
body = "Email Body"
```

Replace your_email@example.com with your email address, recipient_email@example.com with the recipient's email address, and set the subject and body variables to the desired subject and body of the email.

Then, set the SMTP server and login credentials in the following lines of code:
```
smtp_server = "smtp.example.com"
username = "your_username"
password = "your_password"
```

Replace `smtp.example.com` with the address of the SMTP server, and `your_username` and `your_password` with your login credentials for the SMTP server.

## Dependencies
The script requires the smtplib library.

## Note
Make sure to allow less secure apps to access your Google Account if you are using a Gmail account as the sender. You can do this by going to the Security section of your Google Account settings and turning on the option to "Allow less secure apps."