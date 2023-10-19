tab1 = []
tab2 = []
s = 0
x = int(input("enter the number of students : "))
for i in range (0,x) :
    a = int(input("enter the note : "))
    while a < 0 or a > 20 :
       a = int(input("please enter a note between 0 and 20 : "))
    tab1.append(a)
    s = s + a
b = s / x
for i in range(0,x) :
    if tab1[i] >= b :
        tab2.append(tab1[i])
print(tab2)



