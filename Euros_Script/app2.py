import pandas as pd
from datetime import datetime, timedelta

# Read the dataset from CSV
df = pd.read_csv('dataset.csv')

# Function to convert date and time to IST
def convert_to_ist(row):
    datetime_str = row['Date'] + ' ' + row['Time']
    datetime_utc = datetime.strptime(datetime_str, '%d %B %Y %H:%M:%S')
    datetime_ist = datetime_utc + timedelta(hours=3, minutes=30)  # Convert to IST (UTC+3:30)
    return datetime_ist.strftime('%d %B %Y %H:%M:%S IST')

# Apply the function to create IST datetime column
df['IST_datetime'] = df.apply(convert_to_ist, axis=1)

# Drop the 'Date' and 'Time' columns
df.drop(columns=['Date', 'Time'], inplace=True)

# Save only 'match' and 'IST_datetime' columns to a new CSV file
df[['match', 'IST_datetime']].to_csv('dataset_new.csv', index=False)