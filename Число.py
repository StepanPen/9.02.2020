n = int(input('Введите число:'))
c = n % 10
b = n // 10 % 10
a = n // 100
print(c * 100 + b * 10 + a)