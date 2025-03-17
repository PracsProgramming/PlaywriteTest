
# read file
# reverse and write
with open("text.txt",'r') as reader:
    content = reader.readlines()
    rev_content = reversed(content)
    with open("text.txt",'w') as writer:
        for line in rev_content:
            writer.write(line)



