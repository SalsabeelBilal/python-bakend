import re
from datetime import datetime
import pytz

def validate_email(email: str) -> bool:
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

email = "student@example.com"
if validate_email(email):
    print("Valid email!")
else:
    print("Invalid email!")

timezones = ["America/New_York", "Europe/London", "Asia/Amman"]
now = datetime.now(pytz.utc)

print("\nCurrent Times:")
for tz in timezones:
    local_time = now.astimezone(pytz.timezone(tz))
    print(f"{tz}: {local_time.strftime('%Y-%m-%d %H:%M:%S')}")
