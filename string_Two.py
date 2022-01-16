word = str(input('Введите предложение: '))

num = 0

lenth = len(word)
lenth_dif = lenth//2

if lenth % 2 != 0 :
    num = 1

print(word[lenth_dif + num:lenth] + word[:lenth_dif + num])


input()

