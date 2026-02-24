import re

s = input().strip()
parts = re.split(r"_+", s)
print(parts[0] + "".join(w.capitalize() for w in parts[1:]) if parts else "")