#Sets


includes a data type for sets.
Curly branes or the set() function can be used to create set.

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)		# show that duplicates have been removed

'orange' in basket 				# fast membership testing
'crabgrass' in basket


Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a                                 # unique letters in a
a - b                             # letters in a but not in b
a | b                             # letters in a or b or both
a & b                             # letters in both a and b
a ^ b                             # letters in a or b but not both

a = {x for x in 'abracadabra' if x not in 'abc'}
a

--------

>>>Dictionaries

#Dictionaries

#Another useful data type build into Python is the dictionary

tel = {'jack': 4098, 'sape': 4139}
tel['sape']
tel['guido'] = 4127
tel

--------

del tel['sape']
tel['irv'] = 4137
tel

lest(tel) #Change to list

sorted(student) #Alphabet Sorting

'MgOo' in student

'MaMa' not in student

--------

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
dict(sape=4139, guido=4127, jack=4098)

when looping through Dictionaries

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
		print(k, v)
		Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'x' is not defined
>>> for x, y in enumerate(['tic', 'tac', 'toe']):
...     print(x, y)
...
0 tic
1 tac
2 toe
>>>

https:docs.python.org/3/tutorial/

