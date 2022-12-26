def get_next_prime(num):
    
    arr = [i**2<=num for i in range(1,num+1)]
    print(arr)
        
 
   
        
# считываем данные
#n = int(input())
    
    
    
    
# вызываем функцию
print(get_next_prime(6))
print(get_next_prime(7))
print(get_next_prime(14))
num =  int(input())
arr = [i for i in range(1,num+1)]
print(arr)