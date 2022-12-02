# 1.

def fun1(x, y):
    if x == 0:
        return y
    else:
        return fun1(x - 1, x + y)


# TODO What does this do???
# It should add y to x than x-1 than x-2 until x == 0. It then returns y.
#
# print(fun1(3, 5))  # 5 + 3 + 2 + 1 = 11


# correct

# 3.

def fun2(n):
    if (n == 1):
        return 0
    else:
        return 1 + fun2(n // 2)

# 36 --> 1 + fun2(18) --> 1 + 1 + fun2(9) --> 1 + 1 + 1 + fun2(4) --> 1 + 1 + 1 + 1 + fun2(2) --> 1 + 1 + 1 + 1 + 1 = 5
# TODO What does this do???
# This looks a bit like modulus.
# It should get n divided by 2 until n == 1 or lower. Then add that to 1.

# print(fun2(128))  # should be 1 + (5 % 2) which is 1 with the /2 is 1/2 so the answer is 1.5


# My answer was almost correct. If it is an odd number, an error will occur. If it is even, my thought process is
# correct.


def fun3(n):
    if (n == 0):
        return
    print(n)
    fun3(n - 1)


# TODO What does this do???
# 6 --> fun3(3) --> fun3(1) --> fun3(0)

# fun3(6)
# I was pretty much correct

# 2. write selection sort













def selection_sort(list_nums):
    for i in range(len(list_nums) - 1):
        minIndex = i
        for j in range(i+1, len(list_nums)):
            if list_nums[j] < list_nums[minIndex]:
                minIndex = j

        list_nums[i], list_nums[minIndex] = list_nums[minIndex], list_nums[i]

    return list_nums

# now recursively... where to start??? where to start???

arr = [-5, 3, 10, 7, 2, 22, 3]

def indexOfMinimumValue(a, min_val = 0):
    for i in range(len(a)-1):
        if a[min_val] > a[i]:
            min_val = i
    return a[min_val]
print(indexOfMinimumValue(arr))


def recurSelectionSort(a, i = 0):
    if (i == (len(a)-1)):
        return a
    for i in range(len(list) - 1):
        mindex = i
        if list[mindex] > list[i + 1]:
            list[i], list[mindex] = list[mindex], list[i]
    recurSelectionSort(a, i + 1)


# Calculate the minimum index from i -> a.length
# Swapping when i and minimum index are not same
 # Recursively calling selection sort function

