# Sequences,(Collections) and iterables
# https://docs.python.org/3/library/stdtypes.html

a = 1
b = 'hello'
c = 'James'

# Text (str object) '', "", 'Hello I am a string', "Hello I am a string",  format strings << look this up,
a_string = 'Hello' + b + c
print(a_string)

# Look up binary sequenceshttps://docs.python.org/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview

# Tuple (),(1,'Hello') , but also ('ANDREW',3, 'Fixed'), and  (23,'abc', ('inner',4,5),9,(1,2,4),('a','b',2,(1,2,3,4,5)))
a_tuple= (2,a,b,c,'Zorg')
print(a_tuple[2])

# List[], [1,2,'asbc',5,(4,'a',2),3], but also ['a',['a',2,3],['c',3,4]]
a_list= [a,b,c,a_tuple,a_string, [1,'d','v'],[1,[2,['x',3]],('a','f','k')]]
print(a_list[5])

# Set set() {"Ted",1,3,"a"} mutable–FrozenSet(immutable –hashable,can be used as a lookup a dictionary key)
a_set= {"Ted",1,3,"a","a"} # never repeat a value 
print(a_set) # not subscriptable{'a', 3, 'Ted', 1} # no order no repeats

# Dict{}, {'first_name':'Ted','last_name':'Zorg','Address':(123,'Street','Maitai','Nelson')} << look up maps
a_dict= {'first_name':'Ted','last_name':'Zorg','Address': (123,'Street','Maitai','Nelson')}
a_dict['last_name'] = "Zhefran"
print(a_dict['Address'])

# Making and using. Use the constructor to convert or "cast" to that type.

# Text (str object)
a_string= str(123)
a_string= '23'
a_string in a_string # << True

# AND to instantiate a sequence from an "iterable", i.e. another sequence

#  Tuple
a_tuple= tuple('abcZorg') #immutable
('a', 'b', 'c', 'Z', 'o', 'r', 'g')
a_tuple= a_tuple+ ('a',2,'3') # MAKES A NEW TUPLE WITH Added parts
('a', 'b', 'c', 'Z', 'o', 'r', 'g','a',2,3)
a_tuple= (a_tuple,) + (('a',2,'3'),) # MAKES A NEW TUPLE, made up of tuples
(('a', 'b', 'c', 'Z', 'o', 'r', 'g', 'a', 2, '3'), ('a', 2, '3'))

# List
a_list= list(a_tuple) #mutable
[('a', 'b', 'c', 'Z', 'o', 'r', 'g', 'a', 2, '3'), ('a', 2, '3')]
a_list= a_list+ [2,('x','z','z')]
[('a', 'b', 'c', 'Z', 'o', 'r', 'g', 'a', 2, '3'), ('a', 2, '3'), 2, ('x', 'z', 'z')]

# Set
a_set=set(['a', 3, 'Ted', 1,'a','a']) # https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
{'a', 3, 'Ted', 1}
a_set=a_set| {3,5,6}  
# No + , use UNION and other set operators , intersection '&' , and difference '-' 
{1, 3, 'Ted', 5, 6, 'a'}

# Dictionary
# Dictionaries can be created by several means
# Use a comma separted list of key : value pairs within bracers
{'jack' : 4098, 'sjoerd' : 4127}
# or
{4098 : 'jack', 4127 : 'sjoerd'}

#use a dict comprehension:
{}, {x: x ** 2 for x in range (10)}

#use the type constructor:
dict(), dict([('foo', 100), ('bar', 200)]), dict (foo=100, bar=200)

# Range is a sequence of integers (immutable)
# range(up_to_stop)
a_list_from_range = list(range(10))
print(a_list_from_range)
[0,1,2,3,4,5,6,7,8,9]

# range(start,stop,[step])
a_list= list(range(1, 11))
print(a_list)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a_list= list(range(0, 30, 5))
print(a_list)
[0, 5, 10, 15, 20, 25]

# For a positive step, r[i] = start + step*i where i>= 0 and r[i] < stop.
# For a negative step, r[i] = start + step*i, but the constraints are i>= 0 and r[i] > stop.

list(range(0, -10, -1))
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

# empty range –not range
list(range(0))
[]
list(range(1, 0))
[]

# Go through a sequence to calculate or gather information as you go.
a_list_of_tuples= [('John','Doe',230,50000), ('Jane','Doe',260,70000), ('Tane','Kahurangi', 220, 60000),('Hinemoa','Awatea',240,40000)]
print("The original list\n",a_list_of_tuples)

# Calculate the total student debt
student_debt= 0
for a_student in a_list_of_tuples: # << use FOR to iterate
    student_debt+= a_student[3]
    print(f'\n\nTotal Student Debt = {student_debt}\n')

#Go through a sequence to calculate or gather information as you go.
a_list_of_tuples= [('John','Doe',230,50000), ('Jane','Doe',260,70000), ('Tane','Kahurangi', 220, 60000),('Hinemoa','Awatea',240,40000)]

# Calculate if the student uses up all their weekly income,
# how many weeks it will take to pay off for each student.
# Make a new list that contains new tuples that include weeks to pay off.

new_list= []
for a_student in a_list_of_tuples:
    new_student= a_student+ ((a_student[3] / a_student[2]),)
    new_list+= [new_student]
    print("\nNEWLIST \n", new_list)

#Go through a sequence to calculate or gather information as you go.
a_list_of_tuples= [('John','Doe',230,50000), ('Jane','Doe',260,70000), ('Tane','Kahurangi', 220, 60000),('Hinemoa','Awatea',240,40000)]

# Calculate if the student uses up all their weekly income,
# how many weeks it will take to pay off for each student.
# Update the list so that tuples include weeks to pay off.
# Do the same calculation, but update the existing list with the new tuples

for index in range(len(a_list_of_tuples)):
    a_student= a_list_of_tuples[index]
    new_student= a_student+ ((a_student[3] / a_student[2]),)
    a_list_of_tuples[index] = new_student
    print("\nExisting list updated\n",a_list_of_tuples)