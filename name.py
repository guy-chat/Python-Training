name = 'ada lovelace'
print(name.title())

name = ' Ada Lovelace'
print(name.upper())
print(name.lower())

first_name = 'ada '
last_name = 'lovelace'
full_name = first_name + last_name
print(full_name)

msg = 'Hello, ' + full_name.title() + '!'
print(msg)

print('\tpython')

print(f"Hello, {full_name.title()}!")
print(f"My bname is {first_name+last_name} and I am {sum([2,3,4])}")

print("Language:\nPython\nC\nJavaScript")

whitespace = 'python " '
nowhitespace = whitespace.rstrip()
print(whitespace)
print(nowhitespace)