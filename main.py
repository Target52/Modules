__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os, shutil, zipfile, glob, fileinput

folder = os.getcwd()
directory = os.path.join(folder, 'cache')
zip_file_path = os.path.join(folder, 'data.zip')

def clean_cache():
    if 'cache' in os.listdir(folder):
        filelist = [ f for f in os.listdir(directory) ]
        for f in filelist:
            os.remove(os.path.join(directory, f))
    else:
        os.mkdir(directory)

clean_cache()

def cache_zip(zip_file_path, cache_dir_path):
    with zipfile.ZipFile(zip_file_path, 'r',) as zip_ref:
        zip_ref.extractall(cache_dir_path)

cache_zip(zip_file_path, directory)

def cached_files():
    list_files = []
    with os.scandir(directory) as listOfEntries:
        for entry in listOfEntries:
            if entry.is_file():
                result = os.path.abspath(os.path.join(directory, entry))
                list_files.append(result)     
    return list_files

def find_password(files):
        for line in fileinput.input(files):
            if "password" in line:
                password_line = line
                password = password_line.split(": ")[-1]
            else:
                continue
        return password

print("The password is: ")
print(find_password(cached_files()))
