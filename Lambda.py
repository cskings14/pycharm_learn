'''
Lambda is an anonymous function
'''

def func(x):
    func2 = lambda x: x + 5
    return func2(x) + 85

func3 = lambda x,y: x+y
print(func3(5,3))


print(func(2))





