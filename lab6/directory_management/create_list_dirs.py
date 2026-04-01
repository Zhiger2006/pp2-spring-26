import os

os.makedirs("dir1/dir2", exist_ok=True)

for item in os.listdir("dir1"):
    print(item)

for file in os.listdir("."):
    if file.endswith(".txt"):
        print(file)