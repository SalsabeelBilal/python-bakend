class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.__price = price
        self.quantity = quantity

    def apply_discount(self, percent):
        if 0 < percent < 100:
            discount_amount = self.__price * (percent / 100)
            self.__price -= discount_amount
            print(f"Discount applied. New price: ${self.__price:.2f}")
        else:
            print("Invalid discount percent.")

    def restock(self, amount):
        if amount > 0:
            self.quantity += amount
            print(f"Restocked {amount} units. New quantity: {self.quantity}")
        else:
            print("Invalid restock amount.")

    
    def __add__(self, other):
        if isinstance(other, Product) and self.product_id == other.product_id:
            return Product(self.product_id, self.name, self.__price, self.quantity + other.quantity)
        raise ValueError("Can only add quantities of the same product.")

    def __call__(self):
        print(f"{self.name} (ID: {self.product_id}) - Price: ${self.__price:.2f}, Quantity: {self.quantity}")

    def _get_price(self):
        return self.__price  


class DigitalProduct(Product):
    def __init__(self, product_id, name, price, quantity, file_size):
        super().__init__(product_id, name, price, quantity)
        self.file_size = file_size

    def apply_discount(self, percent):
        if percent > 20:
            print("Max discount for digital products is 20%.")
        else:
            super().apply_discount(percent)


class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, quantity, weight):
        super().__init__(product_id, name, price, quantity)
        self.weight = weight

    def apply_discount(self, percent):
        old_price = self._get_price()
        discount_amount = old_price * (percent / 100)
        new_price = old_price - discount_amount
        if new_price < 5:
            print("Cannot reduce price below $5 for physical products.")
        else:
            super().apply_discount(percent)


if __name__ == "__main__":
    
    ebook = DigitalProduct("D001", "Python Guide", 50, 10, "5MB")
    laptop = PhysicalProduct("P001", "Laptop", 1200, 5, "2kg")


    ebook()
    laptop()

  
    ebook.apply_discount(15)   
    ebook.apply_discount(30)   

    laptop.apply_discount(50)  
    laptop.apply_discount(10)  
    
    ebook.restock(5)

    
    ebook_extra = DigitalProduct("D001", "Python Guide", 50, 3, "5MB")
    combined_ebook = ebook + ebook_extra
    combined_ebook()

    
    try:
        combined = ebook + laptop
    except ValueError as e:
        print(e)
