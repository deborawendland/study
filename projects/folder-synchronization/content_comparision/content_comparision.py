import os
import filecmp

def create_path(path, file):
    return os.path.normpath(os.path.join(path, file))

def register_operation(operation, path, file):
    filepath = create_path(path, file)
    operation.append(filepath)
    return {
        'path': filepath,
        'items': []
    }

def compare_items(source, replica, item, operations, is_source):
    path_item_source = create_path(source['path'], item)
    path_item_replica = create_path(replica['path'], item)
    
    if is_source:
        if item in replica['items']:
            # compare content of two files, if equal keep, otherwise copy
            if filecmp.cmp(path_item_source, path_item_replica, shallow=False):
                operations['items']['keep'].append(path_item_replica)
            else:
                operations['items']['copy'].append((path_item_source, path_item_replica))
        else:
            operations['items']['create'].append((path_item_source, path_item_replica))
    else: 
        if item not in source['items']:
            operations['items']['delete'].append(path_item_replica)

def compare_folders(folder, item, operations, is_source):    
    if is_source:
        # if replica items is empty, create item (folder) and so recursively 
        if not folder['items']:
            item_replica = register_operation(operations['folders']['create'], folder['path'], os.path.basename(item['path']))
            compare_structures(item, item_replica, operations)

        else: 
            replica_folders = []
            # there is a item (folder) in replica, checking if it also contains other items inside it in replica, if so compare it recursively
            for item_replica in folder['items']:
                if type(item_replica) is dict:
                    replica_folders.append(os.path.basename(item_replica['path']))
                    if os.path.basename(item['path']) == os.path.basename(item_replica['path']):
                        register_operation(operations['folders']['keep'], folder['path'], os.path.basename(item['path']))
                        compare_structures(item, item_replica, operations)
            
            # if the item (folder) doesn't exist in replica, create it, and so on recursively
            if os.path.basename(item['path']) not in replica_folders: 
                item_replica = register_operation(operations['folders']['create'], folder['path'], os.path.basename(item['path']))
                compare_structures(item, item_replica, operations)
    else:
        # for each folder existing only in replica, it will compare recursively to delete it and its items
        source_folders = []
        for item_source in folder['items']:
            if type(item_source) is dict:
                source_folders.append(os.path.basename(item_source['path']))

        if os.path.basename(item['path']) not in source_folders:
            item_source = register_operation(operations['folders']['delete'], item['path'], '')
            compare_structures(item_source, item, operations)

def compare_structures(source, replica, operations):
    for item_source in source['items']:
        if type(item_source) is dict:
            compare_folders(replica, item_source, operations, True)
        else:
            compare_items(source, replica, item_source, operations, True)
    
    for item_replica in replica['items']:
        if type(item_replica) is dict:
            compare_folders(source, item_replica, operations, False)
        else:
            compare_items(source, replica, item_replica, operations, False)
