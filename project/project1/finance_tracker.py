import json
from datetime import datetime

DATA_FILE = "transactions.json"

class Transaction:
    def __init__(self, amount, category, date, type):
        self.amount = amount
        self.category = category
        self.date = date
        self.type = type

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "type": self.type
        }

class FinanceTracker:
    def __init__(self):
        self.transactions = []
        self.load_data()

    def load_data(self):
        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                self.transactions = [Transaction(**t) for t in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.transactions = []

    def save_data(self):
        with open(DATA_FILE, "w") as f:
            json.dump([t.to_dict() for t in self.transactions], f, indent=4)

    def add_transaction(self, amount, category, t_type):
        try:
            amount = float(amount)
            date = datetime.now().strftime("%Y-%m-%d")
            t = Transaction(amount, category, date, t_type)
            self.transactions.append(t)
            self.save_data()
            print("Transaction added successfully!")
        except ValueError:
            print("Invalid amount. Please enter a number.")

    def view_transactions(self):
        if not self.transactions:
            print("No transactions recorded.")
            return
        for t in self.transactions:
            print(f"{t.date} | {t.type.upper():7} | {t.category}: ${t.amount:.2f}")

    def summary(self):
        income = sum(t.amount for t in self.transactions if t.type == "income")
        expenses = sum(t.amount for t in self.transactions if t.type == "expense")
        balance = income - expenses
        print(f"Total Income: ${income:.2f}")
        print(f"Total Expenses: ${expenses:.2f}")
        print(f"Net Balance: ${balance:.2f}")

def main():
    tracker = FinanceTracker()
    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. View Summary")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            amt = input("Enter amount: ")
            cat = input("Enter category: ")
            tracker.add_transaction(amt, cat, "income")
        elif choice == "2":
            amt = input("Enter amount: ")
            cat = input("Enter category: ")
            tracker.add_transaction(amt, cat, "expense")
        elif choice == "3":
            tracker.view_transactions()
        elif choice == "4":
            tracker.summary()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
