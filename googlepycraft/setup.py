# setup.py

from setuptools import setup

setup(
    name='googlepycraft',
    version='0.1',
    packages=['firestoreupload','gsheetsdb'],
    install_requires=[
        'firebase-admin',
        'gspread',
        'oauth2client',
        'pandas',
        'json',
    ],
)
