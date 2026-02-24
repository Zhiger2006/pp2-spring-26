import re

s = input()
print(" ".join(re.findall(r"[A-Z][^A-Z]*", s)).strip())