'''
alien_1 = {'color': 'green','points' : 5}
print("Alien's color is " + alien_1['color'])

alien_1['color'] = 'yellow'
print("ALien's new color is " + alien_1['color'])

'''
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