
# `Str()` Methods

*method* is an action that Python can perform on a piece of data

`.title()` makes the first letter in a word capital

`.upper()` or `.lower()` makes the data/word/str all *upper* or *lower cases*

`title()` `.upper()` and `.lower()`  function doesn't require addition info, hence, ***empty parenthesis***

```python
name = 'gUy BHumiPat'
print(name.title())
print(name.upper())
print(name.lower())
```
```txt
>>> Guy Bhumipat
>>> GUY BHUMIPAT
>>> guy bhumipat
```
## combine/concatenate strings

Python uses `+` symbol to combine/concatenate strings

```python
first_name = 'guy '
last_name = 'chat'
full_name = first_name + last_name
print(full_name)
print('Hello, ' + full name.title() + '!')
```
```txt
>>> guy chat
>>> Hello, guy chat!
```
# Whitespace in strings
## Adding Whitespace
add tab `\t`, add new line `\n`

```python
print('Python')
print('\tPython')
print('Language:\nPython\n\tJava')
```
```txt
>>> Python
>>>     Python
>>> Language:
Python
    Java
```

## Stripping Whitespace

you can remove **whitespace* by using `.strip() .lstrip()` and `.rstrip()` 

`.strip()` removes **whitespace* on both left and right side of the variable
eg

```python
x = ' python '
print(x.strip())
>>> 'python'

```

whereas  `.rstrip() and .lstrip()` only removes either *whitespace* on the left or right side of the variable

```python
x = ' python '
print(x.rstrip())
>>> ' python'
print(x.lstrip())
>>> 'python '
```
# Single quote vs Double quote?

Double quote is used to ensure that when you include *apostrophe* in your string it doesnt get confused because you'll get syntax error when u try to do that with single *apostrophe*

# Type error

*Type error with `str()` function*

<span style="background-color:yellow">You cannot combine type `int` with type `str`</span>
Eg

```python
age = 23
message = "Happy " + age + "rd Birthday!"

print(message)
```
```txt
>>> TypeError: Can't convert 'int' object to star implicitly
```

Have to convert `int` to `str` type first

```python
age = 23
msg = "Happy " + str(age) + "rd Birthday!"
print(msg)
```
```txt
>>> 'Happy 23rd Birthday!"
```
### <span style="color:red">How to write comment</span>
```python
msg = 23 #type int msg is 23
```

# List

In Python `[]` indicates a `list` individual elements are separated by `,` and you can access elements in a list by specifying *index* in the parenthesis, which starts from `0` in python and you can access the last element in a list from `-1`
```python
bic = ['trek','red','green','chewy']
print(bic)
print(bic[0].title())
print(bic[1]) #second element
print(bic[-1]) #last element
```

```txt
>>> ['trek','red']
>>> Trek
>>> red
>>> chewy
```
Accessing a `list` and use concatenation
```python
msg = "My first bike's name is" + bic[-1].title() + '.'
```
```txt
>>> My first bike's name is Chewy.
```

## Change/Add/Remove elems in a list

You can simply replace/change the value of an element in a list by redefining the element's value

```python
car = ['toyota','honda','ferrari']
print(car)
car[1] = 'subaru' #this replaces 'honda' with 'subaru'
print(car)
```
```txt
>>> ['toyota','honda','ferrari']
>>> ['toyota','subaru','ferrari']
```
You can add/append element (after the last elem) to the `list` by using `.append(data)`
Eg
```python
car.append('hyundai') #append 'hyundai' to car list
print(car)
```
```txt
>>> ['toyota','subaru','ferrari','hyundai']
```

## Creating a list dynamically from empty
```python 
car = [] #empty list
car.append('honda')
car.append('supra')
car.append('toyota')
print(car)
```
```txt
>>>  ['honda','supra','toyota']
```
Lists are commonly build this way, to store data in a program as users input them while the program is running.

## Insert elements into a list w/ `.insert(a,b)` fn

Use `insert(a,b)` function where `a` is the list index and `b` is the new data value
```python
car = ['toyota','honda','ferrari']
car.insert(1,'lambo') #insert 'lambo' as the second element in car list
print(car)
```
```txt
>>> ['toyota','lambo','honda','ferrari']
```

