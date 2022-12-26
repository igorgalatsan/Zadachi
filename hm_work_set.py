

# Дан список чисел, который может содержать до 100_000 чисел. 
# Определите, сколько в нем встречается различных чисел.

def diff_num(some_list:list) -> int:
    
    len_num = len(set(some_list)) 
    return len_num

# some_list = input().split()

# print(diff_num(some_list))


#`69 35 69 94 82 54 68 96 33 65 65`

# Даны два списка чисел, которые могут содержать до 100000 чисел каждый. 
# Посчитайте, сколько чисел содержится одновременно как в первом списке,
#  так и во втором. 


def two_list(start_list_1:list,start_list_2:list) -> int:
    some_set_1 =set(start_list_1)
    some_set_2 =set(start_list_2)
    result_intersection=len(some_set_1.intersection(some_set_2))
    
    return result_intersection 

some_list_1 = [69,35,69,94,82,54,68,96,33,65,65]
some_list_2 = [69,35,69,94,82,55,66,99,34,63,64]
 
print(f" в первом списке и во втором списке- {two_list(some_list_1,some_list_2)}")




#Во входном файле (вы можете читать данные из файла input.txt) записан текст.
# Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов или символами конца строки.

# Определите, сколько различных слов содержится в этом тексте.
 

# пока не могу придумать как привести все слова в списке к одному регистру
# потому что получается слово одинаковое а регистр разный и еще подумаю над задачей 

with open("text.txt") as file:
    add_list = [item.lower().split() for item in file]
#print(add_list)

unpack_list = [x for i in add_list for x in i]
print(unpack_list)

add_set = set(unpack_list)
print(len(add_set))     


# Рассмотрим последовательность целых чисел длины N. По ней с шагом 1
# двигается “окно” длины K, то есть сначала в “окне” видно первые K чисел,
# на следующем шаге в “окне” уже будут находиться K чисел, начиная со второго,
# и так далее до конца последовательности. Требуется для каждого положения “окна”
# определить минимум в нём.
# Входные данные
# В первой строке входных данных содержатся два числа N и K 
# (1 ≤  N ≤  150000, 1 ≤ K ≤ 10000, K ≤  N) – длины последовательности и “окна”,
# соответственно. На следующей строке находятся N чисел – сама последовательность.
# Выходные данные
# Выходые данные должны содержать N − K + 1 строк – минимумы для каждого 
# положения “окна”.

from function_py import get_random_list

def find_window(N: int, K:int):
    pass
 
# N = int(
#         input(
#             'Input number for len of list: '
#             )
#         )

print(int())

# K = int(
#         input("len of window:"
#         )
#     )

N = 14
K = 3
_LIST = [
    18, 16, 15, 
    14, 21, 17, 
    15, 12, 17, 
    13, 13, 12,
    14, 11
]

# [0:3, 3:6, 6:9, 9:12, 12:]

for i in range(0, N, K):
    print(min(_LIST[i:i+K]))





def print_min(some_list, k):
    print('min of ', some_list[:k], ' = ', min(some_list[:k]))
    if len(some_list[k:]) > 0:
        print(some_list[k:])
        print_min(some_list[k:], k)

_LIST = get_random_list(30)
print_min(_LIST, K)
