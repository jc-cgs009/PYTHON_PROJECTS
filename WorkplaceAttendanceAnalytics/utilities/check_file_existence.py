import os


def file_exist_or_not(file_path):
    # folder_path = '/path/to/folder'
    # file_name = 'example.txt'
    #
    # # Create the full file path
    # file_path = os.path.join(folder_path, file_name)

    # Check if the file exists
    if os.path.exists(file_path):
        return True
    else:
        return False
