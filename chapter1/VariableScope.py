a = 15
b = 25


def my_function():
    global a
    a = 11
    b = 21


my_function()
print(a)
print(b)
print("In the preceding code, we define two global variables. "
      "We need to tell the interpreter, using the keyword global, "
      "that inside the function we are referring to a global variable. "
      "When we change this variable to 11, these changes are reflected in the global scope. "
      "However, the b variable we set to 21 is local to the function, "
      "and any changes made to it inside the function are not reflected in the global scope. "
      "When we run the function and print b, we see that it retains its global value.\n\n\n")

# Example 2
a = 10


def my_function2():
    print(a)


my_function2()
print("Able to read the global variable even without using a 'global' keyword\n\n\n")

# Example 3
a = 10


# def my_function3():
#      print(a)
#      a= a+1
#
#
# my_function3()
# Above function throws an exception bcz assignment can be done only on local variables
# or global variable with explicit reference


# Example 4
a = 10


def my_function4():
    global a
    print(a)
    a = a+1


my_function4()
print("Above function doesn't throw an exception bcz assignment can be done on global variable "
      "after an explicit reference")
