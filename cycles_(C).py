num = input('Введите целочисленное число:')
num_len = len(num)

num_order = 0
even_num = 0
nicho_num = 0

for i in range(num_len) :
    num_order = int(num)%10
    num = int(num)//10
    num_order %= 2
    
    if num_order == 0 :
        even_num += 1
    else :
        nicho_num += 1
        
print('Кол-во четных:',even_num,
      '\nКол-во нечетных:',nicho_num)
input()

