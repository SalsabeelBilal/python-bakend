import time

def multiplier(base):
    def multiply(value):
        return value * value if base == 0 else base * value
    return multiply

doubler = multiplier(2)
tripler = multiplier(3)
squarer = multiplier(0)


print("Doubler:", doubler(5))
print("Tripler:", tripler(5))
print("Squarer:", squarer(5))
print("-" * 40)

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.5f} seconds")
        return result
    return wrapper

@measure_time
def slow_function():
    return sum(range(5_000_000))

print("Decorator Example:")
slow_function()
print("-" * 40)

def write_to_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)

print("Context Manager Example:")
write_to_file("output.txt", "Hello from context manager!\n")
print("Data written to output.txt")
print("-" * 40)

class MyContext:
    def __enter__(self):
        print("Entering custom context...")
        return "Resource ready"
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting custom context...")

print("Custom Context Manager Example:")
with MyContext() as resource:
    print(resource)
print("-" * 40)

def call_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"{func.__name__} has been called {wrapper.calls} times")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@call_counter
def greet(name):
    print(f"Hello, {name}!")

print("Call Counter Decorator:")
greet("Alice")
greet("Bob")
greet("Charlie")
print(f"Final call count: {greet.calls}")
