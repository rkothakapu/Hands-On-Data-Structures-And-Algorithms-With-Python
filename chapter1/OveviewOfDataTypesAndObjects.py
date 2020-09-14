# numeric types: int, float, bool, complex
# sequence types: list, str, typle, range
# mapping type: dict
# two set types

a = 5
b = 5

# a and b have the same value
if a == b:
    print('a and b have the same value')

# a and b are the same object
if a is b:
    print('a and b are the same object')

# a and b are the same type
if type(a) is type(b):
    print('a and b are the same type')

# Mutable vs immutable
# mutable objects such as list can have their values changed.
# They have methods such as insert() or append() that changes object's value
# Immutable objects such as strings can not have their values changed
# Though the value cannot be changed, an identifier  referencing this object can be reassigned another value


# Strings - Immutable sequence objects
# s.capitalize, s.count(substring, [start, end]), s.find(substring, [start, end])
# s.isalnnum(), s.isalpha(), s.isdigit()
# s.split([separator], [maxsplit]), s.join(t), etc.
greet = 'hello world'
print('\n')
print(greet[1])
print(greet[0:8])
print(greet[0:8:2])

for i in enumerate(greet[0:5]): print(i)

# Lists
# list(s) -  returns a list of sequence s.
# s.append(x) -  Appends element x at the end of the list s.
# s.count(x), s.index(x, [start], [stop]), s.insert(i, x),
# s.pop(i), s.remove(x), s.reverse(), s.sort(key, [reverse])
print('\n')
x = 1;
y = 2;
z = 3
list1 = [x, y, z]
list2 = list1
list2[1] = 4
y = 5
print(list1)

# List can contain nested structures
items = [['rice', 2.4, 8], ['flour', 1.9, 5], ['corn', 4.7, 6]]
print('\n')
for item in items:
    print('Product: %s Price: %.2f Quantity: %i' % (item[0], item[1], item[2]))

# Since lists are mutable, we can perform inplace updates
# Update price of the flour by 20%:
items[1][1] *= 1.2
print('Update price of the flour by 20%:')
for item in items:
    print('Product: %s Price: %.2f Quantity: %i' % (item[0], item[1], item[2]))

# List comprehension
print('\nList Comprehension:')
l = [2, 4, 8, 16]
print([i ** 3 for i in l])


def f1(x): return x * 2


def f2(x): return x * 4


print([f1(f2(i)) for i in range(16)])

# nested loop:
list1 = [[1, 2, 3], [10, 20, 30]]
print([i * j for i in list1[0] for j in list1[1]])

words = 'here is a sentence'.split()
print([[word, len(word)] for word in words])


# Functions as First class objects
def greeting(language):
    if language=='eng':
        return 'hello world'
    elif language=='fr':
        return 'Bonjour le monde'
    else:
        return 'Language not supported'


l=[greeting('eng'), greeting('fr'), greeting('gr')]
print('\n'+l[1])


# Functions can also be used as an argument
def callf(f):
    lang = 'eng'
    return f(lang)


print(callf(greeting))

# Higher order functions: Functions that take other functions as arguments, or that return other functions
# Built-in examples: map(), filter()
list3 = [1, 2, 3, 4]
print('\n')
for item in map(lambda x: x*2, list3): print(item)
print('\n')
for item in filter(lambda x: x<4, list3): print(item)

words = str.split('The longest word in this sentence')
print(sorted(words, key=len))

# Case insensitive sorting
sl = ['A', 'b', 'a', 'C', 'c']
sl.sort(key=str.lower)
print('Case insensitive sorting: ', sl)

sl.sort()
print('normal sorting: ', sl)
# list.sort function is in place and doesn't returns anything. This method changes the target object and returns None

items = [['rice', 2.4, 8], ['flour', 1.9, 5], ['corn', 4.7, 6]]
items.sort(key=lambda item: item[1])
print(items)

# Recursive Functions
print('\nRecursive Functions')
# Termination or base case


def iterTest(low, high):
    while low <= high:
        print(low)
        low = low+1


def recurTest(low, high):
    if low <= high:
        print(low)
        recurTest(low+1, high)