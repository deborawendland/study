import operations.folder_operations as fold_op
import operations.item_operations as item_op
import logging


def folders_sync(folders_to_sync):
    logging.info('synchronizing folders...')
    fold_op.create_folders(folders_to_sync['create'])
    fold_op.delete_folders(folders_to_sync['delete'])
    fold_op.keep_folders(folders_to_sync['keep'])

def items_sync(items_to_sync):
    logging.info('syncronizing items...')
    item_op.create_items(items_to_sync['create'])
    item_op.delete_items(items_to_sync['delete'])
    item_op.copy_items(items_to_sync['copy'])
    item_op.keep_items(items_to_sync['keep'])

def perform_operations(operations):
    folders_sync(operations['folders'])
    items_sync(operations['items'])