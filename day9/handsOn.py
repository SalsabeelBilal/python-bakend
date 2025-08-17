import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = end - start
        print(f"{func.__name__} took {duration:.5f} seconds")
        return result, duration
    return wrapper

@measure_time
def compute_sum(n):
    return sum(range(n))

def write_to_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)

if __name__ == "__main__":
    result, duration = compute_sum(5_000_000)
    write_to_file("results.txt", f"Result: {result}\nExecution Time: {duration:.5f} seconds\n")
    print("Computation result and execution time saved to results.txt")
