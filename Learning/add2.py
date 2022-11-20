# def add_nums(num1, num2):
#     while num2 != 0:
#         data = num1 & num2
#         # print(data)
#         num1 = num1 ^ num2
#         print(num1)
#         num2 = data << 1
#         # print(num2)
#     return num1
# print(add_nums(2, 10))

# print(type('ab{4,8}'))

d1 = {'key1': 50, 'key2': 100, 'key3':200}
d2 = {'key1': 200, 'key2': 100, 'key4':300}

for i, j in d1.items():
    for x, y in d2.items():
        