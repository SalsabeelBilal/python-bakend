from datetime import datetime, timedelta

def time_until_next_birthday():
   
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    
   
    today = datetime.now()
    
    
    current_year = today.year
    next_birthday = datetime(current_year, birthdate.month, birthdate.day)
    
   
    if next_birthday < today:
        next_birthday = datetime(current_year + 1, birthdate.month, birthdate.day)
    
    
    time_remaining = next_birthday - today
    
    
    days = time_remaining.days
    hours, remainder = divmod(time_remaining.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    
    print(f"⏳ Time until your next birthday: {days} days, {hours} hours, {minutes} minutes")


time_until_next_birthday()
