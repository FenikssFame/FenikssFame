from random import randint

lst = [randint(0,100) for i in range(10)]
print(lst)

lst[lst.index(max(lst))], lst[lst.index(min(lst))] = lst[lst.index(min(lst))], lst[lst.index(max(lst))]

print(lst)

input()
