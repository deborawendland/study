import os
import filecmp

PATH_ITEM = "{path}/{item}"

def compare_items_source_to_replica(source, replica, operations, item_source):
    path_item_source = PATH_ITEM.format(path=source["path"], item=item_source)
    if item_source in replica["items"]:
        path_item_replica = PATH_ITEM.format(path=replica["path"], item=item_source)
        if filecmp.cmp(path_item_source, path_item_replica, shallow=False):
            operations["items"]["keep"].append(path_item_replica)
        else:
            operations["items"]["copy_content"].append((path_item_source, path_item_replica))

    else:
        path_item_replica = PATH_ITEM.format(path=replica["path"], item=item_source)
        operations["items"]["create"].append((path_item_source, path_item_replica))

def compare_items_replica_to_source(source, replica, operations, item_replica):
    path_item_replica = PATH_ITEM.format(path=replica["path"], item=item_replica)
    if item_replica not in source["items"]:
        operations["items"]["delete"].append(path_item_replica)

def compare_folders_source_to_replica(replica, operations, item_source):
    if not replica["items"]:
        path_folder_replica = PATH_ITEM.format(path=replica["path"], item=os.path.basename(item_source["path"]))
        operations["folders"]["create"].append(path_folder_replica)
        item_replica = {
            "path": path_folder_replica,
            "items": []
        }
        compare_structures(item_source, item_replica, operations)

    else: 
        replica_folders = []
        for item_replica in replica["items"]:
            if type(item_replica) is dict:
                replica_folders.append(os.path.basename(item_replica["path"]))
                if os.path.basename(item_source["path"]) == os.path.basename(item_replica["path"]):
                    path_folder_replica = PATH_ITEM.format(path=replica["path"], item=os.path.basename(item_source["path"]))
                    operations["folders"]["keep"].append(path_folder_replica)
                    compare_structures(item_source, item_replica, operations)
        
        if os.path.basename(item_source["path"]) not in replica_folders:
            path_folder_replica = PATH_ITEM.format(path=replica["path"], item=os.path.basename(item_source["path"]))
            operations["folders"]["create"].append(path_folder_replica)
            item_replica = {
                "path": path_folder_replica,
                "items": []
            }
    
def compare_folders_replica_to_source(source, operations, item_replica):
    source_folders = []
    for item_source in source["items"]:
        if type(item_source) is dict:
            source_folders.append(os.path.basename(item_source["path"]))

    if os.path.basename(item_replica["path"]) not in source_folders:
        operations["folders"]["delete"].append(item_replica["path"])
        item_source = {
            "path": PATH_ITEM.format(path=source["path"], item=os.path.basename(item_replica["path"])),
            "items": []
        }
        compare_structures(item_source, item_replica, operations)

def compare_structures(source, replica, operations):
    for item_source in source["items"]:
        if type(item_source) is dict:
            compare_folders_source_to_replica(replica, operations, item_source)
        else:
            compare_items_source_to_replica(source, replica, operations, item_source)
    
    for item_replica in replica["items"]:
        if type(item_replica) is dict:
            compare_folders_replica_to_source(source, operations, item_replica)
        else:
            compare_items_replica_to_source(source, replica, operations, item_replica)

