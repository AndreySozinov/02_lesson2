# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.

symbols = '0123456789ABCDEF'
number = int(input('Введите число: '))
print(f'Проверка: {hex(number)}')

result = ''
while number != 0:
    result = symbols[number % 16] + result
    number //= 16

print(f'Результат: {result}')
