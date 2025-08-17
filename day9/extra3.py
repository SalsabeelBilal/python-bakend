def validate_positive(func):
    def wrapper(*args, **kwargs):
        for arg in list(args) + list(kwargs.values()):
            if not isinstance(arg, (int, float)):
                raise ValueError(f"Invalid argument {arg}: must be a number")
            if arg <= 0:
                raise ValueError(f"Invalid argument {arg}: must be positive")
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def add(a, b):
    return a + b

@validate_positive
def multiply(x, y, z=1):
    return x * y * z

print(add(5, 3))         
print(multiply(2, 4, z=3))