## Remove element w/ `del X[i]` statement

w/ `del` statement u can delete an item from a `list`

```python
car = ['toyota','honda','ferrari']
del car[1] #delete second elem from car list
print(car)
```
```txt
>>> car = ['toyota','ferrari']
```

## Remove last elem from list with `.pop()` or certain element with `.pop(i)` method

### `.pop()` method
```python
car = ['toyota','honda','ferrari']
print(car)
popped_car = car.pop() #last elem removed from car the removed elem is defined as popped_car
print(car)
print(popped_car)
```
```txt
>>> ['toyota','honda','ferrari']
>>> ['toyota','honda']
>>> ferrari #popped_car
```
### `.pop(i)`
```python
car = ['toyota','honda','ferrari']
second_owned = car.pop(1)
print('The second car I owned is a ' + second_owned.title() +'.')
```
```txt
>>> ['toyota','honda','ferrari']
>>> ['toyota','ferrari']
>>> honda
```
So to choose whether you use `del` statement or `.pop()` fn, simply consider whether u need to reuse the element u removed or not.

## `X.remove(some_val)` Remove an element from a list

This .remove(some_val) is used when u know the value of the element u want to remove from the list

```python
car = ['toyota','honda','ferrari']
car.remove('honda')
print(car)
```
```txt
>>> ['toyota','ferrari']
```

## Sorting list *alphabetically* and *permanently* w/ `.sort()` method

`.sort()` method changes the order of the list into an ***alphabetical order***. This change is ***permanent*** and cannot be ***reverted***.
```python
car = ['c','a','x','d']
car.sort()
print(car)
```
```txt
>>> ['a','c','d','x']
```
You can reverse the alphabetical order by passing the argument `reverse=True` in `.sort()` method
Eg
```python
car.sort(reverse=True)
print(car)
```
```txt
>>>['x','d','c','a']
```
## Sorting list *alphabetically* *temporarily* with `sorted(some_list)` function

It lets you display the order alphabetically without affecting the actual order of the list.
Eg

```python
car = ['bugatti','audi','tesla']
print(car)
print(sorted(car))
print(car) #this will print the same as prior
print(sorted(car,reverse=True)) #1
```
```txt
>>> ['bugatti','audi','tesla']
>>> ['audi','bugatti','tesla']
>>> ['bugatti','audi','tesla']
>>> ['tesla',''bugatti','audi'] #1
```

U can also apply `reverse=True` in `sorted()` this makes `sorted(list,reverse=True))` #1

## Print list in a reverse order (not alphabetically reverse) w/ `X.reversed()` method

```python
a_list = ['c','a','b','m']
print(a_list.reverse())
```
```txt
>>> ['m','b','a','c']
```
*tips you can `.reverse()` twice to return list into its original order
## Find Length of a list with `len(some_list)`

```python
a_list = ['c','a','b','m']
print(len(a_list))
```
```txt
>>> 4
```

## Index Errors look like this

```python
a_list = ['c','a','b','m']
print(a_list[4]) #5th index doesn't exist
```
```txt
>>> Traceback (most recent call last):
>>>  File "a_list.py", line 3, in <module> #arbitrary
>>>     print(a_list[4])
>>> IndexError: list index out of range
```

Index error occurs when Python can't figure out the index u requested.

# LOOPS
## `for` loop
When u want to do same action with every item in a list, you can use Python's `for` loop

```python
magicians = ['alice','nancy','alex']
for magician in magicians:
    print(magician)
```

You can read this code as 'For every magician in the list of magicians, print the magician's name'. 

*note you can change `magician` to other name, since you can choose any name you want for the temporary variable that holds each value in the list.

```txt
>>> alice
>>> nancy 
>>> alex 
```
Python will repeat the lines until it can no longer, in this case after the last value in the list `'alex'` has been printed, then Python moves on to the next line in the program. Here, nothing comes after the `for` loop, so the program stops.

## More work within `for` loop

