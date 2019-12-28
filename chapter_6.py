# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 08:41:39 2019

@author: Osheen
"""

############Chapter 6 ##################

print("6.1")
information ={'first_name' : 'neha', 'last_name': 'mishra' , 'city' : 'dubai'}
print(information)
print(information['first_name'])
print(information['last_name'])
print(information['city'])

print("\n6.2")
fav_number= {'ravi': 45 , 'pooja':77, 'riki':9, 'kuku':87}
v1=fav_number['ravi']
v2=fav_number['pooja']
v3=fav_number['kuku']
print("Favorite number of ravu " + " seems to be  " + str(v1))
print("Favorite number of pooja " + " seems to be  " + str(v2))
print("Favorite number of kuku " + " seems to be  " + str(v3))

print("\n6.3")
language={'print':'print the output of the code',
          'int':'to conver the value to integer',
          'for': 'to access each value in the list',
          'list':'too make a lis of values',
          'if': 'conditional operator'}
for i, v in language.items():
    print("\nkey: " + i)
    print("value: " + v)

print("6.4")
rivers = {'nile':'egypt', 'africa': 'amazon' , 'india':'ganga'}
for key,value in rivers.items():
    print(key.title() + " is the major river of " + value.title() + ".") 
for key in rivers.keys():
    print(key.title())
for value in rivers.values():
    print(value.title())


print("6.5")
poll= {'osheen', 'gigi', 'jon', 'nina', 'brian','laura','jana'}    
votes={'osheen','jon','brian'}
for i in sorted(poll):
    
  if i in sorted(votes):
    print(i.title()+ " Thnaks for your vote.")
  else:
    print(i.title()+ " ,you are nvited to vote")



aliens =[]

for i in range (30):
    new_alien ={'color' : 'green', 'speed' : 'slow','points':'10'}
    aliens.append(new_alien)

for i in aliens[6:12]:
    if i['color']=='green':
        i['color']='yellow'
        i['speed']='medium'
        i['points']='5'
        
for i in aliens[0:13]:
    print(i)
print("...")

print("lebgth of th estring is " + str(len(aliens)))


print("6.7")

people_1 ={'first_name' : 'neha', 'last_name': 'mishra' , 'city' : 'dubai'}
people_2 ={'first_name' : 'rohit', 'last_name': 'sharma' , 'city' : 'delhi'}
people_3 ={'first_name' : 'mohit', 'last_name': 'mittal' , 'city' : 'goa'}
people=[people_1,people_2,people_3]

for i in people:
    print(i)
    
print("6.8")

gigi= {'dog':'jon'}
phephe ={'cat' :'sara'}
amy ={'pig' :'ron'}
pets=[gigi, phephe,amy]

for i  in pets:
    print(i)
print("...")

print("/n6.9")

places={'japan':'ravi',
        'africa':'raj',
        'india':'rohit'}

for i ,v in places.items():
    print(v +"'s favorite place is " + i)

print("\n6.10")  

fav_number= {'ravi':[ 45,20,33] , 
             'pooja':[77,67,98],
             'riki':[9,99,100], 
             'kuku':[87,88,45]}
for names,numbers in fav_number.items():
    print("\n" + names + "'s favorite numbers are:")
    for number in numbers:
        print("\t" + str(number))

print("/n6.11")

cities= {
        'chandigarh':{
        'info': 'This is the city beautiful',
        'population' : '6001000',
        'fact':'most planned'
        },
        'delhi':{
         'info':'is the capiital of India',
         'population':'1000000',
         'fact':'really unsafe'
            },
        'mumbai':{
         'info':'is the movie capital',
         'population':'40000000',
         'fact':'very expensive to live in'}
        }
for i,j in cities.items():
    print("\nThe name of city is " + i)
    information= j['info']
    population=j['population']
    fact=j['fact']
    print("\t" + information +"\n\tHas a population of "+population
          + "\n\tThe fact is that it is " +fact )


