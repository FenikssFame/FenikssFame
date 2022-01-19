num = int(input('Введите число не больше 100 :'))

summ = 0

if num > 100 :
    print('Введено число привышающее значение 100!')
else :
    for i  in range(1,num+1,1) :
        summ += 1/i
    print('Сумма',num,'чисел =',summ)

input()
