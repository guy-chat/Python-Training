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

'''

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

#one last test omfg
  
#replit last test 

#test pythonista 1.1
#test pythonista 1.2

#replit 1.1
#replit 1.2
#replit 1.13 
