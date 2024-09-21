def product(inp):
    for duct in inp:
        global pro
        product = pro*int(duct)
        pro = int(duct)
    print(product)
    
while True:
    pro = 0
    inp = input("Enter the no.: ")
    if 10<=int(inp)<=99:
        product(inp)
