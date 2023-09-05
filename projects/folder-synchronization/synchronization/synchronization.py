from content_comparision import content_comparision, folder_content
from operations import operations as op
import logging

def analyse_content(source, replica):
    logging.info(f'comparing source: {source["path"]} to replica: {replica["path"]}...')
    folder_content.get_structure(source)
    folder_content.get_structure(replica)

    # print (f'source: {source}')
    # print (f'replica: {replica}')

    operations = {
        'items': {
            'create': [],
            'delete': [],
            'copy': [],
            'keep': []
        },
        'folders': {
            'create': [],
            'delete': [],
            'keep': []
        }
        
    }
    
    content_comparision.compare_structures(source, replica, operations)

    return operations

def run_sync(params):
    source = {
        'path': params['source'],
        'items': folder_content.get_folder_content(params['source'], False)
    }
    replica = {
        'path': params['replica'],
        'items': folder_content.get_folder_content(params['replica'], True)
    }

    operations = analyse_content(source, replica)
    # print (operations)
    op.perform_operations(operations)
    