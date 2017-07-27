# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 09:23:27 2016

@author: ngj
"""

import os
import time
from os import scandir

BYTES_IN_GIGABYTE = 2**30

def get_folder_size(filepath, level):
    size = os.path.getsize(filepath)
    try:        
        for entry in scandir(filepath):
            item_path = os.path.join(filepath, entry.name)
            if not entry.name.startswith('.') and entry.is_file():
            ## Get size of all files        
                size += entry.stat().st_size
            elif not entry.name.startswith('.') and entry.is_dir():
            ## Enter recursive call    
                level += 1             
                size += get_folder_size(item_path, level)
            if level == 2 and not entry.is_file():
                print(entry.name + ' = ' + format(size/BYTES_IN_GIGABYTE, '.5f'))
                level = 1
                size= 0                    
    except:
        print('Cannot open - ' + filepath)
    return size

def main():
    t = time.time()      
    get_folder_size('T:\\', 1)
    print('Duration = ' + format(time.time() - t, '.5f') + 's')
    
if __name__ == '__main__':
    main()

