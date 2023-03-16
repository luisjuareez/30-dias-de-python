dog= {}
dog['name']= 'Chop'
dog['color']= 'Black'
dog['breed']= 'Rottweiler'
dog['legs']= '4'
dog['age']= '6'
print(dog)

studen_dictionary= {'first_name': 'Luis', 'last_name' : 'Juarez', 'gender' : 'masculine', 'age':'16', 'material_status' : 'single', 'skills' : 'creative', 'country' : 'Spain', 'city' : 'Jerez', 'address' : 'Plaza del agua'}
print(len(studen_dictionary))
values_skill= studen_dictionary['skills'].values()
print(values_skill)
studen_dictionary.append('imaginative', 'agile') 
 
keys_list= studen_dictionary.keys
print(keys_list)
values_list= studen_dictionary.values
print(values_list)

studen_dictionary= {'first_name': 'Luis', 'last_name' : 'Juarez', 'gender' : 'masculine', 'age':'16', 'material_status' : 'single', 'skills' : 'creative', 'country' : 'Spain', 'city' : 'Jerez', 'address' : 'Plaza del agua'}
list= list(studen_dictionary.items())
print(list) 
print(studen_dictionary.items())

studen_dictionary.pop('address')
print(studen_dictionary)

dict.clear(dog)