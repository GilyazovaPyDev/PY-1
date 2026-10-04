from threading import Thread, Lock

from models import Card

class Transaction(Thread):
    lock = Lock()
    def __init__(self, amount, card: Card):
        super().__init__()
        self.amount = amount
        self._card = card
    @property
    def card(self):
        return self._card

    def run(self):
        print(f"Начало транзакций => {self.card}")
        for k in range(self.amount):
            with Transaction.lock:
                if not self.card.credit():
                    break
        print(f'Конец транзакций => {self.card}')

