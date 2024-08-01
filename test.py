# Original code
def process_data(data):
    # Process the data
    processed_data = []
    for item in data:
        processed_data.append(item * 2)
    return processed_data

# Malicious code
import datetime

def process_data(data):
    # Logic bomb: Check if today's date is January 1st
    if datetime.datetime.now().strftime('%m-%d') == '01-01':
        # On January 1st, delete all data (malicious intent)
        return []

    # Process the data
    processed_data = []
    for item in data:
        processed_data.append(item * 2)
    return processed_data
