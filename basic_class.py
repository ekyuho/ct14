#################################
balance = 0

def deposit(v):
    global balance
    balance += v
    return balance

def draw(v):
    global balance
    if balance < v:
        return -1

    balance -= v
    return balance

print(deposit(1000))
print(draw(500))

##################################
class Account:
    def __init__(self):
        self.balance = 0

    def deposit(self, v):
        self.balance += v
        return self.balance

    def draw(self, v):
        if self.balance < v:
            return -1

        self.balance -= v
        return self.balance

acc = Account()
print(acc.deposit(1000))
print(acc.draw(500))

