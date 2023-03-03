empty_list= list()
list= ['1', '2', '3','4','5']
print(list)
size= len(list)
print(size)
list[1:3:5]
print(list) #4

mixed_data_types= ['Luis','16','1.78', 'Single', 'Jerez de la Frontera']
print(mixed_data_types)
it_companies= ['Facebook', 'Google', 'Microsoft', 'Apple', 'IDM', 'Oracle', 'Amazon']
print(it_companies)
len(it_companies) #8

print(it_companies)
print('first_company', it_companies[0]) 
it_companies.insert('Apple', ['Netflix'])
it_companies[4]= 'Netflix'
print(it_companies) #10
it_companies.append('Google')
it_companies.insert(4,'Canon')
print(it_companies) #12
it_companies[1]=it_companies[1].upper()
print('joined list: t/', '#;'.join(it_companies)) #13
it_companies= ['Facebook', 'Google', 'Microsoft', 'Apple', 'IDM', 'Oracle', 'Amazon']
does_exist= 'Amazon' in it_companies
print(does_exist) 
it_companies.sort() #16
it_companies.reverse() #17

it_companies= ['Facebook', 'Google', 'Microsoft', 'Apple', 'IDM', 'Oracle', 'Amazon'] #18
all_companies= it_companies[0:6]
facebook_google_microsoft= it_companies[0:2]
print(facebook_google_microsoft)
idm_oracle_amazon= it_companies[4:6] #19
print(idm_oracle_amazon)
it_companies[len(it_companies)//2] #20
it_companies.pop(0) #21
it_companies.pop(3) #22
it_companies.pop(6) #23
it_companies.clear() #24
del it_companies #25

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux'] #26
back_end = ['Node','Express', 'MongoDB']
full_stack= front_end.copy() #27
full_stack.insert(4, 'Phyton', 'SQL')
print(full_stack)