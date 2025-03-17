values = [1,2,"rahul",4,5]
#List can have multiple data types and can be of any datatype
print(values[0])
print(values[3])
print(values[-1])
print(values[1:3])
values.insert(3,"shetty")
print(values)
values.append(7)
print(values)
values[2] = "Prachi"
print(values)
del values[2]
print(values)


#Tuple

val = (1,2,"prachi",4.5)

print(val[1])

# tuple Immutable so below error
# val[2] = "Rahul"
print(val)


# dictionary

dic = {"a" :2, 4:"abc", "c":"Hellow world"}
print(dic[4])
print(dic["c"])

#
dict = {}
dict["firstname"] = "prachi"
dict["lastname"] = "kulkarni"

print(dict)
print(dict["lastname"])