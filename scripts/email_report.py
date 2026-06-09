import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = "hariom9534aaaa@gmail.com"
receiver = "ashu953442@gmail.com"

# Gmail App Password (NOT your normal Gmail password)
password = "liks auga ltdx pazq"

subject = "Weekly Mutual Fund Report"

body = """
Weekly Mutual Fund Report

Dashboard Updated Successfully
Risk Analysis Updated Successfully
Performance Analysis Updated Successfully
Portfolio Scorecard Updated Successfully

Generated from Bluestock MF Analytics Project
"""

msg = MIMEMultipart()

msg["From"] = sender
msg["To"] = receiver
msg["Subject"] = subject

msg.attach(MIMEText(body, "plain"))

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    server.login(sender, password)

    server.sendmail(
        sender,
        receiver,
        msg.as_string()
    )

    server.quit()

    print("Email sent successfully!")

except Exception as e:
    print("Error:", e)