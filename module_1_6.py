# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
my_dict={'Semen':1988,'Dasha':1989,'Kolia':1990}
print(my_dict)
print(my_dict['Semen'])
print(my_dict.get('Sasha'))
my_dict.update({'Petia':1999,'Alex':1998})
a=my_dict.pop('Alex')
print(a)
print(my_dict)
my_set={1,2,3,3,2,1,'Semen','Semen'}
print(my_set)
my_set.add(5)
my_set.add(6)
my_set.discard(6)
print(my_set)