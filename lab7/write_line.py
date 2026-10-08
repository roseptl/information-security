from datetime import datetime
import os

file_path = "/Users/leedaria/lab7/log.txt"

if os.path.exists(file_path):
    with open(file_path, "r") as file:
        count = len(file.readlines())
else:
    count = 0

with open(file_path, "a") as file:
    count += 1
    file.write(f"Run #{count} | Time: {datetime.now()}\n")