```python
magicians = ['alice','nancy','alex']
for magician in magicians:
    print(magician.title() + ', nice trick!') #apply .title() to magician in each loop
```

```txt
>>> Alice, nice trick!
>>> Nancy, nice trick!
>>> Alex, nice trick!
```

You can write ***as many lines of code as you like in `for` loop***.

*Note that every indented line under a `for` loop is considered as ***inside the loop***, and each indented line is executed once for each value in the list. This means that u can do as much work as you like to each value in the list.

## Doing something after a `for` loop
```python
magicians = ['alice','nancy','alex']
for magician in magicians:
    print(magician.title() + ', cool!')
    print("Can't wait ur next trick, " + magician.title() + '.\n')
print('Thanks everyone for coming!')
```
```txt
>>> Alice, cool!
>>> Can't wait ur next trick, Alice.
>>> 
>>> Nancy, cool!
>>> Can't wait ur next trick, Nancy.
>>> 
>>> Alex, cool!
>>> Can't wait ur next trick, Alex.
>>> 
>>> Thanks everyone for coming!
```

# IndentationError

Python uses indentation to determine if a line of code is connected to the line above it.

```python
magicians = ['alice','nancy','alex']
for magician in magicians:
print(magician)
```

```txt
>>>  File 'magician.py', line 3
>>>    print(magician)
>>> IndentationError: expected an indented block
```
## Indenting unnecessarily
If you indent something that is unnecessary, Python will inform you about the unexpected indent.

```python
msg = 'Hello World'
    print(msg)
```
```txt
>>>  File 'hello_world.py', line 2
>>>     print(msg)
>>> IndentationError: unexpected indent
```
There is no need to indent `print` statement, because it doesn't *belong* to the line above it.

*Note that the error is different in description from 'expect an indented block' to 'unexpected indent'

## Forgetting the colon :
If you forget colon, you'll get a *syntax* error because Python doesn't know what you're trying to do. 

```txt
>>> SyntaxError: invalid syntax
```

# *Logical* error

*logical error* is when the syntax is a valid Python code, which means the Python was able to run the program successfully, but it did not produce the desired result. 

# *Parsing* error

*Parsing error* is a subset of *Syntax error* that occurs when you are missing a parenthesis

# *Unmatched*

Also a subset of *Syntax error* when you have too many parenthesis. 

# Making Numerical lists
## Using the `range()` function

`range()` function makes it easy to generate a series of numbers
Eg

```python
for value in range(1,5)
    print(value)
```
```txt
>>> 1
>>> 2
>>> 3
>>> 4
```

As u can see Python only prints up to 4 and not 5, this is a result of the ***off-by-one*** behaviour in programming. The program starts at the first value you give, but stops when it reaches the value you provide.

## use `range` to make a list of numbers
```python
numbers = list(range(1,5))
print(numbers)
```

```txt
>>> [1,2,3,4]
```

Within `range` function u can tell Python to skip numbers in the given range.
Eg

```python
even_no = list(range(1,11,2))
print(even_no)
```
```txt
>>> [2,4,6,8,10]
```
The `c` in `range(a,b,c)` tells Python how many numbers to skip within the given `a` and `b` range.

### Exercises with `for` loop and `range`

```python
squares = []
for value in range(1,11)
    squares.append(value**2)
print(squares)    
```

```txt
>>> [1,4,9,16,25,36,49,64,81,100]
```

As u go, sometimes using temporary variable makes your code easier to read; other times it makes the code unnecessarily long. 

## Simple Statistics with a List of Numbers
`min(a)` returns minimum value in `a` list
`max(a)` returns maximum value in `a` list
`sum(s)` returns the sum of all the values in `a` list
*works with float, integers 

```txt
>>> numbers = [1,4,9,16,25,36,49,64,81,100]
>>> min(numbers)
1
>>> max(numbers) 
100
>>> sum(numbers)
385
```

# List Comprehensions

Allows you to generate this same list in just one line of code.

```python
squares = [value**2 for value in range(1,11)]
print(squares)
```
```txt
>>> [1,4,9,16,25,36,49,64,81,100] 
```

## Slicing a list

