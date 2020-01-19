# pets = ['dog', 'cat', 'gerbil', 'hamster']

# if 'hamster' in pets:
#     print('yes')

# list1 = [10, 21, 4, 45, 50, 66, 93]

# result = filter(lambda a: a % 2 == 0, list1)

# # print(result)
# # print(list(result))

# # python loops


# for i in range(1,10,2): # start at 1, ends at 1, loops 3
#     print(i)


# for i in range(3,len(list1),2):
#     print(list1[i])

colors = ["red", "blue", "green"]

# for color in range(len(colors)):
#     print(colors[color], color, end=" - ")

# for color in colors:
#     print(colors.index(color) , color)

for index, color in enumerate(colors):
    print(index, color)
