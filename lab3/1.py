import re
import json
word = '{"Ivan":"123@gmail.com","Serega":"lol_mail","Ayan":"ayan@mail.ru"}'
data = json.loads(word)
for x,xx in data.items():
    if re.search(r"\b[\w\.-]+@[\w\.-]+\.\w+\b", xx):
        print(xx)