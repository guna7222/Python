# variables declared outside a function is called global variable
# this can be accessed from inside and outside a function

x = 'hello'

def my_function():
    x = 'java'
    print(x)

my_function()
print(x)

y = "awesome"

def greetings():
    y = "great!"
    print('python is a ' + y)
    # python is a great!

greetings()
print(y)
