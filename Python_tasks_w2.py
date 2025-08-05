# Creating a list
fruits = ["apple", "banana", "cherry", "mango"]

# Indexing
print(fruits[0])      # apple
print(fruits[-1])     # mango

# Slicing
print(fruits[1:3])    # ['banana', 'cherry']

# List methods
fruits.append("grape")
print(fruits)
fruits.remove("banana")
print(fruits)
fruits.insert(1, "orange")
print(fruits)
fruits.sort()
print(fruits)
 
 
 TUPLE
tuple=("ali",19,172.72)
print(tuple)
print(tuple[0])



SETS

juices={"white","green","yellow",1}
print(juices)
juices.add("yellow")
juices.discard("blue")
print(juices)

dictionary

person={
    "name":"Ali",
    "height":5.9,
    "age":19
}
print(person["name"])
print(person.get("age"))

def age_name(age,name):
    print("Your age is",age,"and your name is",name)

myname="ali"
myage=19
age_name(myage,myname)

scopes
x = 10  # Global variable

def demo():
    x = 5  # Local variable
    print("Inside function:", x)

demo()
print("Outside function:", x)

try:
    num=int(input("Give number:"))
    print("square :",num**2)
except ValueError:
    print("Invalid input. Please enter a number.")    

