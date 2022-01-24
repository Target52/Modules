__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os, shutil, zipfile

folder = os.getcwd()
directory = folder + '/cache'
zip_file_path = folder + '/data.zip'

def clean_cache():
    if 'cache' in os.listdir(folder):
        shutil.rmtree(directory)
        os.mkdir(directory)
    else:
        os.mkdir(directory)

def cache_zip(zip_file_path, cache_dir_path):
    with zipfile.ZipFile(zip_file_path, 'r',) as zip_ref:
        zip_ref.extractall(cache_dir_path)


def cached_files():
    list_files = []
    with os.scandir(directory) as listOfEntries:
        for entry in listOfEntries:
            if entry.is_file():
                result = os.path.join(directory, entry.name)
                list_files.append(result)
                
    return list_files

def find_password(cached_files):
    files = cached_files
    for file in files:
        with open(file, 'r') as f:
            read_line = f.read().split("\n")
            for line in read_line:
                if "password" in line:
                    password_line = line
                    password = password_line.split(": ")[-1]
                else:
                    continue
    return password

print("The password is: ")
print(find_password(cached_files()))
