my_list = [9,6,5,4,8,45,34,45,35,7,87,45,34,657,78]

print('Первоначальный список: ',my_list)

print('Список одинаковых значений',
      set([i for i in my_list if my_list.count(i) > 1]))

input()
