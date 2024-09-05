import pandas as pd

def generate_email_addresses():
    df = pd.read_excel('test_files.xlsx')
    emails = []
    for index, row in df.iterrows():
        emails.append(iterations(row))
        print(iterations(row))
    return emails

def iterations(row):
    # Assuming
    full_name = row['Student Name'] # returns a single instance of name
    # Splitting the name by the comma

    parts = full_name.split(',')
    print(f"Parts: {parts} ")
    if len(parts) > 1:
        surname = parts[0]
        rest_of_name = parts[1]
        given_names = rest_of_name.strip().split(' ')
        print(f"{given_names} Given")
        if len(given_names) == 1:
            return f"{surname[0].lower()}{given_names[0].lower()}"
        elif len(given_names) > 1:
            return f"{surname[0].lower()}{given_names[-1].lower()}@gmail.com"