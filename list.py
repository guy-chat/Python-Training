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