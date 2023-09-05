import operations.folder_operations as fold_op
import operations.item_operations as item_op
import logging

def perform_operations(operations):
    logging.info('syncronizing folders...')
    
    fold_op.create_folders(operations['folders']['create'])
    item_op.create_items(operations['items']['create'])
    
    item_op.copy_items(operations['items']['copy'])

    item_op.delete_items(operations['items']['delete'])
    fold_op.delete_folders(operations['folders']['delete'])

    # fold_op.keep_folders(operations['folders']['keep'])
    # item_op.keep_items(operations['items']['keep'])