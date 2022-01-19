list_a = [1,1,2,3,4,8,13,21,34,55,89]
list_b = [1,2,3,4,5,6,7,8,9,10,12,13]

new_list = []

for i in list_a :
    if i not in new_list :
        if i in list_b :
            new_list.append(i)

print('Первый список:',list_a,
      '\nВторой список:',list_b,
      '\nСписок общих элементов:',new_list)

input()
