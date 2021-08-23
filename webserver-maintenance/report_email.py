#!/usr/bin/env python3
import reports
import emails
import os
from datetime import date

# Configs
descpath = os.path.expanduser('~') + '/supplier-data/descriptions/'
report = []

# Process data for PDF
def process_data(data):
    for fruit in data:
        report.append("name: {}<br/>weight: {}<br/>".format(fruit[0], fruit[1]))
    return report

# Process each text file
text_data = []
for file in os.listdir(descpath):
    with open(descpath + file, 'r') as f:
        text_data.append([line.strip() for line in f.readlines()])
        f.close()

if __name__ == "__main__":
    # Generate PDF
    paragraph = "<br/><br/>".join(process_data(text_data))
    title = "Processed Update on {}".format(date.today().strftime("%B %d, %Y"))
    attachment = "/tmp/processed.pdf"
    reports.generate_report(attachment, title, paragraph)

    # Generate email
    subject = "Upload Completed - Online Fruit Store"
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send_email(message)
