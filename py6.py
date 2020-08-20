class Goose():
    voice = 'gagagaga'
    type_an = 'Гусь'

    def feed(self):
        print('Животное сыто')

    def eggs(self):
        print('Яйца собраны')

    def sound(self):
        print(f"Животное издает звук  {self.voice}")

    def __init__(self):
        self.name = ['Серый', 'Белый']
        self.weight = 3

class Cow():
    voice = 'muuuuuuu'
    type_an = 'Корова'

    def feed(self):
        print('Животное сыто')

    def milk(self):
        print('Животное подоено')

    def sound(self):
        print(f"Животное издает звук  {self.voice}")

    def __init__(self):
        self.name = ['Манька']
        self.weight = 50

class Lamb():
    voice = 'meeeeeeee'
    type_an = 'Овечка'

    def feed(self):
        print('Животное сыто')

    def cut(self):
        print('Животное подстрижено')

    def sound(self):
        print(f"Животное издает звук  {self.voice}")

    def __init__(self):
        self.name = ['Барашек', 'Кудрявый']
        self.weight = 20

class Chicken(Goose):
    voice = 'kokoko'
    type_an = 'Курица'

    def __init__(self):
        self.name = ["Ко-Ко", "Кукареку"]
        self.weight = 5

class Goat(Cow):
    voice = 'mememe'
    type_an = 'Коза'

    def __init__(self):
        self.name = ["Рога", "Копыта"]
        self.weight = 15

class Duck(Goose):
    voice = 'Crya'
    type_an = 'Утка'

    def __init__(self):
        self.name = ["Кряква"]
        self.weight = 5

my_Goose = Goose()
my_Cow = Cow()
my_lamb = Lamb()
my_Chicken = Chicken()
my_Goat = Goat()
my_Duck = Duck()

oll_weight = (my_Goose.weight * len(my_Goose.name)) + (my_Cow.weight * len(my_Cow.name)) + (my_lamb.weight * len(my_lamb.name)) + (my_Chicken.weight * len(my_Chicken.name))
+ (my_Goat.weight * len(my_Goat.name)) + (my_Duck.weight * len(my_Duck.name))
print(f' Общий вес животных составляет:  {oll_weight}')

max_weigt = max((my_Goose.weight), (my_Cow.weight), (my_lamb.weight), (my_Chicken.weight), (my_Goat.weight),(my_Duck.weight))
print('\nСамое тяжелое животное это:')
if max_weigt == my_Goose.weight:
    print('Гусь')
elif max_weigt == my_Cow.weight:
    print('Корова')
elif max_weigt == my_lamb.weight:
    print('Овечка')
elif max_weigt == my_Chicken.weight:
    print('Курица')
elif max_weigt == my_Goat.weight:
    print('Коза')
elif max_weigt == my_Duck.weight:
    print('Утка')