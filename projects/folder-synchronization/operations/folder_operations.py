import logging
import os
import sys

def create_folders(folders):
    for folder in folders:
        try: 
            os.mkdir(folder) 
            logging.info(f'created folder:   {folder}')
        except OSError as error: 
            print(error) 
            logging.error(f'error creating folder:   {folder} - {error}')

def delete_folders(folders):
    for folder in folders:
        try:
            os.removedirs(folder)
            logging.info(f'deleted folder:   {folder}')
        except OSError as error:
            logging.error(f'error deleting folder:   {folder} - {error}')

def keep_folders(folders):
    for folder in folders:
        logging.info(f'keeping folder:    {folder}...')