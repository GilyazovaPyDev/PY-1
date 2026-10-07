class Box:
    def __init__(self, name):
        self.name = name
        self.next_box = None

    def __str__(self):
        return f'{self.name} -> {self.next_box}'


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_box = None
        self.previous_box = None

    def push(self, cat_name):
        current_box = Box(cat_name)
        if self.head == None:
            self.head = current_box
            self.last_box = current_box
            return

        self.last_box.next_box = current_box
        self.last_box = current_box

    def pop_left(self):
        if self.head == None:
            return 'Queue is empty'
        elif self.head.next_box == None:
            obj = self.head
            self.head = None
            return obj
        else:
            obj = self.head
            self.head = self.head.next_box
            obj.next_box = None
            return obj

    def entry(self, cat_name):
        if self.head == None:
            return False
        current_box = self.head

        while (current_box is self.head or current_box.next_box != None
                or current_box.name == cat_name):
            if current_box.name == cat_name:
                return True
            self.previous_box = current_box
            current_box = current_box.next_box
        return False


    def __str__(self):
        return f'{self.head}'


ll = LinkedList()
ll.push('Barsk')
ll.push('Alisa')
ll.push('Murchik')
ll.push('Atosik')
# print(ll)
# print(ll.pop_left())
print(ll)
print(ll.entry('Atosik'))
