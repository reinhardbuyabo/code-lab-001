# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

from functions import read_excel_file
from generate_email_addresses import generate_unique_emails
file_path = "Test Files.xlsx"

df = read_excel_file(file_path)

if df is not None:
    print("Original DataFrame:")
    print(df.head())

    unique_emails = generate_unique_emails(df)

    # Add emails to DataFrame
    df['Email Address'] = unique_emails

    # updated DataFrame
    print("\nUpdated DataFrame with email addresses:")
    print(df.head())

    print("\nStudent Names and Email Addresses:")
    for _, row in df.iterrows():
        print(f"Student Name: {row['Student Name']} - Email address: {row['Email Address']}")

else:
    print("Failed to read the Excel file.")
