
print("Algorith Workbench")
print("\nProblem #1")
x=(int(input("Value for x: ")))
y="Nothing"
z="Nothing"
if x >= 100:
    y=20
    z=40
    print("x= ", (x))
    print("y= ", (y))
    print("z= ", (z))
elif x <= 100:
    print("x= ",(x))
    print("y= ",(y))
    print("z= ",(z))

print("\nProblem #2")
a=(int(input("Value for a: ")))
b="Nothing"
c="Nothing"
if a <= 10:
    b=0
    c=1
    print("a= ", (a))
    print("b= ", (b))
    print("c= ", (c))
elif a >= 10:
    print("a= ",(a))
    print("b= ",(b))
    print("c= ",(c))

print("\nProblem #7")
Val=(int(input("Enter Value: ")))
if 9 <= Val <=51:
    print("Valid Point")
else:
    print("Invalid Point")

print("\nProgramming Exercise #15")
sec=(int(input("Enter Seconds: ")))
min=0
hour=0
day=0
if sec >= 86400:            #Calculating Days
    while sec >= 86400:
        sec = int(sec-86400)
        day = int(1+day)
        if sec < 86400:
            break
if sec >= 3600:           #Calculating Hours
    while sec >= 3600:
        sec = int(sec - 3600)
        hour = int(1 + hour)
        if sec < 3600:
            break
if sec >= 60:             #Calculating Minutes
    while sec >= 60:
        sec =int(sec - 60)
        min =int(1 + min)
        if sec < 60:
            break

print("Number Of Days: ",(day),"Day(s)")
print("Number Of Hours: ",(hour),"Hour(s)")
print("Number Of Minutes: ",(min),"Minute(s)")
print("Number Of Seconds: ",(sec),"Second(s)")

print("\nHomework Is Complete")

