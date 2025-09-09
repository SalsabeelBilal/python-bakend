import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

API_KEY = "your_api_key"
CITY = "New York"

url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(url)
data = response.json()

weather_report = f"""
Weather Report for {CITY}:

- Condition: {data['weather'][0]['description']}
- Temperature: {data['main']['temp']}°C
- Feels Like: {data['main']['feels_like']}°C
- Humidity: {data['main']['humidity']}%
- Wind Speed: {data['wind']['speed']} m/s
"""

filename = "weather_report.txt"
with open(filename, "w") as file:
    file.write(weather_report)

sender = "you@example.com"
receiver = "friend@example.com"
password = "your_password"

msg = MIMEMultipart()
msg["From"] = sender
msg["To"] = receiver
msg["Subject"] = f"Weather Report - {CITY}"

msg.attach(MIMEText("Hi,\n\nPlease find attached the latest weather report.\n\nRegards,", "plain"))

with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename={filename}")
    msg.attach(part)

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender, password)
    server.send_message(msg)

print("Weather report emailed successfully!")
