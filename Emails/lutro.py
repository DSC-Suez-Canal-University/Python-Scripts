import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv
import word2html
from email.mime.base import MIMEBase
from email import encoders

sender_email = "automateddsc@gmail.com"
receiver_email = "mashour365@gmail.com"
password = input("Type your password and press enter:")

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

# filename = "img.jpg"
# # # Open PDF file in binary mode
# # with open(filename, "rb") as attachment:
# #     # Add file as application/octet-stream
# #     # Email client can usually download this automatically as attachment
# #     part = MIMEBase("application", "octet-stream")
# #     part.set_payload(attachment.read())
#
# # Encode file in ASCII characters to send by email
# encoders.encode_base64(part)
#
# # Add header as key/value pair to attachment part
# part.add_header(
#     "Content-Disposition",
#     f"attachment; filename= {filename}",
# )

# Add attachment to message and convert message to string


convertedHtml = word2html.convert('mail.docx', 'string.html')

# Turn these into plain/html MIMEText objects

part2 = MIMEText(convertedHtml.value, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first

message.attach(part2)
# message.attach(part)
# Create secure connection with server and send email
context = ssl.create_default_context()


def sending():
    with open("email_list.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, email in reader:
            print(f"Sending email to {name}")
            server.sendmail(
                sender_email, email, message.as_string())


with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    sending()
