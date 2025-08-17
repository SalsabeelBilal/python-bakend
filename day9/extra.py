def multiplier(base):
    def multiply(value):
        if base == 0:
            return value * value
        return base * value
    return multiply

doubler = multiplier(2)
tripler = multiplier(3)
squarer = multiplier(0)

print("Doubler:", doubler(5))   # 10
print("Tripler:", tripler(5))   # 15
print("Squarer:", squarer(5))   # 25
