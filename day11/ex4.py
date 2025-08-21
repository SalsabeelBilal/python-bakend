from datetime import datetime
import pytz

def convert_timezone(time_str: str, from_tz: str, to_tz: str) -> str:
    
    naive_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    
   
    source_timezone = pytz.timezone(from_tz)
    localized_time = source_timezone.localize(naive_time)
    
 
    target_timezone = pytz.timezone(to_tz)
    converted_time = localized_time.astimezone(target_timezone)
    
    return converted_time.strftime("%Y-%m-%d %H:%M:%S %Z%z")


# Example 
print(convert_timezone("2023-10-05 14:30:00", "US/Eastern", "UTC"))
print(convert_timezone("2023-10-05 14:30:00", "UTC", "Asia/Tokyo"))
