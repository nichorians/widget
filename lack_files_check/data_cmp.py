import os
from pathlib import Path
import logging
import time

def compare_files(dir1, dir2, log_file='differences.log', ignore_ext='.avi'):
    #dir1 = Path(dir1)
    #dir2 = Path(dir2)
    
    #directories = [p for p in dir1.glob('*') if p.is_dir()]
    directories = [p for p in sorted(os.listdir(dir1)) if os.path.isdir(dir1)]
    logging.basicConfig(filename=log_file,level=logging.INFO)
    logging.info(time.time())
    
    for dir in directories:
        dir_ = os.path.join(dir1,dir)
        video_directories = [v for v in sorted(os.listdir(dir_)) if os.path.isdir(os.path.join(dir_,v))]
        
        for dir__ in video_directories:
            v_dir = os.path.join(dir_,dir__)
            #files = os.listdir(v_dir)
            #max_file = max(files)
            files = sorted(os.listdir(v_dir))[:-1]
            
            #if max_file:
            #    files_without_max = [file for file in files if file != max_file]
            #else:
            #    print(f"No files were found or there's only one file in {str(v_dir)}.")
                
            #for file in files_without_max:
            for file in files:
                file = os.path.join(v_dir,file)
                found_file = file.replace('jpg','png').replace('frames','mask')
                if not os.path.exists(found_file):
                    logging.info(found_file)
                    
                
# Example usage
dir1 = '/data12t/ucf101/frames/'
dir2 = '/data12t/ucf101/mask/'
log_name = 'frames_mask2.log'
compare_files(dir1, dir2, log_name)
