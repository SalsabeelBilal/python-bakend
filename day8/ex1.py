class Account:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def display_balance(self):
        print(f"Account {self.account_number} balance: {self.__balance}")

    
    def __str__(self):
        return f"Account[{self.account_number}] - Holder: {self.account_holder}"

    def __eq__(self, other):
        return self.account_number == other.account_number


class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        
        if amount > 0:
            if self._Account__balance - amount >= 100:
                self._Account__balance -= amount
                print(f"Withdrew {amount}. New balance: {self._Account__balance}")
            else:
                print("Cannot withdraw: Minimum balance of 100 must be maintained.")
        else:
            print("Withdrawal amount must be positive.")


class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        
        if amount > 0:
            if self._Account__balance - amount >= -self.overdraft_limit:
                self._Account__balance -= amount
                print(f"Withdrew {amount}. New balance: {self._Account__balance}")
            else:
                print("Cannot withdraw: Overdraft limit exceeded.")
        else:
            print("Withdrawal amount must be positive.")



if __name__ == "__main__":
    
    savings = SavingsAccount("SA001", "Alice", 500, 0.03)
    checking = CheckingAccount("CA001", "Bob", 300, 200)

    
    print(savings)
    print(checking)

    
    savings.deposit(100)
    savings.withdraw(450)  
    savings.withdraw(300)  

    checking.withdraw(450) 
    checking.withdraw(200) 

    
    another_savings = SavingsAccount("SA001", "Alice", 700, 0.03)
    print("Accounts equal?", savings == another_savings)

    
    savings.display_balance()
    checking.display_balance()
