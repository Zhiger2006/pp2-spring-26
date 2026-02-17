from datetime import datetime, timedelta

now = datetime.now()
new_date = now - timedelta(days=5)
print(new_date)
