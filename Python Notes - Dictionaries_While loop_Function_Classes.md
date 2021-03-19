Python Crash Course - Introduction to Programming
# Ch 6 - Dictionaries

## A Simple Dictionary
Consider a game, where an 'Alien' in this game has a 'green' color and values '5' points. You can store info about this 'Alien' in the game by using `Dictionary`.

```python
alien_1 = {'color': 'green','points' : 5}
print(alien_1['color']) #print color of alien_1
print(alien_1['points'])	
```
```Txt
green
5
```
A `dictionary` in Python is a collection of ***key-value pairs***. Each `key` is connected to a `value`, and you can use the `key` to access the associated `value`. 
From above, in Python, a dictionary is wrapped by `{ }` and every key is connected to a value by a `:`.

## Accessing a `value` 
Eg
```python
alien_1 = {'color': 'green','points' : 5}
print(alien_1['color']) #print the color of alien_1
print(alien_1['points']) #print alien_1's point

new_points = alien_1['points']
print('\nYou just earned ' + str(new_points) + ' points!')
```
```txt
green
5

You just earned 5 points!
```
## Adding new ***Key-Value*** pairs
```python
alien_1 = {'color': 'green','points' : 5}
print(alien_1)
print('\n')
alien_1['x_coord'] = 0 #add 2 more key-value pair for alien_1 
alien_1['y_coord'] = 25
print(alien_ 1)
print(alien_1['x_coord'])
```
```txt
{'color': 'green', 'points': 5}


{'color': 'green', 'points': 5, 'x_coord': 0, 'y_coord': 25}
0
```

## Modify values in a `dictionary`

Same method as how you add new value, simply replacing the `key-pair` values

Eg

```python
alien_1 = {'color': 'green','points' : 5}
print("Alien's color is " + alien_1['color'])

alien_1['color'] = 'yellow' #simply replace 'green' with 'yellow'
print("ALien's new color is " + alien_1['color'])
```

```txt
Alien's color is green
ALien's new color is yellow
```

### Sophisticated Example

Track the position of an alien that can move at different speeds. Storing a value for Alien's current speed and use it to determine how far to the right the alien should move.

```python
alien0 = {'x_pos' : 0, 'y_pos' : 0, 'speed' : 'slow'}
print('Original pos is: '+ str(alien0['x_pos']))

#new position
if alien0['speed'] == 'slow':
    delta_x = 1
elif alien0['speed'] == 'medium':
    delta_x = 2
else:
    #Fast alien
    delta_x = 3

#alien with its new position
alien0['x_pos'] = alien0['x_pos'] + delta_x
print('New x position: ' + str(alien0['x_pos']))    
```
```txt
Original pos is: 0
New x position: 1
```
## Removing Key-value pair with `del` statement

```python
kate = {'hobby1' : 'anime', 'hobbie2' : 'overwatch'}
print(kate)
#deleting hobby1 from kate 
del(kate['hobby1'])
print(kate)
```

## Dictionary with similar objects
You should practice to move to the next line rather than having a single long line of code.
```python
#Dictionary of similar objects
favorite_game = {
	'guy' : 'dota2',
	'kate' : 'overwatch',
	'gunn' : 'valorant',
	'kaye' : 'icarus'
}

print("Guy's favorite game is " +
	favorite_game['guy'].title() +
	'.')
```
```txt
Guy's favourite game is Dota2.
```	
## Looping through a Dictionary

To use a `for` loop with dictionary you need to use 2 variables after for `for k,v in a_dict` where `k` here represents 'key' and `v` for 'value' in 'key-value' pair

```python
user0 = {
	'username' : 'kate_chat',
	'first' : 'kate',
	'last' : 'chat'
}

for k,v in user0.items():
	print('\nKey : ' + k)
	print('Value : ' + v)
``` 
```txt
Key : username
Value : kate_chat

Key : first
Value : kate

Key : last
Value : chat
```
***Note that looping through a dictionary wont always return values in the order (like the example) they were stored. Python doesn't care the stored order, it only cares the connection between key-value***

## Accessing just `key` and `value` in `key-value` pairs
```python
favorite_game = {
	'guy' : 'dota2',
	'kate' : 'overwatch',
	'gunn' : 'valorant',
	'kaye' : 'icarus'
}

for key in favorite_game.keys():
	print(key.title())
#looping through the keys is actually the default behaviour when looping through a dictionary
#That's why for loop below has the same result as for loop above 	
for k in favorite_game:
	print(k.title())
	
print('\n')
	
for val in favorite_game.values():
	print(val.title())
```
```txt
Guy
Kate
Gunn
Kaye
Guy
Kate
Gunn
Kaye

Dota2
Overwatch
Valorant
Icarus
```	

