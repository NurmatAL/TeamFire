# AK-47:
# У солдата Райана есть АК-47
# Солдаты могут стрелять («тиги-тигитиш»).
# Пистолеты могут стрелять пулями.
# Пистолеты могут начинать патроны - увеличивайте количество патронов (перезаряжает)
# Создайте класс Act_of_Shooting, который унаследует от класса Soldier класс Guns.

# Где солдат будет стрелять из пушки и перезаряжаться, и стрелять еще раз.

class Soldier:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Guns(Soldier):
    def __init__(self, name):
        super().__init__(name)
        self.bullets = 50
        print('Количество пуль: ', self.bullets)

    def shoot_(self):
        num = int(input('Количество выстрелов: '))
        return num

    def shoot(self):
        new_bullets2 = self.bullets - Guns.shoot_(self)
        return f'Осталось пуль: {new_bullets2}'

    def add_bull(self):
        add_bull = int(input('Добавить пули: '))
        return f'Добавили {add_bull} итого {self.bullets + add_bull}'

class Act_of_Shooting(Guns):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f'{Act_of_Shooting.shoot(self)}\n' \
               f'{Guns.shoot_(self)}\n' \
               f'{Guns.shoot(self)}\n' \
               f'{Guns.add_bull(self)}'
    def shoot(self):
        return f'Выстрел: тиги-тигитиш'



    def get_shoot(self, a):
        if a == Act_of_Shooting.shoot:
            return f'{Guns.add_bull(self)}'


soldat = Act_of_Shooting('Rayan')
print(soldat)
soldat.get_shoot('тиги-тигитиш')