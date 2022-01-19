from math import sqrt

start = 1

while start != 0 :
    num_one = float(input('Введите первое число:'))
    num_two = float(input('Введите второе число:'))
    action = input('\nВВЕДИТЕ ТИП ОПЕРАЦИИ:'
                   '\nПеревод в двоичную сист. счисления - "2"'
                   '\nСложение - "+"'
                   '\nВычитание - "-"'
                   '\nУмножение - "*"'
                   '\nДеление - "/"'
                   '\nВозведение в степень - "**"'
                   '\nКвадратный корень - "sqrt"'
                   '\nОперация:')
    if action == "+" :
        print('Сумма =',num_one + num_two)
    elif action == "-" :
        print('Разность =',num_one - num_two)
    elif action == "*" :
        print('Умножение =',num_one * num_two)
    elif action == "/" :
        print('Деление =',num_one / num_two)
    elif action == "**" :
        print('Возведение в степень ',num_one,num_one**2)
        print('Возведение в степень ',num_two,num_two**2)
    elif action == "sqrt" :
        print('Корень из',num_one,sqrt(num_one))
        print('Корень из ',num_two,sqrt(num_two))
    elif action == "2" :
        print('Двоичная система ',num_one,bin(int(num_one)))
        print('Двоичная система ',num_two,bin(int(num_two)))
    else :
        print('"ERROR" \nПОВТОРИТЕ ВВОД!')
        
    start = int(input('Для выхода введите "0" : '
                      'Для продолжения введите "1": '))
