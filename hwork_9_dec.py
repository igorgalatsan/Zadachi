import logging

log = logging.getLogger('logger')

# class MyError:
#     pass

# def func(obj: dict):
#     try:
#         # step 1
#         if not isinstance(obj, dict):
#             raise TypeError

#         value = int(obj.get())
#         if value < 0:
#             raise MyError
    
#     except MyError:
#         # step 2
#         log.error('Dab obj in ..%s', obj)

#     except TypeError:
#         # step 2
#         log.error('Dab obj in ..%s', obj)

#     else:
#         # step 2
#         value += 3
#     finally:
#         # step 3
#         print('All OK')
from os import sys


def input_user_lst(entered_lst:int) -> list:
        num_list = []
        try:
            num_list =[int(i) for i in entered_lst]
            print(f"список чисел,{num_list}")
            return num_list
            
        except ValueError as e:
            # print("Необходимо вводить только целые числа")
            log.critical('Необходимо вводить только целые числа')
            # sys.exit()
            # raise e
        except TypeError:
            print("Необходимо1 вводить только целые числа")
        
        return num_list
                    

def remove_extrem_num(some_lst:list) -> list:
    try:
        if len(some_lst)>=4:
            sorted_lst = sorted(some_lst)
        else:
            print("В списоке должено быть не менее 4х элементов")
            return []
    except Exception:
        print("Необходимо вводить только целые числа")
        return []
    else:
        print(f'начальный список => {sorted_lst}')
        sorted_lst.pop()
        sorted_lst.pop(0)
        print(f'отсортированный список => {sorted_lst}')
        return sorted_lst


# entered_lst = input("Введите список целых,"\
    # "чисел резделенных пробелом ").split()

entered_lst = [92, 85, 90, 37, 56, 83, 94, 69, 95, 54, 11, 35, 73, 42, 38]
entered_lst = input_user_lst(entered_lst)

entered_lst = remove_extrem_num(entered_lst)

print(entered_lst)

    # if result not None:


    # if isinstance(result, list):
    #     for i in result:
    #         pass


 #1. При анализе собранных по результатам научных экспериментов данных
# зачастую возникает необходимость избавиться от экстремальных зна-
# чений, прежде чем продолжать двигаться дальше. Напишите функцию,
# создающую копию списка copy() deepcopy() с исключенными из него n наибольшими и наи-
# меньшими значениями и возвращающую ее в качестве результата. Поря-
# док следования элементов в измененном списке не обязательно должен
# в точности совпадать с источником.
# В основной программе должна быть продемонстрирована работа вашей
# функции. Для начала попросите пользователя ввести целые числа, затем
# соберите их в список и вызовите написанную вами ранее функцию. Вы-
# ведите на экран измененную версию списка вместе с оригинальной. Если
# пользователь введет менее четырех чисел, должно быть отображено соот-
# ветствующее сообщение об ошибке

# 2. В отдельной функции реализовать: исключить элементы больше 90% и меньше 10% 
# [92, 85, 90, 37, 56, 83, 94, 69, 95, 54, 11, 35, 73, 42, 38]
# 92 85 90 37 56 83 94 69 95 54 11 35 73 42 38  -->95 11
