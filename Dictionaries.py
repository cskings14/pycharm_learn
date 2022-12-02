customer = {
    'name': 'John Smith', # these are key value pairs
    'age': 30,
    # 'age': 40,   cant do this
    'is_cool': True

}

print(customer['name'])

print(customer.get('bday', 'June 5, 2003')) # adds a key value

customer['name'] = 'LeBron James'
print(customer)

# TODO CHALLENGE: make a converter which gets numbers and changes them int letters

pnum = input('Phone: ')
full_change= ''
for num in pnum:
    if num == '1':
        full_change += 'One '
    if num == '2':
        full_change += 'Two '
    if num == '3':
        full_change += 'Three '
    if num == '4':
        full_change += 'Four '
    if num == '5':
        full_change += 'Five '
    if num == '6':
        full_change += 'Six '
    if num == '7':
        full_change += 'Seven '
    if num == '8':
        full_change += 'Eight '
    if num == '9':
        full_change += 'Nine '
    if num == '0':
        full_change += 'Zero '

print(full_change)

# Lol that has no dictionarires... Try again

phonenum = input('Phone: ')
digits_converts = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four'
}

output = ''

for ch in phonenum:
    output += digits_converts.get(ch, '!') + ' '# if it not the number 1-4, it will print a ! instead

print(output)