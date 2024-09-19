import csv
import pandas as pd

# Function to convert 12-hour format to 24-hour format
def convert_to_24_hour(timestamp):
    try:
        # Attempt to convert to datetime
        dt_timestamp = pd.to_datetime(timestamp, format='%m/%d/%Y %I:%M:%S %p', errors='raise')
        
        # Check for NaT (Not a Time)
        if pd.isna(dt_timestamp):
            return ''
        
        # Convert to 24-hour format
        return dt_timestamp.strftime('%Y-%m-%d %H:%M:%S')
    
    except ValueError:
        # Handle value errors (invalid date/time format)
        return ''

# Input and output file paths
input_file_path = 'nyc_311_sample_2P.csv'
output_file_path = 'modified_nyc_311_sample_2P.csv'

# Open the input CSV file and create a CSV reader
with open(input_file_path, 'r', newline='', encoding='utf-8') as input_file:
    csv_reader = csv.reader(input_file)
    
    # Read the header and get the column indices
    header = next(csv_reader)
    timestamp_columns = ['Created Date', 'Closed Date', 'Due Date', 'Resolution Action Updated Date']
    indices = [header.index(column) for column in timestamp_columns]

    # Open the output CSV file and create a CSV writer
    with open(output_file_path, 'w', newline='', encoding='utf-8') as output_file:
        csv_writer = csv.writer(output_file)
        
        # Write the header to the output file
        csv_writer.writerow(header)

        # Process each line in the input file
        for row in csv_reader:
            # Convert 12-hour format timestamps to 24-hour format
            for index in indices:
                row[index] = convert_to_24_hour(row[index])

            # Write the modified row to the output file
            csv_writer.writerow(row)

print("Conversion complete. Modified data saved to:", output_file_path)
