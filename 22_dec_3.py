"""
Напишите функцию get_next_prime(num), 
которая принимает в качестве аргумента натуральное число num 
и возвращает первое простое число большее числа num.
"""

def get_next_prime(num):
    
    arr = [i for i in range(0,num+1)]
    
    arr[1]=0
    i = 2
    while i <= num:
        if arr[i] !=0:
            j= i+i
            while j<=num:
                arr[j]=0
                j=j+i
        i+=1
    
# считываем данные
#n = int(input())
    print(arr)
# вызываем функцию
# print(get_next_prime(6))
# print(get_next_prime(7))
# print(get_next_prime(14))


def eratoshen(N: int) -> list:
    result_list = [i for i in range(2, N)]
    for i in range(0, len(result_list)):
        if result_list[i] != 0:
            for x in range(result_list[i]**2, N, result_list[i]):
                result_list[x-2] = 0
    return [i for i in result_list if i != 0]

def eratoshen_2(N: int) -> list:
    simple_set = {x  for x in range(2,N)}
    simple_set_2 ={}

def get_next_simple_number(N):
    result_list = eratoshen_2(int(N + N*(3/4)))
    print(result_list)
    return [i for i in result_list if i > N][0]

print(get_next_simple_number(6))
print(get_next_simple_number(7))
print(get_next_simple_number(14))
# 628547
print(get_next_simple_number(628549))
# 628561