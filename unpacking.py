coordinates = (1, 2, 3)
coordinates[0] * coordinates[1] * coordinates[2]
# that takes too long. Let's try something else

x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

# also takes too long. Let's unpack this

x, y, z = coordinates
# x * y * z



