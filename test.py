#import package
from googlepycraft.googleSheet.gsheetsdb import gsheetsdb as gb
from googlepycraft.fireStore.firestoreupload import firestoreupload
from googlepycraft.app_config import Admin
import os

# Instantiate the Admin class
admin_instance = Admin()
os.environ['SHEET_NUMBER'] = '3'
# Access the variables from the admin instance
credentials_path = admin_instance.credentials_path
sheetNumber = os.environ.get('SHEET_NUMBER')
sheet_url = admin_instance.sheet_url(sheet_number=sheetNumber)
storage_bucket = admin_instance.storage_bucket

# Now you can use these variables as needed
gsheets_instance = gb(credentials_path, sheet_url,sheet_number=sheetNumber)

#begin by instanciating the class
gsheets_instance = gb(credentials_path,sheet_url)
fire_instance=firestoreupload(storage_bucket='realtime-375815.appspot.com',credentials_path=credentials_path)

sheets=gsheets_instance


DataFrame = sheets.in_pd()

SecondSheet=DataFrame[:2]

FinSheet=DataFrame[:10]
print(FinSheet)
print(SecondSheet)
print(sheets.read_sheet('Country',10))


#fire_instance.upload_file(local_file_path='/workspaces/codespaces-blank/FirstSheet.xlsx')

#fire_instance.get_file('https://storage.googleapis.com/realtime-375815.appspot.com//workspaces/codespaces-blank/FirstSheet%20.xlsx',local_folder='local')

#sheets.save(SecondSheet,'secondsheet.xlsx')#saving file
#fire_instance.upload_file(local_file_path='FirstSheet.xlsx')#uploading file
#fire_instance.get_file(file_url='https://storage.googleapis.com/realtime-375815.appspot.com/secondsheet.xlsx')