import logging
import os
import sys

def create_folders(folders):
    for folder in folders:
        try: 
            os.mkdir(folder) 
            logging.info(f'creating folder:   {folder}...')
        except OSError as error: 
            print(error) 
            logging.error(f'error creating folder:   {folder} - {error}')

def delete_folders(folders):
    for folder in folders:
        logging.info(f'deleting folder:   {folder}...')

def keep_folders(folders):
    for folder in folders:
        logging.info(f'keeping folder:    {folder}...')