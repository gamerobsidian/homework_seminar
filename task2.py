# Задача 2: Найдите сумму цифр трехзначного числа.

n = input("Введите трехзначное число: ")
n = int(n)

d1=n%10
n=n//10
d2=n%10
n=n//10

print("сумма цифр числа:", n+d2+d1)