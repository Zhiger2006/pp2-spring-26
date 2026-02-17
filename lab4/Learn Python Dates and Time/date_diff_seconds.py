from datetime import datetime

d1 = datetime(2026,2,17,12,0,0)
d2 = datetime(2026,2,18,14,30,0)
diff = d2 - d1
print(diff.total_seconds())
