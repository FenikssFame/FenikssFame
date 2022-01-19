var_one = int(input('Введите первое число:'))
var_two = int(input('Введите второе число:'))

num = 1

if var_one > var_two :
    num = -1

while var_one != var_two + num :
    print(var_one)
    var_one += num
    
input()
