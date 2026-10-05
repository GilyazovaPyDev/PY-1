class Stack:
    def __init__(self, data=[], limit=10000000):
        self.data = data
        self.limit = limit

    def push(self, obj):
        if self.limit and len(self.data) < self.limit:
            self.data.append(obj)
        else:
            return f'Стек уже заполнен!'

    def pop(self):
        if self.data:
            return self.data.pop()
        else:
            return None

    def __len__(self):
        return len(self.data)

    def empty(self):
        return len(self.data) == 0

    def __str__(self):
        return f'{self.data}'


s1 = Stack(limit=2)
s1.push(5)
s1.push(6)
print(s1.push(7))
print(s1)
print(s1.empty())
print(s1.pop())
print(s1)
