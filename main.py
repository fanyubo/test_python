# basic list
mylist = [1, 3, 5, 7]
print(mylist)

# list multiplication
newlist = mylist * 3
print(newlist)
newlist.sort()
print(newlist)

# append and delete
mylist.append(9)
print(mylist)
print(mylist[2])
del mylist[2]
print(mylist)

# length
print(len(mylist))
print(mylist)

# adding lists
stringlist = ['git', 'has', 'good', 'stuff']
print(mylist + stringlist)

# multiply list
print(stringlist * 3)

# tuple
t1 = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55)
print(t1)
print(len(t1))

# map
age_map = {'Nathan': 12, 'Maddie': 15, 'Yubo': 46}
age_map['Sharon'] = 43
age_map['Xunpei'] = 81
age_map['Linzhu'] = 74
print(age_map['Maddie'])
print(age_map['Sharon'])
print(age_map)
