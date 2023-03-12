# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и
# знаменателем. Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

import fractions
import math

fraction1 = input('Введите первую дробь: ').split('/')
fraction2 = input('Введите вторую дробь: ').split('/')

numer1 = int(fraction1[0])
denom1 = int(fraction1[1])
numer2 = int(fraction2[0])
denom2 = int(fraction2[1])

num_add = numer1 * denom2 + numer2 * denom1
den_add = denom1 * denom2

divider = math.gcd(num_add, den_add)
if divider:
    num_add //= divider
    den_add //= divider

num_mult = numer1 * numer2
den_mult = denom1 * denom2

divider = math.gcd(num_mult, den_mult)
if divider:
    num_mult //= divider
    den_mult //= divider

print(f'{numer1}/{denom1} + {numer2}/{denom2} = {num_add}/{den_add}')
print(f'{numer1}/{denom1} * {numer2}/{denom2} = {num_mult}/{den_mult}')

print(f'Проверка сложения: {fractions.Fraction(numer1, denom1) + fractions.Fraction(numer2, denom2)}')
print(f'Проверка умножения: {fractions.Fraction(numer1, denom1) * fractions.Fraction(numer2, denom2)}')
