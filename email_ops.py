"""
+----------------+-------------------------------------------------------------+
| Author:        | Ganesh Kuramsetti                                           |
+----------------+-------------------------------------------------------------+
| Script Name:   | email_ops.py                                                |
+----------------+-------------------------------------------------------------+
| Date Created:  | 04-July-2021                                                |
+----------------+-------------------------------------------------------------+
| Description:   | Script that includes functions related to email operations. |
+----------------+-------------------------------------------------------------+
| Language:      | python                                                      |
+----------------+-------------------------------------------------------------+
| Prerequisites: | python, smtplib                                             |
+----------------+-------------------------------------------------------------+
| Instructions:  | Integrate with other scripts and use the function required. |
+----------------+-------------------------------------------------------------+
| Date Updated:  | 16-Dec-2021                                                 |
+----------------+-------------------------------------------------------------+
"""

#!/usr/bin/python

# importing libraries.
import smtplib
from email.message import EmailMessage

def send_email(email_credentials,email_message):
    """
    A function which accepts email credentials(a dictonary)
    and an EmailMessage as parameter.
    Sends the email with the data provided.
    """
    email_id = email_credentials["user_id"]
    email_passwd= email_credentials["user_passwd"]

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_id, email_passwd)
        smtp.send_message(email_message)

def prepare_email_data(from_email, to_email, subject, content):
    """
    This function prepares an email message by accepting
    to whom the email needs to be sent to, what's the subject
    and what should be the email content.
    """
    email_message = EmailMessage()
    email_message["Subject"] = subject
    email_message["From"] = from_email
    email_message["To"] = to_email
    email_message.set_content(content)
    return email_message
