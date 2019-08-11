#Python Basics
print("################  Print Basics ##################")
print("Hello WOrld")
#variable assignment
a =10
b =20
print("sum",a+b)
print("sum"+str(a))

#String with first letter as caps
print("hi".title() , "hello".title())

print("################  List Basics ##################")
#Lists in Python represented by []
a = ["Book", "Cook", "Took", "shook"]
#reversing items in a list
a.sort(reverse = True)
a.reverse()
#accessing items in a list
print(a[2])
#deleting an item
del a[3]
#add items to a list
a.append("Shook")
#list index starts from 0
#slicing the list the range will print all the items from the starting position excluding the index
print("Printing the items from the begining till 4th item " , a[:3])
print("Printing the items from the index 1 to 3 ",a[1:3])
print("Printing the items from the index 1 to 2 ",a[1:2])
#-1 range beings from the end of the list
print("Printing the items from the index 1 to 2 ",a[:-1])
print(a)
#copy list
c = a
print("Original List ",a)
print("Copied list ",c)
b = [1,4,67]
#min and max functions
print("Max Value", max(b))
print("Min Value", min(b))

print("################  Loop Basics ##################")
#Array or accessing the items in a list via loop
for i in a:
    print("Values in array " +str(i))

#Accessing the items in aloop range function handy to generate sequence numbers
for a in range(1,10):
    print ("Item:" , a)

print("################  Tuple Basics ##################")
#tuples are similiar as List represented by () but the values are immutable as they cannot be changed
#only way they can be changed iv by over writting it
tup = (1,2,3,4)
print("value in index 0:" , tup[0])
print("value in index 1:" , tup[1])
#accessing tuples in a  loop
for tup in tup:
    print(tup)

#overwriting a tuple
tup = (3,2,3,4)
print("Over written tuple", tup)

print("################  if/else and if/elif/else Basics ##################")
a = "b"
if (a == "a"):
    print(a)
elif(len(a) == 1):
    print("1 character")
else:
    print("Not a ")

print("################  Dictionaries Basics ##################")
#represented as {}, they are always key:values
dict = {"car":"Civic", "mileage": 13}
print(dict)
print(dict["car"])
print(dict["mileage"])

#printing all keys (keys is a python keyword)
for keys in dict:
    print(keys)

for keys in dict:
    print(str(dict[keys]))

#print both ley and values
for k, v in dict.items():
    print(k, v)

print("################  User Input Basics ##################")
name = input("Whats the anme?\n")
print("Hi" + name)

print("################  While Loop Basics ##################")
i = 8
while(i < 10):
    print("In while loop")
    if(i == 9):
        print("In Continue loop")
        continue
    else:
        print("In Break loop")
        break


print("################  Functions Basics ##################")
def funct():
    print("Hi, first function")

#with parameters
def funct1(a,b):
    print("Hi, ",a,b)

#with parameters + return
def functrtn(a,b):
    return a+b

#Calling a function
funct()
funct1("Shook", "Book")
print("Value returned from functrtn:",functrtn(1,3))

print("################  Classes Basics ##################")
#Python is a OOPs. We can create a class and create objects

#Note: first letter of a class name should always be capital
#CREATING A CLASS
class Person():
    #create a constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def output(self):
        print("Name:"+ self.name +", Age:"+str(self.age))

class SecondChild():
    #constructor
    def greetings(self):
        print("Hi, multiple inheritance, second inherited class")

#inheriting a parent class to a child class
#we can inherit multiple classes
class FirstChild(Person, SecondChild):
    #pass command does the inheritance
    pass

#creating an object for a class
p = Person("Hi",13)
#print the methods in a class
p.output()
#accessing a variable
print(p.name)

print("################  Class Inheritance Basics ##################")
c = FirstChild("Hi, inheritance",13)
#calling the methods from Parent Class
c.output()
#calling the methods from SecondChild
c.greetings()