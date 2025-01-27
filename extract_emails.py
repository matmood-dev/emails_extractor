import re

def extract_emails(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()

    # Regex pattern for matching email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, content)

    with open(output_file, 'w') as file:
        file.write(','.join(emails))

# Example usage
input_file = 'input.txt'
output_file = 'emails.txt'
extract_emails(input_file, output_file)
