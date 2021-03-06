# Organize invoices in a new folder and flag if file size is > 5MB

import glob
import shutil 
import os
from pathlib import Path

path = '/Users/Admin/invoice/'

# Check whether the specified path exists or not
isExist = os.path.exists(path)

# Create a new directory if it does not already exist
if not isExist:
  os.makedirs(path)
  print("New directory created.")

src_folder = "/Users/Admin/Downloads/"
dst_folder = "/Users/Admin/invoice/"

# Move file if name starts with string 'invoice'
pattern = src_folder + "/invoice*"
for file in glob.iglob(pattern, recursive=True):

    # Extract file name form file path
    file_name = os.path.basename(file)
    shutil.move(file, dst_folder + file_name)
    print('Moved:', file)

# Find files that are > 5MB
dir_path = Path('/Users/Admin/invoice/')

F_LIST = list(x for x in dir_path.rglob('*.*') if x.is_file() and os.path.getsize(x) >= 5000000)

for f in F_LIST:
    print(f.parts[-1] + " ===> " + "Size = " + str(format(os.path.getsize(f), ',d')))
