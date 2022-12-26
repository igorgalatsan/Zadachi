
'''
 Написать рекурсивную программу для уплощения списка списков.
'''

list_of_lists = [[1,2,3], [[1,2,3],1,6]]


def list_simple_2(some_list:list)->list:
    if some_list==[]:
        return some_list
    if isinstance(some_list[0],list):
        return (list_simple_2(some_list[0])+list_simple_2(some_list[1:]))
    return some_list[:1] +list_simple_2(some_list[1:])

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


    return [x for x in some_list for x in some_list]

