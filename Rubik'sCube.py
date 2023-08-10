print("Welcome to rubik's cube")
print("Below is a link to cube notation")
print("https://ruwix.com/the-rubiks-cube/notation/advanced/")
#global
global running,a1,a2,a3,a4,a5,a6,a7,a8,a9,b1,b2,b3,b4,b5,b6,b7,b8,b9,c1,c2,c3,c4,c5,c6,c7,c8,c9,d1,d2,d3,d4,d5,d6,d7,d8,d9,e1,e2,e3,e4,e5,e6,e7,e8,e9,f1,f2,f3,f4
global f5,f6,f7,f8,f9,z1,z2,z3,z4,z5,z6,z7,z8,z9,z10,z11,z12,z13,z14,z15,z16,z17,z18,z19,z20
#misc variables
running = True
#top
a1 = 1
a2 = 1
a3 = 1
a4 = 1
a5 = 1
a6 = 1
a7 = 1
a8 = 1
a9 = 1
#front
b1 = 2
b2 = 2
b3 = 2
b4 = 2
b5 = 2
b6 = 2
b7 = 2
b8 = 2
b9 = 2
#Bottom
c1 = 3
c2 = 3
c3 = 3
c4 = 3
c5 = 3
c6 = 3
c7 = 3
c8 = 3
c9 = 3
#Back
d1 = 4
d2 = 4
d3 = 4
d4 = 4
d5 = 4
d6 = 4
d7 = 4
d8 = 4
d9 = 4
#Right
e1 = 5
e2 = 5
e3 = 5
e4 = 5
e5 = 5
e6 = 5
e7 = 5
e8 = 5
e9 = 5
#Left
f1 = 6
f2 = 6
f3 = 6
f4 = 6
f5 = 6
f6 = 6
f7 = 6
f8 = 6
f9 = 6
def unfold():
    global running,a1,a2,a3,a4,a5,a6,a7,a8,a9,b1,b2,b3,b4,b5,b6,b7,b8,b9,c1,c2,c3,c4,c5,c6,c7,c8,c9,d1,d2,d3,d4,d5,d6,d7,d8,d9,e1,e2,e3,e4,e5
    global e6,e7,e8,e9,f1,f2,f3,f4,f5,f6,f7,f8,f9,z1,z2,z3,z4,z5,z6,z7,z8,z9,z10,z11,z12,z13,z14,z15,z16,z17,z18,z19,z20
    print("       ",a1,a2,a3)
    print("       ",a4,a5,a6)
    print("       ",a7,a8,a9)
    print(" ")
    print(f1,f2,f3," ",b1,b2,b3," ",e1,e2,e3)
    print(f4,f5,f6," ",b4,b5,b6," ",e4,e5,e6)
    print(f7,f8,f9," ",b7,b8,b9," ",e7,e8,e9)
    print(" ")
    print("       ",c1,c2,c3)
    print("       ",c4,c5,c6)
    print("       ",c7,c8,c9)
    print(" ")
    print("       ",d1,d2,d3)
    print("       ",d4,d5,d6)
    print("       ",d7,d8,d9)
def cubeshow():
    print("Top")
    print(a1,a2,a3)
    print(a4,a5,a6)
    print(a7,a8,a9)
    print("Front")
    print(b1,b2,b3)
    print(b4,b5,b6)
    print(b7,b8,b9)
    print("Bottom")
    print(c1,c2,c3)
    print(c4,c5,c6)
    print(c7,c8,c9)
    print("Back")
    print(d1,d2,d3)
    print(d4,d5,d6)
    print(d7,d8,d9)
    print("Right")
    print(e1,e2,e3)
    print(e4,e5,e6)
    print(e7,e8,e9)
    print("Left")
    print(f1,f2,f3)
    print(f4,f5,f6)
    print(f7,f8,f9)
while running == True:
    i1 = input("Next Move? ")
    if i1 == "print":
        cubeshow()
    elif i1 == "show":
        unfold()
    elif i1 == "F":
        z1 = b1
        z2 = b2
        z3 = b3
        z4 = b4
        z5 = b6
        z6 = b7
        z7 = b8
        z8 = b9
        z9 = f3
        z10 =f6
        z11 =f9
        z12 =a7
        z13 =a8
        z14 =a9
        z15 =e1
        z16 =e4
        z17 =e7
        z18 =c1
        z19 =c2
        z20 =c3
        b3 = z1
        b6 = z2
        b9 = z3
        b2 = z4
        b8 = z5
        b1 = z6
        b4 = z7
        b7 = z8
        a9 = z9
        a8 = z10
        a7 = z11
        e1 = z12
        e4 = z13
        e7 = z14
        c3 = z15
        c2 = z16
        c1 = z17
        f3 = z18
        f6 = z19
        f9 = z20
    elif i1 =="F'":
        z1 = b1
        z2 = b2
        z3 = b3
        z4 = b4
        z5 = b6
        z6 = b7
        z7 = b8
        z8 = b9
        z9 = f3
        z10 =f6
        z11 =f9
        z12 =a7
        z13 =a8
        z14 =a9
        z15 =e1
        z16 =e4
        z17 =e7
        z18 =c1
        z19 =c2
        z20 =c3
        b7 = z1
        b4 = z2
        b1 = z3
        b8 = z4
        b2 = z5
        b9 = z6
        b6 = z7
        b3 = z8
        c1 =z9
        c2 =z10
        c3 = z11
        e7 =z18
        e4 =z19
        e1 = z20
        a9 =z17
        a8 =z16
        a7 = z15
        f3 =z14
        f6 =z13
        f9 =z12
    elif i1 == "F2":
        z1 = b1
        z2 = b2
        z3 = b3
        z4 = b4
        z5 = b6
        z6 = b7
        z7 = b8
        z8 = b9
        z9 = f3
        z10 =f6
        z11 =f9
        z12 =a7
        z13 =a8
        z14 =a9
        z15 =e1
        z16 =e4
        z17 =e7
        z18 =c1
        z19 =c2
        z20 =c3
        b9 = z1
        b8 = z2
        b7 = z3
        b6 = z4
        b4 = z5
        b3 = z6
        b2 = z7
        b1 = z8
        e7 = z9
        e4 = z10
        e1 = z11
        a9 = z18
        a8 = z19
        a7 = z20
        f3 = z17
        f6 = z16
        f9 = z15
        c1 = z14
        c2 = z13
        c3 = z12
    elif i1 == "R":
        z1 = e1
        z2 = e2
        z3 = e3
        z4 = e4
        z5 = e6
        z6 = e7
        z7 = e8
        z8 = e9
        z9 = a3
        z10 = a6
        z11 = a9
        z12 = b3
        z13 = b6
        z14 = b9
        z15 = c3
        z16 = c6
        z17 = c9
        z18 = d3
        z19 = d6
        z20 = d9
        e7= z1
        e4= z2
        e9= z3
        e2= z4
        e8= z5
        e1= z6
        e4= z7
        e7= z8
        d3= z9
        d3= z9
        d6= z10
        d9= z11
        a3= z12
        a6= z13
        a9= z14
        b3= z15
        b6= z16
        b9= z17
        c3= z18
        c6= z19
        c9= z20
    elif i1 == "quit":
        running = False