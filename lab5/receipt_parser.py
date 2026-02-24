import re

with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

prices = re.findall(r'\d[\d ]*,\d{2}', text)
numbers = [float(p.replace(' ', '').replace(',', '.')) for p in prices]

products = re.findall(r'\d+\.\n(.+)', text)

total = sum(numbers)

datetime = re.search(r'\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2}', text)
datetime = datetime.group() if datetime else ""

payment = re.search(r'Банковская карта', text)
payment = "Bank card" if payment else ""

print("Products:")
for p in products:
    print(p)

print("Prices:")
for n in numbers:
    print(n)

print("Total:", total)
print("DateTime:", datetime)
print("Payment:", payment)