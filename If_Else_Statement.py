


#Boolean Expression  -> True or False

print(20 > 10)
print(20 == 10)
print(20 < 10)
print(bool("Hello World"))
print(bool(20))


Python Conditions 

Equals						-> x == y
Not Equals					-> x!= y
Less than					-> x < y
Less than or equals to		-> x <= y
Greater than				-> x > y
Greater than or equal to	-> x >= y
Boolean OR 					-> x or y , x | y
Boolean AND 				-> x and y , x & y
Boolean Not 				-> not x


if -
else - 


#If Statement

x = 70
y = 60

if x > y:
	print("x is greater than y")

#Elif

x = 70
y = 70

if x > y:
	print("x is greater than y")
elif x == y:
	print("x and y are equal")

#Else

x = 50
y = 150
if x > y:
	print("x is greater than y")
elif x == y:
	print("x and y are equal")
else:
	print("x is less than y")

#Short Hand If

if x > y: print("x is greater than y") 
x is less than y
>>> x = 50
>>> y = 150
>>> print(x) if x > y else print(y)

#And is logical operator

>>> x = 50
>>> y = 40
>>> z = 100
>>> if x > y and z > x:
...     print("All Conditions are True")
...
All Conditions are True
>>> if x < y and z > x:
...     print("All Conditions are True")
... else:
...     print("Some COnditions are False")
...
Some COnditions are False

# OR is logical operator

>>> x = 50
>>> y = 40
>>> z = 100
>>> if x > y or z < y:
...     print("one of the conditions is True")
... elif x > y and z > y:
...     print("All conditions are True")
... else:
...     print("nothing else")
...
one of the conditions is True

>>> if x > y and z > y and z > x:
...     print("Answer 1")
... elif x == y or z == y or z > y and x > y:
...     print("Answer 2")
... elif z > y and y < x or z > y:
...     print("Answer 3")
... else:
...     print("Default")
...
Answer 1

>>> if x > y and z > y and x > z:
...     print("Answer 1")
... elif x == y or z == y or z > y and x > y:
...     print("Answer 2")
... elif z > y and y < x or z > y:
...     print("Answer 3")
... else:
...     prrint("Default")
...
Answer 2




#Nested If is if statements in if statements 



>>> if x > y :
...     print("x is greater than y")
... elif x >= y:
...     print("x is greater or equal to y")
... elif y < x:
...     print("y is smaller than x")
... else:
...     print("x is nothing")
...
x is greater than y
>>> if x == y:
...     print("Answer 1")
... elif x < y:
...     print("Answer 2")
... elif x <= y:
...     print("Answer 3")
... else:
...     print("default")
...
default