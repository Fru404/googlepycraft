#import package
from googlepycraft.googleSheet.gsheetsdb import gsheetsdb as gb
from googlepycraft.fireStore.firestoreupload import firestoreupload
#setup your credentials
credentials_path = 'credentials.json'
sheet_url='https://docs.google.com/spreadsheets/d/15FfUKjivLLftJ3R0eDVuxUYRFJd6pyWWOc8vWxTiLlA/edit#gid=0'

#begin by instanciating the class
gsheets_instance = gb(credentials_path,sheet_url)
fire_instance=firestoreupload(storage_bucket='realtime-375815.appspot.com',credentials_path=credentials_path)

sheets=gsheets_instance


DataFrame = sheets.in_pd()

SecondSheet=DataFrame[:2]

#sheets.read_sheet('name',None,2,4)


#fire_instance.upload_file(local_file_path='/workspaces/codespaces-blank/FirstSheet.xlsx')

#fire_instance.get_file('https://storage.googleapis.com/realtime-375815.appspot.com//workspaces/codespaces-blank/FirstSheet%20.xlsx',local_folder='local')

#sheets.save(SecondSheet,'secondsheet.xlsx')#saving file
fire_instance.upload_file(local_file_path='FirstSheet.xlsx')#uploading file
#fire_instance.get_file(file_url='https://storage.googleapis.com/realtime-375815.appspot.com/secondsheet.xlsx')