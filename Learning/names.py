a = {"Naveen Rama Siva" : 110, "Venka Bala Bala": 111}
# print(sorted(list(set(a.keys)))[0])
# b = list(set(a.keys))
n = []

for name, number in a.items():
    fullName = name.split(" ")
    firstName = fullName[0][0]
    middleName = fullName[1][0]
    lastName = fullName[-1]
    
    newName = lastName + ", " + firstName + " " + middleName
    
    n.append(newName)
    
n.sort()

print(n)

# for i in a:
#     print(i)
#     l = i.split(" ")
#     print(l[-1])
#     b = ""
#     b += l[-1] + " " + l[0][0] +" "+l[1][0];
#     n.append(b)
# print(a,n)