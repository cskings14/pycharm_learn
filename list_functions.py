lucky_numbers = [1000, 99, 15, 16, 23, 42]
friends = ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby', 'Toby']



lucky_numbers.sort() # sorts it
lucky_numbers.reverse() # reverse sort
friends.extend(lucky_numbers) # puts everything in lucky nubers on friends
friends.append('Bruh') # puts bruh at the end
friends.insert(1, 'OOF') # inserts at position 1

print(friends)

friends.pop() # takes the last off

friends2 = friends.copy() # makes a new list that copies everything in friends

print(friends)
print(friends.index('Kevin'))
print(friends.count('Kevin'))

print(50 in friends) # checks if 50 is in the friends list

# TODO CHALLENGE: make a list that deletes duplicates

nums = [2, 2, 4, 6, 3, 4, 6, 1]

uniques = []

for num in nums:
    if num not in uniques:
        uniques.append(num)
print(uniques)







