import settings
from content_comparision import content_comparision, folder_content

def analyse_content(source, replica):
    folder_content.get_structure(source)
    folder_content.get_structure(replica)

    # print (f"source: {source}")
    # print (f"replica: {replica}")

    operations = {
        "items": {
            "create": [],
            "delete": [],
            "copy_content": [],
            "keep": []
        },
        "folders": {
            "create": [],
            "delete": [],
            "keep": []
        }
        
    }
    
    content_comparision.compare_structures(source, replica, operations)

    return operations

def run_sync():
    source_pathname = f"{settings.source_folder_path}/{settings.source_folder_name}"
    replica_pathname = f"{settings.replica_folder_path}/{settings.replica_folder_name}"

    source = {
        "path": source_pathname,
        "items": folder_content.get_folder_content(source_pathname, False)
    }
    replica = {
        "path": replica_pathname,
        "items": folder_content.get_folder_content(replica_pathname, True)
    }

    operations = analyse_content(source, replica)

    print (operations)