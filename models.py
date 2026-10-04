class Card:
    balance: float = 1000000
    def __init__(self, num, owner):
        self.num = num
        self.owner = owner
        self._count = 0

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value

    @staticmethod
    def deposit(self, amount):
        self.balance += amount

    def credit(self):
        if Card.balance > 0:
            self.count += 1
            Card.balance -= 1
            return True
        else:
            print(f'На карте {self.num} недостаточно средств')


    def __str__(self):
        return (f'\nКарта: {self.num}\n'
                f'Выдана: {self.owner}\n'
                f'Кол-во операций: {self._count}')
