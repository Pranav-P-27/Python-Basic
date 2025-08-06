#Variables
name = "Pranav"
age = 25
is_student = True
print("Name",name)
print(age)
print(is_student)

#Operators
a=50;
b=10;
c=100;
result=a+b;
print("Add : ",a + b);
print("Subtract: ", a - b)
print("Multiply: ", a * b)
print("Divide: ", a / b)
print("Floor Divide:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)
print("Pranav")
#conditon
d = a + b
if c >= d:
    {
        print("C is Greater")
    }
else:{
    print("C is less than G")
     }

if b == d and d != 0:
    {
        print("b and d are equal")
    }
elif b >= d:
    {
        print("b is only greater")
    }
else:
    {
        print("No Action is Performed")
    }

#loops
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print("I like", fruit)

for i in range(5):
    print("Number:", i)

for i in range(10,20):
    {
        print("Number:", i)
    }
count = 1

while count <= 5:
    print("Count is:", count)
    count += 1

for i in range(10):
    if i == 5:
        break
    print("For break statment",i)
for i in range(5):
    if i == 2:
        continue
    print("For Continue ",i)