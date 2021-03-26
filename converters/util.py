import os.path


def file_exists( file_path ):
    
    if not os.path.exists(file_path):
        return False
    
    if os.path.getsize(file_path) == 0:
        return False
    
    return True

