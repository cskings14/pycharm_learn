def secondSmallestValueIndex(arr):
    smallval = 0
    ssmallval = 1
    for i in range(1, len(arr)):

        if arr[ssmallval] < arr[smallval]:
            smallval, ssmallval = ssmallval, smallval

        if arr[i] < arr[smallval]:
            ssmallval = smallval
            smallval = i

        if arr[i] < arr[ssmallval] and ssmallval != smallval and i != smallval:
            ssmallval = i
    return ssmallval


array = [200, 99, 55, 5, 99, 0]

print(secondSmallestValueIndex(array))


