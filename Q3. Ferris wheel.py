#Python
while True:
    lst = []
    n = 0
    inpN = int(input("Enter the no. of children: "))
    inpX = int(input("Enter the max allowed weight: "))
    for i in range(inpN):
        inpP = int(input("Enter the weight of child: "))
        lst.append(inpP)
    for i in lst:
        n += i
    if n%inpX != 0:
        print("->",(n//inpX) + 1)
    else:
        print("->",n//inpX)
