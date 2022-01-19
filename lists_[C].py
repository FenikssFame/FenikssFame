my_list = [1,4,6,3,8,0,3,4,-4,-3,6,-2,-9,-20,-46,-2,321,35,-8]
print('Исходная матрица:',my_list)

negative = min(my_list)
average = negative/len([i for i in my_list if i < 0])

my_list.insert(my_list.index(negative), average)
my_list.remove(negative)

print('Средне арефметическое:',average,
      '\nМатрица с заменой:',my_list)
input()


