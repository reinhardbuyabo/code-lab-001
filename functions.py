import re
import pandas as pd
import logging
from constraints import EMAIL_DOMAIN

def sanitize_name(name):
    """
    Remove special characters(non-word characters) or white spaces, and convert to lowercase.
    Basically, it removes punctuation marks, spaces and tabs.
    """
    sanitized = re.sub(r'[^\w\s]', '', name)
    return sanitized.lower()

def generate_email(first_name, last_name, existing_emails):
    """
    Generate a unique email address based on first and last names.
    """
    base_email = f"{first_name[0]}{last_name}".replace(" ", "")
    email = f"{base_email}@{EMAIL_DOMAIN}"
    counter = 1
    while email in existing_emails:
        # if the generated email already exists, then we add a numeric suffix starting from 1, making each one unique
        email = f"{base_email}{counter}@{EMAIL_DOMAIN}"
        counter += 1
    return email

def setup_logging(log_file):
    """
    Setup logging configuration.
    """
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s:%(levelname)s:%(message)s'
    )

# Params: Input File
# Returns: DataFrame
def read_student_data(input_file):
    """
    Read student data from Excel file.
    """
    try:
        df = pd.read_excel(input_file)
        logging.info(f"Successfully read input file: {input_file}")
        return df
    except Exception as e:
        logging.error(f"Error reading input file: {e}")
        raise

def save_output(df, csv_path, tsv_path):
    """
    Save the DataFrame to CSV and TSV files.
    """
    try:
        df.to_csv(csv_path, index=False)
        df.to_csv(tsv_path, sep='\t', index=False)
        logging.info(f"Successfully saved output files: {csv_path}, {tsv_path}")
    except Exception as e:
        logging.error(f"Error saving output files: {e}")
        raise

def separating_gender(df):
    """Separate names of male and female students"""
    male_students = df[df['Gender'] == 'M']
    female_students = df[df['Gender'] == 'F']

    """Counting Male and Female Students"""
    num_of_male_stds = male_students.shape[0]
    num_of_female_stds = female_students.shape[0]
    return male_students, female_students, num_of_male_stds, num_of_female_stds

def special_students(df):
    """Regex to find names with special characters (like apostrophes, hyphens, etc.)"""
    df2 = df[df['Student Name'].str.contains(r"['\-]")]
    return df2['Student Name'].tolist()

