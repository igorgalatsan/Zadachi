"""
откачка - картинка(2 насоса, номера клапанов, выбор номера клапана, показывает какие клапана открыть), таймер добавить и 
и сохранение замеров(в  таблицу №танка и сколько см осталось и  в тоннах показывать))

закачка - как откачка, номер клапанов другие

схема - просто таблица или кртинка, фото - расположение клапанов

время - таблица с номером танка и кол-во времени на закачку и откачку

Замеры по всем операциям за сутки(можно еще геолокацию писать)
"""

import time
import keyboard

#OPENED = "opened"
#CLOSED = "closed"

CLAPANS_RIGHT_BRANCH = {"FP": 1, "DB1S": 3, "ST1S": 5, "DB1C": 7, "DB2S": 8, "ST2S":10,
                "DB3S": 13, "ST3S": 15, "DB3C": 17, "DB4P":20, "ST4S": 21}

CLAPANS_LEFT_BRANCH = {"DT":2, "DB1P":4, "ST1P":6, "DB2P":9, "ST2P":11,"DB2C":12,
              "DB3P":14, "ST3P":16, "DB4C":18, "DB4S":19, "ST4P":22, "ST7S":29,
              "ST7P":30, "STTS":47, "STTP":48}

TIMERS = {

    # время старта закачки в сек
}

D_TIMES_PUMP_IN = {'FP': 1, 'DT': 2, 'DB1S': 3, 'DB1P': 4, 'ST1S': 5, 'ST1P': 6,
                  'DB1C': 7, 'DB2S': 8, 'DB2P': 9, 'ST2S': 10, 'ST2P': 11, 
                  'DB2C': 12, 'DB3S': 13, 'DB3P': 14, 'ST3S': 15, 'ST3P': 16, 
                  'DB3C': 17, 'DB4C': 18, 'DB4S': 19, 'DB4P': 20, 'ST4S': 21, 
                  'ST4P': 22, 'ST7S': 29, 'ST7P': 30, 'STTS': 47,'STTP': 48}
    # dtime in sec
    

D_TIMES_PUMP_FROM ={'FP': 1, 'DT': 2, 'DB1S': 3, 'DB1P': 4, 'ST1S': 5, 'ST1P': 6,
                  'DB1C': 7, 'DB2S': 8, 'DB2P': 9, 'ST2S': 10, 'ST2P': 11, 
                  'DB2C': 12, 'DB3S': 13, 'DB3P': 14, 'ST3S': 15, 'ST3P': 16, 
                  'DB3C': 17, 'DB4C': 18, 'DB4S': 19, 'DB4P': 20, 'ST4S': 21, 
                  'ST4P': 22, 'ST7S': 29, 'ST7P': 30, 'STTS': 47,'STTP': 48}
                  
def set_new_timer() -> None:
    while True:
        klapan = input("ВВедите номер клапана: ").upper()
        
        # валидацию клапана в соответствии со сипском 
        if CLAPANS.get(klapan, False):
        
            # Сросить: создать?
            if input("Открыть? (y/n) ").lower() == "y":
                
                # установить клапан в положение открыт
                CLAPANS[klapan] = OPENED
                # добавить время страта таймера
                TIMERS[klapan] = int(time.time())
                break
            
        else:
            print("Нет такого клапана!")       
    # вернуться в меню

def alarm_func():
    for clapan, start_time in TIMERS.items():
        dt = D_TIMES[clapan]
        end_time = start_time + dt
        current_time = int(time.time())
    
        # проверить вышло ли время для клапана
        if current_time > end_time:
            # если вышло, то напечатать для какого клапана
            print(f"{clapan} most closed!!")
        
    # вернуться в функцию main


def main():
    print("ВВедит q чтобы установить ноый таймер")
    while True:
        if keyboard.is_pressed('q'):
            set_new_timer()
        # если нажата кнопка пробе на клавиатуре то set_new_timer
        alarm_func()
        # печатать только раз в секунду !!!
        if keyboard.is_pressed('с'):
            close_timer()

#
if __name__ == "__main__":
    main()

    # pip install keyboard