
import logging

from functions import (
    sanitize_name,
    generate_email,
    setup_logging,
    read_student_data,
    save_output
)
from constraints import (
    LOG_FILE,
    INPUT_FILE,
    OUTPUT_CSV,
    OUTPUT_TSV
)

def main():
    """Setup logging"""
    setup_logging(LOG_FILE)
    logger = logging.getLogger()

    logger.info("Starting email generation process.")

    """Read student data"""
    df = read_student_data(INPUT_FILE)

    existing_emails = set()
    emails = []

    for index, row in df.iterrows():
        student_name = row.get('Student Name', '').strip()
        logger.info(f"Processing student: {student_name}")

        if not student_name:
            logger.warning(f"Empty name at index {index}. Skipping.")
            emails.append('')
            continue

        """Sanitize the student name"""
        sanitized_name = sanitize_name(student_name)
        name_parts = sanitized_name.split()

        if len(name_parts) >= 2:
            first_name, last_name = name_parts[0], name_parts[-1]
        elif len(name_parts) == 1:
            first_name = name_parts[0]
            last_name = name_parts[0]
        else:
            logger.warning(f"Invalid name format for student at index {index}: {student_name}")
            emails.append('')
            continue

        """Generate email"""
        email = generate_email(first_name, last_name, existing_emails)
        emails.append(email)
        existing_emails.add(email)
        logger.info(f"Generated email: {email}")

    """Add the emails to the DataFrame"""
    df['Email Address'] = emails

    """Save the output"""
    save_output(df, OUTPUT_CSV, OUTPUT_TSV)

    logger.info("Email generation process completed.")

if __name__ == "__main__":
    main()
