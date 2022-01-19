num = input('Введите натуральное число > 0:')

num_len = len(num)
summ = 0
mult = 1

for i in range(int(num_len)) :
    num_order = int(num)%10
    num = int(num)//10
    if num_order != 0 :
        summ += num_order
        mult *= num_order

print('Сумма цифр числа =',summ,
      '\nПроизведение цифр числа =',mult)
input()
