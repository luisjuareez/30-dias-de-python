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
print(does_exist) #15
it_companies.sort()
it_companies.reverse()