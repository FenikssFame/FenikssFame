my_list = [1,1,4,6,3,7,8,9,4,0,7,8,9,6,5,4,7,9]

print('Исходная матрица:',my_list)

num_one = 0
num_two = 0
num_three = 0

for i in my_list :
    if i >= 1 and i <= 3 :
        num_one += 1
    elif i >= 4 and i <= 6 :
        num_two += 1
    elif i >= 7 and i <= 9 :
        num_three += 1

print("от 1 до 3 :", num_one,
      "\nот 1 до 3 :", num_two,
      "\nот 1 до 3 :", num_three)
input()
