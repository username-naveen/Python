lst = [1,2,3,[1,2,0]];
print(lst)
print(len(lst)) #4
print(lst[3][2]) #0
print(lst[::-1])
print(lst[:0])
lst.extend([9,8,0])
print(lst)

lst.insert(2, [8,9,0])
print(lst)

