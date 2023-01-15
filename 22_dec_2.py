def is_palindrome(text:str) -> bool:
    
    
    str_1 = "".join(filter(str.isalnum, text))# 
    #str_1 = text.lower().translateslate({ord(i): None for i in " .,!-"})
    #str_new = text[::-1].lower().translate({ord(i): None for i in " .,!-"})
    str_new = str_1[::-1]
    str_1set =set(enumerate(str_1.lower()))
    str_new_set = set(enumerate(str_new.lower()))
    result = str_1set.difference(str_new_set)
    if len(result)==0:
        return True
    else:
        return False
    
    

# считываем данные
#txt = input()

# вызываем функцию
print(is_palindrome("Do me?.. Kill I victim? Must summit civil like mod."))
print(is_palindrome('А роза упала на лапу Азора.'))
print(is_palindrome('Gabler Ruby - burrel bag!'))
print(is_palindrome('BEEGEEK'))
print(is_palindrome("Тер жен, а нес токмо недаром кот сена не жрет."))
print(is_palindrome("Карман, жена, но Какашкин - вор! О, Ковалева... Вела во коровник. Ша! Как она нежна! рак..."))