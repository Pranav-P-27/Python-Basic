#Functions
def greet():
    print("Hello from a function!")

def getname(name):
        print ("hello" ,name)
        if name == "Pranav":
            print("Pranav is correct")
        else:
            print("Pranav is incorrect")

def add(a,b):
    c=a+b
    return c

def random():
    s="Pranav"
    i=45
    return s,i

getname("Pranav")
an=add(10,20)
print(an)
srt,inti=random()
print(srt,inti)

