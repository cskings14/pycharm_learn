import sys

sys.setrecursionlimit(10_000)
'''
Recursion is basically a function that calls itself
Recursion is very powerful
It can make things easier than using iterations (for/while loops)
'''


# The if statement is the base case that
# stops recursion when you have reached the
# wanted value. It stops infinite recursion.

def func(k, n=0, arr=[]):
    if n == k:
        return  # this stops the recursion
    else:
        arr.append(n)
        func(k, n + 1, arr)
    return arr


# The else statement is the recursive case.
# Each time the function is called,
# it evaluates the statement. If true,
# the loops stops. Else, it continues.
# the else is where recursion goes.


'''
What does it do? k is the len(arr).
If n (the increment) is not at k, it adds n.
It stops when n is at k.
'''
# print(func(8))
# print(20, 0, [])

# TODO NOW LET'S LOOK AT MERGE SORT

'''
Merge sort is a divide and conquer algorithm
It uses recursion to do this.
It has a run time of O(n * log(n)) //Optimal running time for comparison based algorithms//
The logn comes form the array split into 2. The other n comes from multiple comparisons.
'''


# TODO MERGE SORT STEPS
# 1. Continuously split array in half until there are individual nodes
# 2. Call merge sort on each half to sort them recursively
# 3. Merge both sorted halves into one array

# list = [2, 6, 5, 1, 7, 4, 3]
#    [2 6 5 1]         [7 4 3]
#  [2 6]   [5 1]       [7 4]     [3]
# [2] [6]  [5] [1]     [7] [4]    |
# Now, we merge them.             |
#  [2 6]    [1 5]        [4 7]    ^
#     [1 2 5 6]              [3 4 7]
#              [1 2 3 4 5 6 7]

# TODO LET'S WRITE CODE

def merge_sort(arr):
    if len(arr) > 1:  # if the length is smaller than one, we are good to return
        left_arr = arr[:len(arr) // 2]
        right_arr = arr[len(arr) // 2:]

        # recursion
        merge_sort(left_arr)  # divides array until size becomes 1
        merge_sort(right_arr)

        # merge step
        i = 0  # left list index
        j = 0  # right list index
        k = 0  # merge sort array
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1  # compares the elements of two subarrays and merges them
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1  # copies the remaining left array elements, if there is any

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1  # copies the remaining right array elements, if there is any
    return arr


# list = [2, 6, 5, 1, 7, 4, 3]
# print(merge_sort(list))


# factorial

def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    return n


# print(factorial(4))


def fibonacci(n):  # n in this is the position of the fibonacci numbers
    # 1, 1, 2, 3, 5
    # if n = 6, (n-1) + (n-2) = n so ... 5 + 3 = 8 and so on
    if n > 2:  # it has to be greater than 2 so that it can find the positions of n-1 and n-2
        return fibonacci(n - 1) + fibonacci(n - 2)
    return 1


# fibonacci(1)
# is 1 > 2??? no
# returns 1

# fibonacci(3)
# is 3 > 2??? yes
# return fibonacci(3-1) + fibonacci(3-2) or return 1 + 1

# f4
# return f(4-1) + f(4-2) or return 1 + 2

# print(fibonacci(5))


# TODO challenges palindrome and binary search


def isPalindrome(word):  # return true if word backwards == word forwards. else false
    if len(word) == 1:  # single letters should always be true
        return True
    elif word[0:1] == word[len(word) - 1]:  # if this already starts out as false, we do not need to go further
        return isPalindrome(word[1:len(word) - 1])  # this returns the next word without the first and last letters
    return False


def palllydrom(str):  # Bruh
    return str == str[::-1]


# print(isPalindrome("obo"))
# print(palllydrom("obo"))


def binarysearch(target, array, start, end):  # Doesn't sort. Instead finds target from array using recursion
    print("******************************************************")
    print(f'The start is {start}')
    print(f'The end is {end}')
    print(f'The target is {target}')
    print(f'The array is {array}')
    middle_val = array[(start + end) // 2]  # gets the middle
    print(f'The middle value is {middle_val}')
    print("*******************************************************")
    if target == middle_val:
        return (start + end) // 2
    elif middle_val > target:
        return binarysearch(target, array, 0, (start + end) // 2)  # supposed to look through left half and find target
    elif middle_val < target:
        if end - start == 1:
            if target != array[len(array) - 1]:
                return False
            return end
        return binarysearch(target, array, (start + end) // 2, end)  # supposed to look through right half and find target
    return False  # returns false if there is no target in the array.


list = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
print(binarysearch(36, list, 0, len(list) - 1))



