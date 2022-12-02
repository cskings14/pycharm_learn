'''
Functions are instructions packaged together to do a certain task
to define a function, use def
functions allow us to reuse code without writing tons of text
'''

def hello_func():
    pass

print(hello_func()) # says none because there is no return

def hello_fun(greet, name): # greet and name are parameters. They are local variables in a function
     return '{} {}.'.format(greet, name)
     # return (f'{greet} {name}.') could also do this

print(hello_fun('Hello', 'Chris'))

def student_info(*args, **kwargs):
    print(args) # positional arguments
    print(kwargs) # keyword arguments

# we could pass a list/dictionary to put in values

courses = ['Math', 'Art']
info = {'name': 'Jon', 'age': 22}
student_info(*courses, **info)















