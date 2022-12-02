list = [1, 2, 7, 33, 64, 86, 3, 7, 9, 101, 11, 132, 3, 26, 68, 144]



def linear_search(list_nums, value):
    for item in list_nums:
        if item == value:
            return list_nums.index(value)
    return -1

print(linear_search(list, 11))


def selection_sort(list_nums):
    for i in range(len(list_nums) - 1):
        minIndex = i
        for j in range(i+1, len(list_nums)):
            if list_nums[j] < list_nums[minIndex]:
                minIndex = j

        list_nums[i], list_nums[minIndex] = list_nums[minIndex], list_nums[i]
    return list_nums


print(selection_sort(list))


def insertion_sort(list_nums):
    for i in range(1, len(list_nums)):
        possible_index = i

        while list_nums[i-1] > possible_index and i>0: # if the number to the left is higher
            # it will switch the numbers and then go through the rest of the list until i changes
            #the i>0 is so that there is not negative indexing
            list_nums[i], list_nums[i-1] = list_nums[i-1], list_nums[i]
            i = i - 1
    return list_nums



print(selection_sort(list))







