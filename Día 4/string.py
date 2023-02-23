word1= 'Thirty'
word2= 'Days'
word3= 'Of'
word4= 'Phyton'
string1= word1 + word2 + word3 + word4
print(string1)

word5= 'Coding'
word6= 'for'
word7= 'all'
string2= word5 + word6 + word7
print(string2)

company= 'Coding for all'
company= string2
print(company)
print(len(company))
 
company.upper
print(company.upper())

company.lower
print(company.lower())

company= 'Coding for all'
print(company.capitalize())
print(company.swapcase())
print(company.title())

string2= word5 + word6 + word7
cut= string2. split(0)
for word in cut:
    print(cut[word5])

check= 'Coding for all'.index()
print(check)

company= 'Coding for all'
newcompany= company.replace("Coding","Phyton")
print(company)
print(newcompany)

newcompany= 'Phyton for all'
all_company= newcompany.replace("Phyton","Everyone")
print(newcompany)
print(all_company)

company= 'Coding for all' #13
print(company.split())
company= 'Coding, for, all'
print(company.split(', '))

webs= "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
separate_webs= webs.split(", ")
print(separate_webs)

company= 'Coding for all'
first_letter= company[0]
print(first_letter)
last_index= len(company) -1
print(last_index)
index10= company[10]
print(index10) 

acronym= 'Phyton for everyone'
acronym = acronym +word[0].upper()
print(acronym)
acronym_2= 'Coding for all'
acronym_2= acronym_2 +word[0].upper()
print(acronym_2)

company= 'Coding for all'
first_ocurrence= 'C'
index= company.find(first_ocurrence)
print(index)
last_ocurrence= 'f'
index_2= company. find(last_ocurrence)
print(index_2)
company_2= 'Coding for all people'
ocurrence= company_2.rfind('e')
print(ocurrence) 
