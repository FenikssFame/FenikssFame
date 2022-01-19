my_list = [2,5,-3,-5,-2,34,56,1,54,-35,-3,-8,32,0]

new_list = []

for i in my_list :
    if i > 0 :
        new_list.append(i)
        
print('Список:',my_list,
      '\nСумма 1-го, 3-го и 6-го положительного числа по порядку =',
      new_list[0]*new_list[2]*new_list[5])

input()
