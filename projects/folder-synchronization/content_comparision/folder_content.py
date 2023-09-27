import os

def if_folder_in_path(path, items):
    for item in items:
        if os.path.isdir(os.path.normpath(os.path.join(path, item))):
            return True
    return False

def get_folders_in_path(folder):
    for item in folder['items']:
        path_item = os.path.normpath(os.path.join(folder['path'], item))
        if os.path.isdir(path_item):
            folder_items = get_folder_content(path_item, False)
            new_folder = {
                'path': path_item,
                'items': folder_items
            }
            folder['items'][item] = new_folder

            get_structure(new_folder)
            
    return folder

def get_folder_content(path, replica):
    # print (f'checking items in {path}...')
    if os.path.isdir(path):
        # print (f'{path}: {os.listdir(path)}')
        return os.listdir(path)
    else:
        if replica:
            # print (f'creating {path} directory...')
            os.mkdir(path)
            return []
        else:
            raise NotADirectoryError('Folder not found.')
        
def get_structure(folder):
    if if_folder_in_path(folder['path'], folder['items']):
        for index, item in enumerate(folder['items']):
            path_item = os.path.normpath(os.path.join(folder['path'], item))
            if os.path.isdir(path_item):
                folder_items = get_folder_content(path_item, False)
                new_folder = {
                    'path': path_item,
                    'items': folder_items
                }
                folder['items'][index] = new_folder
                get_structure(new_folder)
    return folder