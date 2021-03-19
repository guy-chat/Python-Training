'''
alien_1 = {'color': 'green','points' : 5}
print("Alien's color is " + alien_1['color'])

alien_1['color'] = 'yellow'
print("ALien's new color is " + alien_1['color'])


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



kate = {'hobby1' : 'anime', 'hobbie2' : 'overwatch'}
print(kate)
#deleting hobby1 from kate 
del(kate['hobby1'])
print(kate)

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

user0 = {
	'username' : 'kate_cat',
	'first' : 'kate',
	'last' : 'chat',
	'favGame' : 'Overwatch'
}

for k,v in user0.items():
	print('\nKey : ' + k)
	print('Value : ' + v)

'''
favorite_game = {
	'guy' : 'dota2',
	'kate' : 'overwatch',
	'gunn' : 'valorant',
	'kaye' : 'icarus'
}

for key in favorite_game.keys():
	print(key.title())
for k in favorite_game:
	print(k.title())
	
print('\n')
	
for val in favorite_game.values():
	print(val.title())


