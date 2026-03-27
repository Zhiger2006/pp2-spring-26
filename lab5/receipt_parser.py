import re
import json

with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

def to_float_ru(s: str) -> float:
    s = s.replace(" ", "").replace(",", ".")
    return float(s)

date_time = None
m = re.search(r"\b\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2}\b", text)
if m:
    date_time = m.group(0)

payment_method = None
m = re.search(r"\b(Наличные|Банковская карта)\b", text)
if m:
    payment_method = m.group(1)

receipt_total = None
m = re.search(r"ИТОГО:\s*\n\s*([\d\s]+,\d{2})", text)
if m:
    receipt_total = to_float_ru(m.group(1))

products = []
for m in re.finditer(r"^\d+\.\s*\n(.+)$", text, flags=re.MULTILINE):
    products.append(m.group(1))

item_prices = []
for m in re.finditer(r"\n([\d\s]+,\d{2})\nСтоимость", text):
    item_prices.append(to_float_ru(m.group(1)))

calculated_sum = sum(item_prices)

data = {
    "date_time": date_time,
    "payment_method": payment_method,
    "receipt_total": receipt_total,
    "calculated_sum": calculated_sum,
    "products": products
}

print(json.dumps(data, indent=4, ensure_ascii=False))