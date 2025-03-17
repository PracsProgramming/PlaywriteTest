file = open("text.txt")
# print(file.read(5))
# print(file.readline())
# print(file.readline())


# read line by line

# line = file.readline()
# while line != '':
#     print(line)
#     line = file.readline()

# print(file.readlines())

for line in file.readlines():
    print(line)

file.close()

