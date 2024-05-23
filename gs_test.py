import gspread
from datetime import datetime, timedelta
from oauth2client.service_account import ServiceAccountCredentials

def sort_by_date(Dict):
    # inner sort by Time
    sorted_by_time = dict(sorted(Dict.items(), key=lambda x: x[1]['Time']))
    # Outer sort by Date
    sorted_tuple = sorted(sorted_by_time.items(), key=lambda x: x[1]['Date'])
    # sorted tuple is sorted by Date and by Time inside one Date
    return sorted_tuple

def get_time(record):
    return datetime.strptime(record['Time'], "%H:%M:%S")

def get_date(record):
    return datetime.strptime(record['Date'], "%d.%m.%Y")

# Connect to google sheets
scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]


# Use JSON as keyfile
credentials = ServiceAccountCredentials.from_json_keyfile_name("gs-credentials.json", scope)
client = gspread.authorize(credentials)


# Open Google Sheet with name Event form (responses)
sheet = client.open('Event form (responses)')

# Create a worksheet from first sheet of sheets
worksheet = sheet.worksheet("Ответы на форму (1)")


all_records = worksheet.get_all_records()
def filter_records(records, date_field, comparison_date, border_date):
    filtered_records = []
    for record in records:
        record_date = datetime.strptime(record[date_field], "%d.%m.%Y")  # Adjust format as needed
        if record_date >= comparison_date and record_date <= border_date:
            filtered_records.append(record)
    return filtered_records


def sort_records(filtered_records):
    sorted_records_by_time = sorted(filtered_records, key=get_time)
    sorted_records = sorted(sorted_records_by_time, key=get_date)

    return sorted_records
# Define the field name that contains the date and the comparison date (today)
date_field_name = 'Date'  # Adjust this to the name of your date field
today = datetime.now()

# Filter the records
filtered_records = filter_records(all_records, date_field_name, today, today + timedelta(days=3))


sorted_records = sort_records(filtered_records)

# Print the filtered records
print(filtered_records)

print(sorted_records)
print(type(filtered_records[0]))
