# built in
import math

# custom module
import my_utils

# custom package
from my_package import basic_math, advanced_math

# 3rd party package from pip
import requests


# built in
print("built in:")
print("Square root of 49:", math.sqrt(49))
print()


# custom module
print("Custom module:")
my_utils.print_with_date("Python")
print()


# custom package
print("Custom package:")
print("Add 7 + 2:", basic_math.add(7, 2))
print("2 to the power of 3:", advanced_math.power(2, 3))
print()


# third party module from pip
print("From pip:")
response = requests.get("https://api.github.com")
print("Status Code:", response.status_code)
print("Content Type:", response.headers.get("Content-Type"))
