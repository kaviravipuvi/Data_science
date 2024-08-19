# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 09:04:48 2024

@author: Kaviyarasan PR
"""
studlist = {'Anand' : {'DOB' : '20/11/2001', 'Roll' : 'ED1234' },
'Ramesh' : {'DOB' : '19/11/2001', 'Roll' : 'ED1235' },
'Kamesh' : {'DOB' : '21/11/2001', 'Roll' : 'ED1236' } }

print(type (studlist))

for k in studlist.items():
    print(k)
    print(*k)
    # print(**k)

print("\n")
for u in studlist.keys():
    print(u)
    print(*u)


print(studlist["Anand"])

print(studlist["Anand"]["Roll"])

print(studlist["Anand"]["Roll"]=="AM23M025")

studlist['Anand']['Roll'] = 'ED5678'
print(studlist['Anand'])

studlist['Suresh'] = {'DOB': '22/11/2001', 'Roll': 'ED1237'}

print(studlist)



squares_dict = {num: num**2 for num in range(1, 10)}

print(squares_dict)




