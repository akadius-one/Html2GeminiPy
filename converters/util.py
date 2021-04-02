import os.path
import time


def file_exists( file_path ):
    
    if not os.path.exists(file_path):
        return False
    
    if os.path.getsize(file_path) == 0:
        return False
    
    return True


def timer( tic=None, name=None ) :
    
    toc = time.perf_counter()
    if tic is None:
        # Special case to start a timer!
        return toc
    
    print(f"{name} time {toc - tic:0.4f} seconds")
    return toc


def pause(sleep_time):
    print(f"Pausing {sleep_time} seconds")
    time.sleep(sleep_time)

