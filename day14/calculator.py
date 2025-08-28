
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class Calculator:
    def __init__(self):
        self.memory = 0

    def store(self, value):
        self.memory = value

    def recall(self):
        return self.memory
