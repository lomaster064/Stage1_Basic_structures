immutable_var = (1, 3, [4, 5], 'String', True)

print(immutable_var)
print(type(immutable_var))

# immutable_var[1] = 5    ## TypeError: 'tuple' объект не поддерживает назначение элементов


mutable_list = [1, 3, [4, 5], 'String', True]

print(mutable_list)
print(type(mutable_list))

mutable_list[1] = 5
mutable_list[2][0] = 3
mutable_list[4] = False

print(mutable_list)

dict = {'key1': 'value1', 'key2': 'value2', 'key3': 123}

pars = dict.items()
print(pars(1))