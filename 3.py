# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n=int(input("Введите число"))
i=1
s=0
while s<n:
    s=2**i
    i=i+1
    if s<n:
        print(s)