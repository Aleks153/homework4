my_string = input('Введите произвольный текст: ')
print(len(my_string))
print(my_string.upper())
print(my_string.lower())
print(my_string.replace(' ',''))
print(my_string[0])
print(my_string [-1])
print('__________')
print('Баловство:')
simvol = 'символ'
value = len(my_string)
x = value%10
if value == 1:
    print('В Вашем тексте ', value, simvol)
if value == 11:
    print('В Вашем тексте ', value, simvol + 'ов')
if value > 11 and x == 1:
    print('В Вашем тексте ', value, simvol)
if 1< x <= 4:
    print('В Вашем тексте ',value, simvol+'а')
if x >4:
    print('В Вашем тексте ',value, simvol+'ов')

print('Текст в верхнем регистре: "',my_string.upper(),'"')
print('Текст в нижнем регистре: "',my_string.lower(),'"')
kolich_probel = my_string.count(' ')
probel = 'пробел'
if kolich_probel == 1:
    print('Текст без ', probel+'а'+':', my_string.replace(' ',''))
if kolich_probel > 1 or kolich_probel == 0:
    print('Текст без ', probel+'ов'+':', my_string.replace(' ',''))
print('Первый символ: "',my_string[0],'"')
print('Крайний символ: "',my_string [-1],'"')
