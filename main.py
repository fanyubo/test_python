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
