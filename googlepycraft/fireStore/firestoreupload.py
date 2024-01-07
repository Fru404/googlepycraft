# firestoreupload.py


from firebase_admin import credentials, initialize_app, storage
import requests 
import os
import yaml
import datetime
import random
import string

class firestoreupload:
    def __init__(self, credentials_path, storage_bucket) -> None:
        """
        Initialize the FireStoreUpload class.

        :param credentials_path: Path to the Firebase service account credentials JSON file.
        :param storage_bucket: Firebase Storage bucket name.
        """
        self.credentials_path = credentials_path
        self.storage_bucket = storage_bucket
        self.file_url=''
        
        
    def generate_reference(self):
        ints = random.randrange(1000000, 10000000)
        digit = str(ints)
        letter = random.choice(string.ascii_lowercase)
        return letter + digit

    def save_message_to_yaml(self, message, message_yml):
        try:
            with open(message_yml, 'a') as yaml_file:
                yaml.dump(message, yaml_file, default_flow_style=False)
            print(f'{yaml.dump(message,default_flow_style=False)} Saved')
        except Exception as e:
            print(f'Error saving message: {e}')

    def overwrite_message_in_yaml(self, existing_data, message, message_yml):
        print(yaml.dump(existing_data,default_flow_style=False))
        user_input = input("The document already exists. Do you want to continue? (y/n): ")
        if user_input == 'y':
            existing_data.update(message)
            try:
                with open(message_yml, 'w') as yaml_file:
                    yaml.dump(existing_data, yaml_file, default_flow_style=False)
                print('/n')
                print(f'{yaml.dump(message,default_flow_style=False)} Document uploaded')
            except Exception as e:
                print(f'Error overwriting message: {e}')
        else:
            print('/n')
            print(f'{yaml.dump(message,default_flow_style=False)} Not uploaded')

        

    def upload_file(self, local_file_path):
        """
        Upload a file to Firebase Storage.

        :param local_file_path: Path to the local file to be uploaded.
        """
      
        self.local_file_path = local_file_path
        try:
            # Initialize Firebase app with credentials and storage bucket
            cred = credentials.Certificate(self.credentials_path)
            initialize_app(cred, {'storageBucket': self.storage_bucket})

            # Get file name from the local file path
            fileName = local_file_path

            # Get reference to the default storage bucket
            bucket = storage.bucket()

            # Create a blob (object) in the bucket with the same name as the local file
            blob = bucket.blob(fileName)

            # Upload the file to Firebase Storage
            blob.upload_from_filename(fileName)

            # Make the uploaded file public
            blob.make_public()
            
            self.file_url=blob.public_url
            #keep track of time uploaded
            # Get the current date and time
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            
            # Print success message with the file URL
            ref = self.generate_reference()

            message = {
                'ref': ref,
                'file': fileName,
                'url': self.file_url,
                'time': current_time,
                '#':'################################################'
            }

            message_yml = os.path.join('catalog', 'dossier.yaml')

            os.makedirs('catalog', exist_ok=True)

            if os.path.exists(message_yml):
                with open(message_yml, 'r') as existing_message:
                    existing_data = yaml.safe_load(existing_message)
                    if existing_data and 'ref' in existing_data and existing_data['file'] == fileName:
                        self.overwrite_message_in_yaml(existing_data, message, message_yml)
                    else:
                        self.save_message_to_yaml(message, message_yml)
                        print('file uploaded')
            else:
                  print('file not recieved')
        except Exception as e:
                print(f"Error uploading file: {e}")
                
    def get_file(self,file_url,local_folder='local'):
        """
        Download a file from a public URL and save it to the local folder.

        :param public_url: Public URL of the file to be downloaded.
        :param local_folder: Path to the local folder to save the downloaded file.
        """
        
        try:
            if not os.path.exists(local_folder):
                os.makedirs(local_folder)
                
            file_name = os.path.join(local_folder, file_url.split('/')[-1])
            response = requests.get(file_url)

            # Save the file locally
            with open(file_name, 'wb') as file:
                file.write(response.content)

            print(f"File '{file_name}' downloaded successfully.")

        except Exception as e:
            print(f"Error downloading file: {e}")
            
