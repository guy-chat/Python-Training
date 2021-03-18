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

