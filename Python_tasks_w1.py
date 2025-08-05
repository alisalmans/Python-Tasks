name = "Ali"     # Variable: string
age = 25          #Variable: integer
height = 5.9      # Variable: float
# Proper indentation
if age > 18:
    print(name, "is an adult.")

a = 10              # int
b = 3.14            # float
c = "Python"        # str
d = True            # bool

print(type(a), a)
print(type(b), b)
print(type(c), c)
print(type(d), d)

x = 8
y = 3

# Arithmetic
print(x + y, x - y, x * y, x / y, x % y, x ** y)

# Comparison
print(x > y, x == y, x != y)

# Logical
a = True
b = False
print(a and b)
print(a or b)
print(not b)

name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
print("Hello", name, "- you are", age, "years old.")

marks = int(input("Enter your marks out of 100: "))

if marks >= 90 and marks<=100:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
else:
    print("Grade: C or below")

for loop
for i in range(1, 6):
    print("Number:", i)

# while loop
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue  # skip 3
    print("While loop:", i)
    i += 1


print("Hello, Python World!")