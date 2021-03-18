'''

bic = ['trek', 'red','green','chewy']
print(bic)
print(bic[0].title())
print(bic[1])
print(bic[-1])

car = ['toyota','honda','ferrari']
car.append('mistu')
car[1] = 'subaru' #this replaces 'honda' with 'subaru'
car.insert(1,'ducatti') #insert 'ducatti' as 2nd elem
del car[1] #delete second elem in car list
print(car)

car1 = ['toyota','honda','ferrari']
second_owned = car1.pop(1)
print('The second car I owned is a ' + second_owned.title() +'.')

dinner = ['kate','gunn','kaye']
print('Come to dinner ' + dinner[0].title() + '!')
print('Come to dinner ' + dinner[1].title() + '!')
print('Come to dinner ' + dinner[2].title() + '!')

bailer = dinner.pop(1).title()
print('come to dinner ' + dinner[1].title() + '!')
print(bailer + ' is no longer coming to dinner!')
dinner.insert(1,'mum')
print('but ' +dinner[1].title() + ' is coming instead!')
dinner[0] = 'pun'
dinner[1] = 'kim'
dinner[2] = 'net'
print('come to dinner ' + dinner[0].title() + '!')

dinner.insert(0,'syrup')
dinner.insert(len(dinner)//2,'france')
dinner.append('phoon')
print(dinner)
del dinner[-1]
del dinner[-1]
print(dinner)

squares = []
for value in range(1,11):
  squared_no = value**2
  squares.append(squared_no)
print(squares)  
print(sum(squares))

xo = [2.1,2.3,3]
print(min(xo))

my_food = ['pizza','pasta']
frd_food = my_food[:]
my_food.append('salt')
frd_food.append('sugar')
print(my_food)
print(frd_food)

b_tuple = ('b','a','c','e','x')
b_list = ['b','a','c']
b_list.insert(2,'d')
b_list.reverse()
print(b_tuple[2])
print(sorted(b_tuple))
print(b_tuple)



#if statement

cars = ['audi','bm','subaru','toyota']

for car in cars:
  if car == 'audi':
    print(car.upper())
  else:
    print(car.title())
    
# testing 123     
    
topping = 'mush'

if topping != 'anch':
  print('Hold anchovies!')



banned_user = ['andy','tony','charles']
user = 'faye'

if user not in banned_user:
	print(user.title() + ', welcome!')
else:
	print(user.title() + ', plz fk off!')
		
# 80-90
car = 'sub'
print(car == 'sub')
print(car == 'aud') 

car = 'Audi'
print(car.lower() == 'audi')

age = 13
if age >= 14:
    print('No longer a kiddo')
    print('But still a brat, haha!')
else:
    print('Not only a brat, but also a kiddo, hahaha!')    
  
  

grade = 100
if grade <= 49 :
    print('F')
elif grade <= 59:
    print('P')
elif grade <= 69:
    print('C')
elif grade <= 79:
    print('D')
elif grade <= 100: #no need for else after elif
    print('HD')    
    
    
#Multiple ifs

topping = ['mushrooms','extra cheese']

if 'mushrooms' in topping:
	print('Adding mush')
if 'extra cheese' in topping:
	print('Add cheese')
if 'garlic' in topping:
	print('Add garlic')
print('\nFinished your pizza!')	
			


prime_numbers = [1,3,5,7,11]
prime = 11
if prime in prime_numbers:
	print('Prime!')
else:
	print('xD')	

todays_available_toppings = ['mushroom','green pep','garlic']

topping_lists = ['mushroom','green pep','chilli','garlic','cheese']
requested_toppings = ['green pep','chilli','mushroom']

if len(requested_toppings) == 0:
	print('U sure u want plain pizza?') 
else:
	for topping in requested_toppings:
		if topping not in topping_lists:
			print('we dont have ' + topping.title() + ' in our toppings.')
		else:
			#if its in topping list now check today's availability
			if topping in todays_available_toppings:
				print('Adding ' + topping.title())
			else:
				print('Sorry, we are out of ' + topping.title() + ' today...')
print('\nThank u for ordering with us today!')				
				
'''
alien_1 = {'color': 'green','points' : 5}
print(alien_1)
print('\n')
alien_1['x_coord'] = 0
alien_1['y_coord'] = 25
print(alien_1)
print(alien_1['x_coord'])
                                                                                       
