
'''
def say_hello(user):
    print(f'From {user["name"]}: Hello!')

def get_new_user(name, age):
    return {
        'name': name,
        'age': age,
        'say': say_hello,
    }

user = get_new_user('Roma', 31)
user['say'](user)




class User:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'From {self.name}: Hello!')
    
    def __repr__(self) -> str:
        return f'User: {self.name} {self.age}'


user = User('Vadim', 55)
print(user.name)
print(user.age)
user.say_hello()
print(user)



class Car:
    def __init__(self, mark:str = None, color:str = None) -> None:
        self.mark = mark if mark else input('ВВедите марку машины: ')
        self.color = color if color else input("Ввведите цвет машины: ")

    def watch_mark_color(self):
        return print(f"Car: {self.mark} : {self.color}" )

    def __repr__(self) -> str:
        return f"Car: {self.mark}: {self.color}"


car = Car("Honda", "grey")

print(car)

car.watch_mark_color()

# new_car = Car()
# print(new_car)

class Track(Car):
    def __init__(
        self, 
        mark: str = None, 
        color: str = None, 
        weigh: int = 0,
        x: int = None,
        y: int = None
    ) -> None:
    
        super().__init__(mark, color)
        self.weigh = weigh
        self.x = x
        self.y = y

    def move(self, d_x: int = None, d_y: int = None)-> None:
        # написать метод который изменяет координаты грузовика
        if self.x is None:
            self.x = 0
        self.x += d_x if not d_x is None else int(input("Введите координату х: "))
        if self.y is None:
            self.y = 0
        self.y += d_y if not d_y is None else int(input("Введите координату у: "))
               
    
    def __repr__(self) -> str:
        return super().__repr__() + f": {self.weigh} ({self.x}, {self.y})"


my_track = Track(mark="Maz",color="red",weigh=1234,x=66,y=55)
# Создать экземпляр грузовика
my_track.move(100,100)
# переместить его на 10, 20
# вывести на экран грузовик
print(my_track)
'''
# SQlite(RAW SQL, ORM SQLAlchemy), postgres(Views, Fuctions, Proc)
# celery + rabbitmq (мультипроцессорность)
# asyncio (асинхронность)

# tkiner
"""
откачка - картинка(2 насоса, номера клапанов, выбор номера клапана, показывает какие клапана открыть), таймер добавить и 
и сохранение замеров(в  таблицу №танка и сколько см осталось и  в тоннах показывать))
закачка - как откачка, номер клапанов другие
схема - просто таблица или кртинка, фото - расположение клапанов
время - таблица с номером танка и кол-во времени на закачку и откачку
Замеры по всем операциям за сутки(можно еще геолокацию писать)
"""

"""
ДЗ:
Создайте класс Soda (для определения типа газированной воды), 
принимающий 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду). 
В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}» 
в случае наличия добавки, а иначе отобразится следующая фраза: «Обычная газировка».

Создать родителя Water с методом show_my_drink()

Создать потомок от Water Kompot с атрибутами добавок
 
Создать экземляр класса Kompot с атрибутами вишня и яблоко
вывести его на экран.
"""


class Water:
    def show_my_drink(self) -> str:
        return f"Обычная вода"

    def __repr__(self) -> str:
        return f"Обычная вода"


class Soda(Water):
    def __init__(self,ingredient:str = None) -> None:
        self.ingredient = ingredient 
    
    def show_my_drink(self) -> str:
        if self.ingredient is None:
            return f"Обычная газировка"
        return f"Газировка с {self.ingredient}"
    
    def __repr__(self) -> str:
        if self.ingredient is None:
            return f"Обычная газировка"
        return f"Газировка с {self.ingredient}"


class Kompot(Water):
    def __init__(self,
     ingredient: str = None,
     apple: str = None,
     cherry: str = None
     ) -> None:
        self.ingredient = ingredient
        self.apple = apple
        self.cherry = cherry
    
    def show_my_drink(self) -> str:
        if self.ingredient is None:
            if self.cherry is None:
                return f"Компот с {self.apple}"
            else:
                return f"Компот с {self.cherry}"

    def __repr__(self) -> str:
        return self.show_my_drink()


user_for_soda = Soda()
# print(user_for_soda)


user_for_water = Water()
# print(user_for_water)

user_for_kompot = Kompot(apple="яблоко")
# print(user_for_kompot)

pack = [user_for_soda, user_for_water, user_for_kompot]

for i in pack:
    # print(i)
    print(i.show_my_drink())
