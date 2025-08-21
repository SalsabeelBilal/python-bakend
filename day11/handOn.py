import re
from datetime import datetime
import pytz



phone = "+962-777-123456"
pattern = r"\+962-\d{3}-\d{6}"

if re.match(pattern, phone):
    print("Valid Jordanian phone number")
else:
    print("Invalid phone number")


text = "Order #123 will ship on 2025-08-21"
numbers = re.findall(r"\d+", text)
print("Extracted numbers:", numbers)

utc = pytz.utc
now = datetime.now(utc)

london = pytz.timezone("Europe/London")
tokyo = pytz.timezone("Asia/Tokyo")
amman = pytz.timezone("Asia/Amman")

print("UTC:", now.strftime("%Y-%m-%d %H:%M:%S"))
print("London:", now.astimezone(london).strftime("%Y-%m-%d %H:%M:%S"))
print("Tokyo:", now.astimezone(tokyo).strftime("%Y-%m-%d %H:%M:%S"))
print("Amman:", now.astimezone(amman).strftime("%Y-%m-%d %H:%M:%S"))
