import re

def extract_dates(text: str):

    pattern = r'\b\d{2}[-/]\d{2}[-/]\d{4}\b'
    


    return re.findall(pattern, text)


# Example 
sample_text = """
Today's date is 21-08-2025.
My birthday is on 23/08/2004.
Invalid example: 2025-08-21 (should not match).
Another date: 01/01/2000.
"""

print(extract_dates(sample_text))
