# this whole process makes lists from strings based on the delimiter
problems = 'broke, pale, short, nerdy'

print(problems)

l = problems.split(", ") # this is the delimiter

print(l)

joined = ' and '.join(l)

print(joined)




