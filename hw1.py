class BankCard:
    def __init__(self, owner: str, balance: int = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: int):
        if amount > 0:
            self.balance += amount
            print(f"Карта {self.owner}: успешно пополнено на {amount}. Текущий баланс: {self.balance}")
        else:
            print("Сумма пополнения должна быть положительной!")

    def pay(self, amount: int):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Карта {self.owner}: оплата на сумму {amount} прошла успешно. Остаток: {self.balance}")
        else:
            print(f"Карта {self.owner}: Недостаточно средств для оплаты {amount}! Баланс: {self.balance}")

    def info(self):
        print(f"Владелец карты: {self.owner}, Текущий баланс: {self.balance}")


card1 = BankCard("Азамат", 5000)
card2 = BankCard("Айпери", 3000)

card1.deposit(2000)
card1.pay(1500)
card2.pay(500)
card1.info()
card2.info()