U can slice a list by specifying the index of the 1st and last element you wanna work with, just like `range()`, Python stops one item before the 2nd index u specify.


```python
players = ['kim','jen','ruby','lola','ken']
print(players[0:2]) #prints first to second object
print(players[1:4]) #prints second to third object
print(players[:3]) #this prints the first three object / if slicing without specifying first index Python will start from beginning
print(players[2:]) #slice without 2nd index will print from first index to end of the list
print(players[-3:]) #this prints the last three object in the players list
```
```txt
>>> ['kim','jen']
>>> ['jen','ruby','lola']
>>> ['kim','jen,'ruby']
>>> ['ruby','lola','ken']
>>> ['ruby','lola','ken']
```

## Copy a list without overwriting original list

Use `[:]` after the original list u wanna copy

```python
my_food = ['pizza','pasta']
frd_food = my_food[:] #here frd_food is a copy of my_food 
my_food.append('salt')
frd_food.append('sugar')
print(my_food)
print(frd_food)
```
```txt
>>> ['pizza','pasta','salt']
>>>  ['pizza','pasta','sugar']
```
You can't just overwrite without `[:]` as you can see below 
```python
my_food = ['pizza','pasta']
frd_food = my_food #no [:], my_food == frd_food
my_food.append('salt')
frd_food.append('sugar')
print(my_food)
print(frd_food)
```
```txt
>>> ['pizza','pasta','salt','sugar']
>>> ['pizza','pasta','salt','sugar']
```
Now my_food and frd_food is the same, not a copy that's why they're both the same.

# Tuples

In Python, list works well for storing sets of items that change throughout a program. But sometimes you want a list of items that cannot change. These values that can't change are called ***immutable***, immutable list in Python is ***tuple***.

Tuples use `()` instead of `[]` in a usual `list` but the way you access elements in a`tuple` is the same as `list`.

```python
a_tuple = ('v','c','a','d')
print(a_tuple[1])
print(a_tuple[-1])
print(a_tuple[0:2])
```
```txt
>>> c
>>> d
>>> ('v','c','a')
```
However, you cannot change or modify `tuple` in anyway. This includes all methods `.reverse()` `.insert(a,b)` `.append()` `.sort()`

Surprisingly, you can use `sorted(X)` which converts the `tuple` into a `list` as it doesn't affect the original `tuple`

```python
a_tuple = ('v','c','a','d')
print(sorted(a_tuple)) #sorted() converts tuple into a list and sort it in that instance
print(a_tuple)
```


```txt
>>> ['a','c','d','v']
>>> ('v','c','a','d') #original tuple still the same that's why sorted() function works
```

You can use `for` loop to access elements in a tuple just like a list

```python
a_tuple = (200,30)
for value in a_tuple:
    print(value)
```

```txt
>>> 200
>>> 30
```
The only way to change values inside a tuple is to assign a new value to the variable that holds a `tuple`.
Eg

```python
a_tuple = (200,30)
print(a_tuple)
a_tuple = (400,30)
print(a_tuple)
```
```txt
>>> (200,30)
>>> (400,30)
```

# Styling your code

When someone makes a change to Python language, they write  ***PEP (Python Enhancement Proposal)***, which instructs Python programmers how to style their code. 

Between writing code that's easier to write vs easier to read. Always choose 'easier to read' as you'll often be sharing it with others + debugging purposes.

## Indentation

***PEP*** recommends 4 spaces per indentation level.

## Line length

***PEP*** recommends no more than 80 characters per line.

## Blank lines

Use Blank Lines to group parts of ur program. 

Blank lines don't affect how ur code runs, but it affects the readability of your code. 


# Introducing `If` statement 

Use to write conditional tests, to check any condition of interest

Eg

```Python
cars = ['audi','bm','subaru','toyota']

for car in cars:
  if car == 'audi':
    print(car.upper())
  else:
    print(car.title())
```
Here only 'audi' will be printed in upper cases, while the rest will be printed with title cases.

```txt
>>> AUDI
>>> be
>>> subaru
>>> toyota
```

## Conditional Tests

