from googlepycraft.googleSheet.gsheetsdb import gsheetsdb as gb
from googlepycraft.fireStore.firestoreupload import FireStoreUpload
#credentials_path = '/workspaces/codespaces-blank/googleSheet/credentials.json'
sheet_url = 'https://docs.google.com/spreadsheets/d/15FfUKjivLLftJ3R0eDVuxUYRFJd6pyWWOc8vWxTiLlA/edit#gid=0'
project_id = "inspire-innovation"
bucket_name = "inspire-innovation.appspot.com"
#gsheets_instance = gb(credentials_path,sheet_url)

#gsheets_instance.read_sheet(key='email',number_of_rows=2)

#gsheets_instance.in_json(target_key=None, num_rows=None,  start_index=2, end_index=4)

#DataFrame=gsheets_instance.in_pd()

fire_instance=FireStoreUpload(storage_bucket='inspire-innovation.appspot.com',credentials_path='/workspaces/codespaces-blank/fireStore/Fire_store_cred.json')
fire_instance.upload_file(local_file_path='FirstSheet.xlsx')

