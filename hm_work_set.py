# Дан список чисел, который может содержать до 100_000 чисел. 
# Определите, сколько в нем встречается различных чисел.

def diff_num(some_list:set) -> int:
    
    len_num = len(set(some_list)) 
    return len_num

some_list = input().split()

print(diff_num(some_list))


#69 35 69 94 82 54 68 96 33 65 65
