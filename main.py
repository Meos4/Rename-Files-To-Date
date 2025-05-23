import os
import sys
import time

def creation_time_formatted(file_path):
    stats = os.stat(file_path)
    return time.strftime("%d-%m-%Y %H %M %S", time.localtime(stats.st_mtime))

def rename_file_path(old, new):
    try:
        os.rename(old, new)
    except Exception as e:
        print(f"Error: {e}")

def files_in_directory(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

if len(sys.argv) < 2:
    sys.exit("No directory provided")

directory = os.path.join(sys.argv[1], '')

if not os.path.isdir(directory):
    sys.exit("Not a directory")

for file in files_in_directory(directory):
    name, extension = os.path.splitext(file)
    rename_file_path(directory + file, directory + creation_time_formatted(directory + file) + extension)