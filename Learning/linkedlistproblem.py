

d = {'nav': 2.1, 'har': 2.2, 'anj': 2.0}
# print(d.values())
# print(d.keys())
# print(d.items())

# for i,j in d.items():
#     print(i)
#     print(j)


# d = {}
# for _ in range(int(input("Enter a range: "))):
#     name = input("Name: ")
#     grade = float(input("Grade: "))
#     d[name] = grade
s=sorted(list(set(d.values())))[0]
print(s)
# se= []
# for i, j in d.items(): 
#     if j == s:
#         se.append(i)
# se.sort()
# print(se)
# for i in se:
#     print(i)