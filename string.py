# initial value
fred = "1. how are you today"
print(fred)

# change value
fred = "2. bad weather today and tomorrow"
print(fred)

# multi-line string
fred = '''3. this is first line
4. this is the second line'''
print(fred)

# use single quotes to include double quotes
fred = '5. He said, "I\'m feeling much better"'
print(fred)

# use escapse character to include double quotes
fred = "6. He said, \"I'm feeling so wonderful now\""
print(fred)

# embed value in strings
score = 95
fred = "7. I got %s points in my math test"
print(fred)
print(fred % score)

score = 92
print(fred % score)

print(fred % 100)
print(fred % "a hundred")

# embed two values in a string
fred = "8. I got %s points in my ELA, and %s points in my social study project"
print(fred % (80, 94))

ela_score = 91
ss_score = 87
print(fred % (ela_score, ss_score))

# create strings with multiplication
print(12 * 'n')

spaces = 40 * ' '
grid = '1234567890' * 8
print(grid)
print("%s418 Alliance Cir" % spaces)
print("%sCary, NC 27519" % spaces)
print("%sU.S.A." % spaces)
