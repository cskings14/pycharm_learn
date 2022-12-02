# What is Big O Notation?

'''
Big O is a simplified analysis of an algorithm's efficiency.

1. Complexity in terms of the input size, n.
2. Machine-independent (You don't calculate every single program on a different machine. It simplifies this problem).
3. We examine the basic computer steps of steps of the algorithm.
4. Big O analyzes time and space.


When talking about Big O, we generally talk about the worst case scenario.
For example, if we have an array that is 100 numbers long.
We are trying to find the number 23.
If we go through all of the code to find 23,
the complexity would be O(n) or in this specific case, O(100).



GENERAL RULES

1. We ignore constants
Example: 5n -> O(n)
What does this mean? As n increases exponentially,
n times 5 won't matter as much as n itself. If the time complexity is
1 billion seconds at O(n), 5 billion won't really matter
in the grand scheme of things.

2. Certain terms "dominate" others
Example: O(1) < O(logn) < O(n) < O(nlogn) < O(n^2) < O(2^n) < O(n!)
What does this mean? This is like the general rule.
For example, if we have a program where there are two main parts,
the first being O(n) and the other being O(n^2), O(n) would
not matter in the grand scheme of things because O(n^2) is so much
bigger.




'''

# constant time / O(1) (independent os input size, N).

# x = 5 + (15 * 20)
# y = 12 - 2
# print(x  + y)

'''
Total time = 3 * O(1)
We drop the constants so this program is still O(1).
'''

# linear time / O(n)

# for x in range (O,n):
#   print(x)

'''
Total time = O(n) * O(1) = O(n)
O(1) comes from the print statement
O(n) comes from the for loop.
The constant of O(1) is dropped.
'''

# quadratic time / O(n ^ 2)

# x = 5 + (15 * 20)
# for x in range(0, n): O(n)
#   print x
# for x in range(0, n):    \
#   for x in range(0, n):    O(n ^ 2)
#       print(x * y)       /

'''
Total time = O(1) * O(n) * O(1) * O(n * n) * O(1)
In this case, everything else is dwarfed by O(n ^ 2).
Everything else is dropped besides (n ^ 2).
'''

# another quadratic time / O(n ^ 2)

# if x > 0:   O(1)
#
# else if x < 0:    O(logn)
#  else:    O(n ^ 2)

