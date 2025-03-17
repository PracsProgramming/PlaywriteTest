it = 4
while it > 0 :
    print(it)
    it-=1

print("******************************")
it = 10
while it > 0 :
    if it == 9:
        it -= 1
        continue # skips only it =9 step
    if it ==3:
        break # skips while
    print(it)
    it-=1
print("while is done")


