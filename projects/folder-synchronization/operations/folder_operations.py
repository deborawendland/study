import logging
import os
import sys

def create_folders(folders):
    for folder in folders:
        logging.info(f'creating folder:   {folder}...')

def delete_folders(folders):
    for folder in folders:
        logging.info(f'deleting folder:   {folder}...')

def keep_folders(folders):
    for folder in folders:
        logging.info(f'keeping folder:    {folder}...')