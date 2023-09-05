import logging
import os
import shutil

def create_items(items):
    for source, replica in items:
        try:
            shutil.copyfile(source, replica)
            logging.info(f'created item:     {source} to {replica}')
        except Exception as error:
            logging.error(f'created item:     {source} to {replica} - {error}')

def delete_items(items):
    for item in items:
        logging.info(f'deleting item:     {item}...')

def copy_items(items):
    for source, replica in items:
        logging.info(f'copying item:      {source} to {replica}...')

def keep_items(items):
    for item in items:
        logging.info(f'keeping item:      {item}...')