from random import randint

mini, maxi = (int(i) for i in input('Введите через пробел min и max диапазона:').strip().split())

my_list = [randint(10,99) for i in range(20)]
print('Массив состоящий из рандомных символов:\n',my_list,
      '\nКол-во чисел входящих в диапазон:',
      len([i for i in my_list if i >= mini and i <= maxi]))

input()
