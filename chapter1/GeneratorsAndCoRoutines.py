# We can create functions that do not just return one result but rather an entire sequence of results, by using the
# yield statement. These functions are called the generators.

# compares the running time of a list compared to a generator
import time


# generator function creates an iterator of odd numbers between n and m
def oddGen(n, m):
    while n < m:
        yield n
        n += 2


# builds a list of odd numbers between n and m
def oddLst(n, m):
    lst = []
    while n < m:
        lst.append(n)
        n += 2
    return lst


# the time it takes to perform sum on an iterator
t1 = time.time()
sum(oddGen(1, 1000000))
print("Time to sum an iterator: %f" % (time.time() - t1))
# the time it takes to build and sum a list
t1 = time.time()
sum(oddLst(1, 1000000))
print("Time to build and sum a list: %f" % (time.time() - t1))

# Generator Expressions, which, apart from replacing square brackets with parentheses, use the same syntax and carries
# out the same operation as list comprehensions. Generator expressions, however, do not create a list;
# they create a generator object. This object does ot create the data, but creates the data on demand.

# you can change generator into a list using list() function
print()
lst1 = [0, 1, 2, 3]
gen1 = (10 ** i for i in lst1)
print(type(gen1))
for x in gen1: print(x)


# CLASSES and OBJECT PROGRAMMING
class Employee(object):
    numEmployee: int = 0

    def __init__(self, name, rate):
        self.owed = 0
        self.name = name
        self.rate = rate
        Employee.numEmployee += 1

    def __del__(self):
        Employee.numEmployee -= 1

    def hours(self, numHours):
        self.owed += numHours * self.rate
        return "%.2f hours worked" % numHours

    def pay(self):
        self.owed = 0
        return "payed %s " % self.name


emp1 = Employee('Jill', 18.50)
emp2 = Employee('Jack', 15.50)

print()
print(Employee.numEmployee)
print(emp1.hours(20))
print(emp1.owed)
print(emp1.pay())


# SPECIAL METHODS
# __add__ -> +
# __repr__ -> toString
# __init__ -> constructor, etc

# INHERITANCE
# Inheritance in Python is done by passing the inherited class as an argument in the class definition. It
# is often used to modify the behavior of existing methods. For a subclass to define new class variables, it needs to
# define an __init__() method, as follows:
class specialEmployee(Employee):
    def __init__(self, name, rate, bonus):
        Employee.__init__(self, name,
                          rate)  # calls the base classes
        self.bonus = bonus

    def hours(self, numHours):
        """

        :type numHours: float
        """
        self.owed += numHours * self.rate + self.bonus
        return "%.2f hours worked" % numHours


# Example issubclass() to check whether a class is a subclass of another class
# Example isinstance() to check if an object belongs to a class or not

print(issubclass(specialEmployee, Employee))
print(issubclass(Employee, specialEmployee))

d = specialEmployee("packt", 20, 100)
b = Employee("packt", 20)
print(isinstance(b, specialEmployee))
print(isinstance(b, Employee))


# Class method vs static method
# class method: @classmethod decorator and 'cls' is passed as first agument by convention
class exponentialA(object):
    base = 3

    @classmethod
    def exp(cls, x):
        return (cls.base ** x)

    @staticmethod
    def addition(x, y):
        return (x + y)


class exponentialB(exponentialA):
    base = 4


a = exponentialA()
b = a.exp(3)
print("the value: 3 to the power 3 is", b)
print('The sum is:', exponentialA.addition(15, 10))
print(exponentialB.exp(3))

# The difference between a static method and a class method is that a static method doesn't know anything about the
# class, it only deals with the parameters, whereas the class method works only with the class, and its parameter is
# always the class itself.

# DATA ENCAPSULATION AND PROPERTIES private attributes begin with double underscore, such as __privateMethod(). These
# methods are automatically changed to __Clasname_privateMethod()
