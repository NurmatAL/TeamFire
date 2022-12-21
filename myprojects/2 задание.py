"""""
 Furniture
 Тип дома, общая площадь и перечень наименований мебели В новом доме совсем нет мебели.
 Мебель имеет название и площадь, из которых Спальня: 4 квадратных метра Гардероб: 2 квадратных метра Стол: 1,5 квадратных метра.
 Добавьте в дом три вышеупомянутых предмета мебели.
 При печати дома требуются следующие данные: тип дома, общая площадь, оставшаяся площадь, список названий мебели.


"""
class furniture():

    def __init__(self, name, area):
        self.name = name
        self.area = area
    def __str__(self):
        return f"{self.name, self.area}"

krovat = furniture('кровать', 4)
shkaf = furniture('шкаф', 2)
stol = furniture('стол', 1.5)

class house():
    def __init__(self, monolit, OArea):
        self.house_style = monolit
        self.Ozarea = 20000
    def __str__(self):
        return f"{self.house_style, self.Ozarea}"

    def add_item(self, item):
        self.item = item

if __name__ == '__main__':

    house2 = house('One bedroom and one bathroom', 5)
    print(house2)
    house2.add_item(krovat)
    print(krovat)
    print(house2)
    house2.add_item(stol)
    print(stol)
    print(house2)
    print(shkaf)
    print(house2)
    house2.add_item(shkaf)
