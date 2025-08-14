class Car:
    wheels = 4  
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0  

    def accelerate(self, increment):
        self.speed += increment
        print(f"{self.brand} {self.model} accelerated to {self.speed} km/h")

    def brake(self, decrement):
        self.speed = max(0, self.speed - decrement)
        print(f"{self.brand} {self.model} slowed down to {self.speed} km/h")


if __name__ == "__main__":
    car1 = Car("Toyota", "Corolla", 2022)
    car1.accelerate(30)
    car1.brake(10)
