import logging

def create_items(items):
    for source, replica in items:
        logging.info(f'creating item:     {source} to {replica}...')

def delete_items(items):
    for item in items:
        logging.info(f'deleting item:     {item}...')

def copy_items(items):
    for source, replica in items:
        logging.info(f'copying item:      {source} to {replica}...')

def keep_items(items):
    for item in items:
        logging.info(f'keeping item:      {item}...')