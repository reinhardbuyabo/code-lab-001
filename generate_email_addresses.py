"""This python module generates email addresses of all students based on the specifications of...
- all addresses should be unique
- use two names if available
- no special characters in the emails
"""

import re

def generate_email(name):
    # Remove special characters and split the name
    clean_name = re.sub(r'[^a-zA-Z\s]', '', name)
    name_parts = clean_name.lower().split()

    # Use the first letter of the first name and the last name
    if len(name_parts) > 1:
        email = f"{name_parts[0][0]}{name_parts[-1]}@gmail.com"
    else:
        email = f"{name_parts[0]}@gmail.com"

    return email


def generate_unique_emails(df):
    emails = set()
    unique_emails = []

    for _, row in df.iterrows():
        base_email = generate_email(row['Student Name'])
        email = base_email
        counter = 1

        while email in emails:
            email = f"{base_email[:-10]}{counter}@gmail.com"
            counter += 1

        emails.add(email)
        unique_emails.append(email)

    return unique_emails