D_TIMES_PUMP_IN = {"DT":2, "DB1P":4, "ST1P":6, "DB2P":9, "ST2P":11,"DB2C":12,
              "DB3P":14, "ST3P":16, "DB4C":18, "DB4S":19, "ST4P":22, "ST7S":29,
              "ST7P":30, "STTS":47, "STTP":48,"FP": 1, "DB1S": 3, "ST1S": 5, "DB1C": 7, "DB2S": 8, "ST2S":10,
                "DB3S": 13, "ST3S": 15, "DB3C": 17, "DB4P":20, "ST4S": 21}

sorted_dict = dict(sorted(D_TIMES_PUMP_IN.items(), key=lambda item: item[1]))
print(sorted_dict)
D_TIMES_PUMP_IN ={'FP': 1, 'DT': 2, 'DB1S': 3, 'DB1P': 4, 'ST1S': 5, 'ST1P': 6,
 'DB1C': 7, 'DB2S': 8, 'DB2P': 9, 'ST2S': 10, 'ST2P': 11, 'DB2C': 12, 'DB3S': 13,
  'DB3P': 14, 'ST3S': 15, 'ST3P': 16, 'DB3C': 17, 'DB4C': 18, 'DB4S': 19,
   'DB4P': 20, 'ST4S': 21, 'ST4P': 22, 'ST7S': 29, 'ST7P': 30, 'STTS': 47,
    'STTP': 48}