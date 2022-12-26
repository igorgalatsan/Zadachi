from random import randint


def get_random_list(num: int, down_limit:int = 10, up_limit:int = 99) -> list:
    '''
    Функция возвращает список указанной длинны.
    :param num: это длинна списка 
    :param down_limit: нижний предел рандомного значения
    :param up_limit: верхний предел рандомного значения  
    '''
    return [randint(down_limit, up_limit) for i in range(0,num)]
    


# if True:
#     x = 12
# else:
#     x = 13

# x = 12 if True else 13

# for x in [1,]:
#     if x // 2:
#         y = x 

# y = (x for x in [1,] if x //2)

if __name__ == '__main__':
    # TODO tests
    print(get_random_list(1, 0, 1)[0] in [1, 0])

    print(get_random_list(10))
    print(get_random_list(25,89))
    print(get_random_list(25,10,65))
    print(get_random_list(num=23,down_limit=10))
    print(get_random_list(16,up_limit=55))
    print(get_random_list(up_limit = 13,num=15,down_limit= 65))
    print(get_random_list(num=33,up_limit=33))

