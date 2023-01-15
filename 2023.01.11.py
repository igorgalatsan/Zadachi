
person_1 = {
    "name": "Dmitry",
    "birthday": "01.01.1990",
    "address": "Lenina str. 98",
    "sex": "male",
    "email": "dima@ya.ru"
}

# 1. НАписать функцию конструктор для создания пользователей в виде словаря

def get_new_person(name, brithday, address, sex, email:str='') -> dict:
    """
    Конструктор пользователей
    """
    def _validate_email(email):
        if not email:
            return None
        return email
    
    return {
        "name": name,
        "birthday": brithday,
        "address": address,
        "sex": sex,
        "email": _validate_email(email)
    }

person_3 = get_new_person("Sergey", "05.05.1990", "Gagarina str","male", "sergio@mail.ru")
person_2 = get_new_person("Ivan", "02.02.1989", "Lenina str. 98", "male", "ivan@ya.ru")

print(person_2["name"])
print("-"*20)
print(person_2)

# # 0-255
# a = 294234
# b = 294230 + 4
# if a is b:
#     print(True)

# None 0 False
# 1 True
# print(True is 1)

