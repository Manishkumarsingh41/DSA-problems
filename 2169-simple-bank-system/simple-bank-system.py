class Bank:
    def __init__(self, balance):
        self.b = balance
        self.n = len(balance)

    def transfer(self, a1, a2, money):
        if 1 <= a1 <= self.n and 1 <= a2 <= self.n and self.b[a1-1] >= money:
            self.b[a1-1] -= money
            self.b[a2-1] += money
            return True
        return False

    def deposit(self, a, money):
        if 1 <= a <= self.n:
            self.b[a-1] += money
            return True
        return False

    def withdraw(self, a, money):
        if 1 <= a <= self.n and self.b[a-1] >= money:
            self.b[a-1] -= money
            return True
        return False
