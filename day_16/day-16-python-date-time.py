# Day 16 - Python Datetime

from datetime import datetime

now = datetime.now()
print(f"Day: {now.day}")
print(f"Month: {now.month}")
print(f"Year: {now.year}")
print(f"Hour: {now.hour}")
print(f"Minute: {now.minute}")
print(f"Timestamp: {now.timestamp()}")


print("Formatted:", now.strftime("%m/%d/%Y, %H:%M:%S"))

today = "5 December, 2019"
print(now.strptime(today, "%d %B, %Y"))

new_year = datetime(2026, 1, 1)
time_diff = new_year - now
print(time_diff)

past = datetime(year=1970, month=1, day=1)
result = now - past
print(result)

