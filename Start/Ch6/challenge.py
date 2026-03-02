# Python code​​​​​​‌‌‌‌​‌​​​​‌​‌‌‌​‌​​‌​‌​‌‌ below
# Use print("messages...") to debug your solution.
import os
from os import path

show_expected_result = False
show_hints = False

def file_info():
    subdir = 'deps'
    # subdir = '.'
    size = 0
    files = os.listdir(subdir)
    for f in files:
        if f[-4:] == '.txt':
            size += os.path.getsize(subdir+'/'+f)
    return size/1024

print(file_info())
