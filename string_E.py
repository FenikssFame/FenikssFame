word = input("Введите слово: ")

print('Являеться перевертышем' if word == word[::-1] else 'Не являеться перевертышем')

input()
