my_dict = {"Anton": 25000, "Ilya": 50000, "Dmitriy": 40000, "Daniil": 60000}

print(my_dict)
print(my_dict.get('Ilya'))
print(my_dict.get('Katya'))

my_dict['Mariya'] = 20000
my_dict['Sasha'] = 33000

print(my_dict)

print(my_dict.pop('Sasha'))

print(my_dict)

# Множества

my_set = {1, 'String', 2, 3, False, 2, 3, 'String'}

print(my_set)

my_set.add(4)
my_set.add('Sallary')

my_set.discard(False)

print(my_set)