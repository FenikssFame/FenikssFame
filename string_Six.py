word = ('Привет ученик')
print(word)

word_two = word[:word.find(' ')]
word_one = word[word.find(' ') + 1:]
        
print(word_one + ' ' + word_two)
input()


