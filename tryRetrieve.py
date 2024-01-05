import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Set up the credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('googleSheet/credentials.json', scope)
client = gspread.authorize(creds)

sheet_url = 'https://docs.google.com/spreadsheets/d/15FfUKjivLLftJ3R0eDVuxUYRFJd6pyWWOc8vWxTiLlA/edit#gid=0'
spreadsheet = client.open_by_url(sheet_url)

# Get the first (default) sheet
sheet = spreadsheet.sheet1
# Get all values from the sheet
all_values = sheet.get_all_values()

# Print the retrieved data
for row in all_values:
    print(row)
