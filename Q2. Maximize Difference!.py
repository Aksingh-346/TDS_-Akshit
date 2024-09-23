#Python
def main(x,y):
    n = 0
    z = x
    for i in range((inpy-inpx)+1):
        if x != y:
            a = (z-x)+(y-z)
            z += 1
            if a > n:
                n = a
        elif x == y:
            break
    print(n)

while True:
    inpx = int(input("Enter the 1st no.: "))
    inpy = int(input("Enter the 2nd no.: "))
    if (1<=inpx<=inpy<=10):
        main(inpx,inpy)
    else:
        print("*Please enter the numbers b/w 1 to 10*")
        continue
