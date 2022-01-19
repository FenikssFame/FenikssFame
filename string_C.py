word = input("Введите слово минимум двумя 'h': ")

print(word[:word.find('h')] + word[word.rfind('h')+1:])
input()
