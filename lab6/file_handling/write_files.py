with open("sample.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")

with open("sample.txt", "a") as f:
    f.write("Appended line\n")

with open("sample.txt", "r") as f:
    print(f.read())