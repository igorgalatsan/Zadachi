# Дан список чисел, который может содержать до 100_000 чисел. 
# Определите, сколько в нем встречается различных чисел.

def diff_num(some_list:set) -> int:
    
    len_num = len(set(some_list)) 
    return len_num

some_list = input().split()

print(diff_num(some_list))


#69 35 69 94 82 54 68 96 33 65 65

# Даны два списка чисел, которые могут содержать до 100000 чисел каждый. 
# Посчитайте, сколько чисел содержится одновременно как в первом списке,
#  так и во втором. 


def two_list(start_list_1:list,start_list_2:list) :
    some_set_1 =set(start_list_1)
    some_set_2 =set(start_list_2)
    result_diff_1_2 =len(some_set_1.difference(some_set_2))
    result_diff_2_1 = len(some_set_2.difference(some_set_1))
    
    return result_diff_1_2, result_diff_2_1

some_list_1 = [69,35,69,94,82,54,68,96,33,65,65]
some_list_2 = [69,35,69,94,82,55,66,99,34,63,64]
 
print(f" в первом списке - {two_list(some_list_1,some_list_2)} во втором")

# не понимаю красиво вывести на экран  :
#  в первом списке - 5 элементов   во втором - 6 элементов
