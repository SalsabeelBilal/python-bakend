import sqlite3

# ---------------- Database Setup ----------------
DB_NAME = "store.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        price REAL NOT NULL,
                        stock INTEGER NOT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# ---------------- Classes ----------------
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self._stock = stock

    def __str__(self):
        return f"{self.name} (${self.price}) - Stock: {self._stock}"

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        if product._stock >= quantity:
            self.items.append((product, quantity))
            product._stock -= quantity
            print(f"Added {quantity} x {product.name} to cart.")
        else:
            print(f"Not enough stock for {product.name}!")

    def view_cart(self):
        if not self.items:
            print("Cart is empty.")
            return
        for product, qty in self.items:
            print(f"{product.name} x{qty} = ${product.price * qty:.2f}")
        print(f"Total: ${self.total_price():.2f}")

    def total_price(self):
        return sum(product.price * qty for product, qty in self.items)

    def checkout(self):
        print("Checkout complete!")
        self.items.clear()

# ---------------- Demo ----------------
def demo():
    # Initialize DB
    init_db()

    # Create some products
    p1 = Product("Laptop", 1200, 5)
    p2 = Product("Phone", 800, 10)

    # Shopping process
    cart = ShoppingCart()
    cart.add_product(p1, 1)
    cart.add_product(p2, 2)
    cart.view_cart()
    cart.checkout()

if __name__ == "__main__":
    demo()
