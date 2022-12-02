for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

'''
range is exclusive
The first number that changes in a nested for loop like this would be y
after why gets to its limit, x changes.



'''

# TODO CHALLENGE: make an f with x using x's.
'''
Should look like this:
xxxxx
xx
xxxxx
xx
xx
'''


numbers = [5, 2, 5, 2, 2]

for nu in numbers:
    print(nu * 'x')
# This is the easy way. In python, we can multiply strings. Let's try using a nested loop

print('')
print('')


for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)


