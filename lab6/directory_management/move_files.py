import shutil
import os

os.makedirs("dir1", exist_ok=True)

with open("move.txt", "w") as f:
    f.write("data")

shutil.move("move.txt", "dir1/move.txt")
shutil.copy("dir1/move.txt", "copy.txt")