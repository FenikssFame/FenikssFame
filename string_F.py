word = input("Введите два слова: ")
        
print(word[word.find(' ') + 1:] + ' ' + word[:word.find(' ')])

input()


