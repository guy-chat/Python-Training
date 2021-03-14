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