### Checking for equality
Conditional tests compare current value of variable to a specific value of interest, this can be done with `==`, which is a `Boolean` type. The result of `==` can be either `True` or `False`.

```python
#console
>>> car = 'bmw'
>>> car == 'bmw'
True
```
In the case where `==` doesn't match.
```python
#console
> car = 'aid'
> car == 'aids'
False
```
*Note that `==` Boolean is case sensitive, this means `Audi==audi` will result in `False` However, you can convert the variable's value to lower cases before doing the comparison.

```Python
#console
> name = 'Guy'
> name.lower() == 'guy'
True
> name
'Guy'
```
As you can see the original value of name doesn't change.

### Checking for inequality

You can use `!=` to check for inequality. 
Eg
```Python
topping = 'mushrooms'

if topping != 'anchovies':
  print("Hold the anchovies!")
```
```txt
Hold the anchovies
```
You can use this to check for numerical values as well. This is good when you are writing a question and trying to compare answers.
```python
ans = 17
if ans!= 13:
  print('Incorrect answer, pls try again!')
```
```d
Incorrect answer, pls try again!
```
## Checking multiple conditions with `and`

```python
#console
>>> age0 = 18
>>> age1 = 20
>>> age0 >= 18 and age1 >= 20
True
>>> age0 >= 18 and age1>= 21
False
```

## Checking whether a value is not in a list using `not`

Here you can use `if` statement to check whether a value is in a `list` or not, a good example is when you are checking for a banned user.

Eg

```python
banned_user = ['andy','tony','charles']
user = 'faye'

if user not in banned_user:
	print(user.title() + ', welcome!')
else:
	print(user.title() + ', plz fk off!')
```

```txt
Faye, welcome!
```

Because `user`  is `'Faye'` isn't in `banned_user` she receives the `welcome!` msg, if `user` was `'andy','tony' or 'charles'` they would have received `'plz fk off'` msg.

## Boolean expressions

A `Boolean` value is either `True` or `False`, and is often used to keep track of certain conditions, such as whether a game is running or a user can edit website content.

Eg

```python
game_active = True
can_edit = False
```

Its an efficient way to track state of a program/ condition that's important to ur program.

# `if` statement in action

Indentation plays same role in `if` statement as it did in `for` loops. All indented lines will be executed if the test condition passes, and will be ignored if the test condition fails. You can have as many lines as you want following the `if` statement.

Eg

```python
age = 14
if age >= 14:
    print('No longer a kiddo')
    print('But still a brat, haha!')
```

```txt
No longer a kiddo
But still a brat, haha!
```

`age = 14` which satisfies test condition for `age>=14` so indented block after `if` statement is executed.

## `if else` statement

If the test condition fails, you'll want something to occur instead, you can use `else` for this

Eg

```python
age = 13
if age >= 14:
    print('No longer a kiddo')
    print('But still a brat, haha!')
else:
    print('Not only a brat, but also a kiddo, hahaha!')    
```

```txt
Not only a brat, but also a kiddo, hahaha!
```

In this case `age = 13` which fails the `age>=14` condition so the indented block after `else` statement gets executed.

## `If - elif - else` Chain

`if-elif-else` is used when you need to test ***more than 2 conditions*** at the same time! Python executes only one block in the `if-elif-else` chain. It runs each conditional test in order until one passes, the code block following that test condition is executed and the rest of the `if-elif-else` code is ignored.

Eg

```python
grade = 55
if grade <= 49 :
    print('F')
elif grade <= 59:
    print('P')
elif grade <= 69:
    print('C')
elif grade <= 79:
    print('D')
else:
    print('HD')    
```

```txt
P
```

**Note that you can use as many `elif` block as you like as shown above. And there's no need for `else` statement after `elif` block.

```python
grade = 100
if grade <= 49 :
    print('F')
elif grade <= 59:
    print('P')
elif grade <= 69:
    print('C')
elif grade <= 79:
    print('D')
elif grade <= 100:
    print('HD')    
```

```txt
HD
```

The code above runs just fine without `else` statement, in this case if you make `grade = 101` console simply won't return anything.

## Multiple `if` statements for testing multiple conditions

