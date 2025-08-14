#tests
fruits0 = ['kiwi', 'banana']
more_fruits0 = ['apple', 'orange']
fruits0.extend(more_fruits0)
print(fruits0)

fruits1 = ['kiwi', 'banana']
more_fruits1 = ['apple', 'orange']
fruits1.append(more_fruits1)
print(fruits1)

fruits2 = ['kiwi', 'banana']
more_fruits2 = ['apple', 'orange']
fruits2.insert(1, more_fruits2)
print(fruits2)

fruits3 = ['kiwi', 'banana']
fruits3.remove('banana')
print(fruits3)

fruits4 = ['kiwi', 'banana', 'mango']
popped = fruits4.pop(1)
print(fruits4, popped)

fruits5 = ['kiwi', 'banana', 'mango']
fruits5.clear()
print(fruits5)


