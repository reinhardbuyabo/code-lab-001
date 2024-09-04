# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
from functions import read_excel_file

file_path = "Test Files.xlsx"

df = read_excel_file(file_path)

if df is not None:
    print(df.head())
else:
    print("Failed to read the Excel file.")
