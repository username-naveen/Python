# a = []
# n = int(input("Enter number of positions: "))
# for i in range(n):
#     x,y = input("enter with spaces: ").split()
#     a += [[int(x),int(y)]]
# print(a)

from operator import itemgetter


a = [[0, 0], [0, 10], [10, 0], [10, 10], [5, 5]]
sorted(a, key = itemgetter(0))
