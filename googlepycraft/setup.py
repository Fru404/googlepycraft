# setup.py

from setuptools import setup

setup(
    name='googlepycraft',
    version='0.1',
    packages=['googlepycraft', 'googlepycraft.firestoreupload', 'googlepycraft.gsheetsdb'],
    install_requires=[
        'firebase-admin',
        'gspread',
        'oauth2client',
        'pandas',
    ],
)
