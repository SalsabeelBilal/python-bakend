
import re

def validate_email(email: str) -> bool:
 
    pattern = r'^[A-Za-z0-9._-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,4}$'
    
    return re.match(pattern, email) is not None


# Example tests
print(validate_email("john.doe@example.com"))    #True
print(validate_email("user_name-123@domain.net")) #True
print(validate_email("invalid@domain"))           #False
print(validate_email("wrong@domain.toolong"))     #False
print(validate_email("bad@@domain.com"))          #False
