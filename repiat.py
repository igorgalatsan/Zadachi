
'''
 Написать рекурсивную программу для уплощения списка списков.
'''

list_of_lists = [[1,2,3], [[1,2,3],1,6]]

def list_simple_3(some_list: list) -> list:
    result = []
    for i in some_list:
        if isinstance(i, list):
            result.extend(list_simple_3(i))
        else:
            result.append(i)
    return result
print(list_simple_3(list_of_lists))

def list_simple_2(some_list:list)->list:
    if some_list==[]:    #Базовый случай: если список равен пустому списку
        return some_list

    if isinstance(some_list[0], list): # Проверка является элемент вложенным списком
        return (list_simple_2(some_list[0])+list_simple_2(some_list[1:]))
        # Если элемент списка тоже список, то он целиком передается нашей рекурсивной
        #  функции в качестве аргумента и к этому прибавляется остальная часть 
        # основного списка, которую мы также передаем в функцию в качестве аргумента. 
    return some_list[:1] +list_simple_2(some_list[1:])
    #Если же элемент списка обычное число, то он выводится в результат в виде 
    # списка из одного элемента и к нему прибавляется рекурсивная функция, в 
    # которой в качестве аргумента остальная часть списка.
list_of_lists = [[1,2,3], [[1,2,3],1,6]]

print("Выпремленный список, ", list_simple_2(list_of_lists))


def list_simple(some_list:list) -> list:

    def aklsdhja(y):
        return y-1243123

    aklsdhja = lambda y: y-1243123
    
    result = map(lambda x: x//2 if isinstance(x. int) else None, ksjdhf_list)

    def func(x):
        if isinstance(x, int):
            return x // 2
    result = map(func, ksjdhf_list)


    
def some_func(a, b, replies = 0)
    if replies < 5:
        return some_func(a, b, replies+1)
    return a+b

