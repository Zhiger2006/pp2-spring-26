import re
person = """
    ID:8712111578454,
    Name:Kairat,
    Gender:Male
"""
m = re.findall(r"\d+", person)
print(*m)


