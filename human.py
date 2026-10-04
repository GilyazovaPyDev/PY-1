class Human:
    def __init__(self, name, *essence, magic=0):
        self.name = name
        self.essence = list(essence)
        self.magic = magic

    def change_name(self, name):
        self.name += ' ' + name

    def __add__(self, line):
        self.essence.append(line)
        self.magic += len(line)//4
        return self

    def __sub__(self, other):
        name = self.name[:3] + other.name[-3:].capitalize()
        essence = list(set(self.essence) - set(other.essence))
        essence.sort()
        return Human(name, *essence,  magic = 0)

    def __call__(self, num):
        return self.essence[:num]

    def __eq__(self, other):
        if self.magic == other.magic:
            if len(self.essence) == len(other.essence):
                if self.name == other.name:
                    return True
        return False

    def __gt__(self, other):
        if self.magic > other.magic:
            return True
        elif self.magic == other.magic and len(self.essence) > len(other.essence):
            return True
        elif self.name > other.name and len(self.essence) == len(other.essence):
            return True
        return False

    def __lt__(self, other):
        if self.magic < other.magic:
            return True
        if self.magic == other.magic and len(self.essence) < len(other.essence):
            return True
        elif self.name < other.name and len(self.essence) == len(other.essence):
            return True
        return False

    def __le__(self, other):
        if self.magic <= other.magic:
            return True
        else:
            return False

    def __ne__(self, other) -> bool:
        if (self.magic != other.magic or len(self.essence) != len(other.essence)
            or self.name != other.name):
            return True
        return False

    def __str__(self):
        return f'Человек по имени {self.name} ({", ".join(self.essence)}, уровень магии - {self.magic})'


# hm = Human('Illmarrannen', 'Forgiving', 'Forgiven', magic=2)
# hm.change_name('Rual')
# id_hm = id(hm)
# hm += 'Skyman'
# print(hm, hm(2), sep='\n')
# print(id_hm == id(hm))

hm = Human('Marran', 'Hanger', 'Stick', 'Wizzard', magic=10)
hm1 = Human('Lart',  'Wizzard')
print(hm, hm1, sep='\n')
print(hm > hm1, hm <= hm1, hm == hm1)
hm2 = hm - hm1
print(hm2)
print(hm2 > hm1, hm <= hm, hm2 != hm)


