import re
from datetime import datetime

def parse_log_timestamps(log: str):
    
    pattern = r"\[(\d{2}/[A-Za-z]{3}/\d{4}:\d{2}:\d{2}:\d{2} [+-]\d{4})\]"
    
   
    matches = re.findall(pattern, log)
    
    converted_times = []
    for ts in matches:
     
        dt = datetime.strptime(ts, "%d/%b/%Y:%H:%M:%S %z")
        
       
        utc_time = dt.astimezone(datetime.utcnow().astimezone().tzinfo)
        converted_times.append(utc_time.strftime("%Y-%m-%d %H:%M:%S"))
    
    return converted_times


# Example
log_data = """
127.0.0.1 - - [21/Aug/2025:14:32:10 +0000] "GET /index.html HTTP/1.1" 200 1024
192.168.1.1 - - [20/Aug/2025:23:59:59 +0000] "POST /login HTTP/1.1" 302 512
"""

print(parse_log_timestamps(log_data))
