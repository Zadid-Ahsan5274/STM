'''print(1<1)
print(1<=1)
print(1>1)
print(1>=1)
print(1==1)
print(1!=1)'''

name = input("What is your name: ")
if name == "Jessica":
    print("Hello, nice to see you {}".format(name))
elif name == "Danielle":
    print("Hello, you are a great person!")
elif name == "Kingston":
    print("Hi, {}, let's have lunch soon!".format(name))
elif name != "Mariah":
    print("You are not mariah!")
else:
    print("Have a nice day!")