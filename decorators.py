'''
decorators allow you to extend and or modify the behavior
of a callable(functions/methods/classes) without permanently modifying
the callable itself.
'''

def decorator_function(original_func):
    def wrapper_func(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_func.__name__))
        return original_func(*args, **kwargs)
    return wrapper_func



@decorator_function
def display():
    print('display function ran')


display()

'''
In this code, I have used a decorator on the display method and then 
used it. It then did the jobs of the decorator function and the display function. 
'''
@decorator_function # to be able to do this, we need *args, **kwargs in the wrapper func and return original function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('john', 25)


#  classes can also be used with decorators

class decorator_class(object):

    def __init__(self, orginal_func):
        self.original_func = orginal_func

    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.original_func.__name__))
        return self.original_func(*args, **kwargs)




@decorator_class
def display():
    print('display function ran')

@decorator_class
def display_info(name, age):
    # print('display_info ran with arguments ({}, {})'.format(name, age))
    print(f'display_info ran with arguments ({name}, {age})')
display()
display_info('john', 25)

# classes can do the same exact thing
print("\U0001F602")