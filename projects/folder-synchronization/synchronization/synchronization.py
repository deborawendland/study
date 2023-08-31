import settings
import os
import operations.operations as op


def check_folder(folderpath, replica):
    print (f"checking items in {folderpath}...")
    if os.path.isdir(folderpath):
        return os.listdir(folderpath)
    else:
        if replica:
            print (f"creating {folderpath} directory...")
            os.mkdir(folderpath)
            return None
        else:
            raise NotADirectoryError("Folder not found.")
        

def check_items(source, replica):
    copy = list(set(source) - set(replica))
    delete = list(set(replica) - set(source))
    flag = False

    if copy:
        flag = op.copy(source, replica, copy, all=False)
        while flag:
            flag = op.copy(source, replica, copy, all=False)
        flag = False

    if delete:
        flag = op.delete(source, replica, delete, all=False)
        while flag:
            flag = op.delete(source, replica, delete, all=False)


def compare_folder_items(source, replica):
    if not source["items"] or source["items"] is None:
        if not replica["items"] or replica["items"] is None:
            print ("Source items match replica items. No operation needed.") 
        else: 
            print ("Source items unmatch replica items. Deletion operation needed...")
            op.delete(source, replica, source["items"], all=True)
    else: 
        if not replica["items"] or replica["items"] is None:
            print ("Source items unmatch replica items. Copy operation needed.")
            op.copy(source, replica, source["items"], all=True)
        else: 
            if set(source["items"]) == set(replica["items"]):
                print ("Source items match replica items. No operation needed...")
            else:
                print ("Source items unmatch replica items. Checking individual files...")
                check_items(source, replica)



def run_sync():
    source_pathname = f"{settings.source_folder_path}/{settings.source_folder_name}"
    replica_pathname = f"{settings.replica_folder_path}/{settings.replica_folder_name}"

    source = {"path": source_pathname,
              "items": check_folder(source_pathname, False)}
    replica= {"path": replica_pathname,
              "items": check_folder(replica_pathname, True)}

    # print (source["items"])
    # print (replica["items"])

    compare_folder_items(source, replica)





