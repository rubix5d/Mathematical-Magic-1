def factors():
    n = int(input("Write the number"))
    for i in range(1,n+1):
        if n%i == 0:
            print(i)
factors()
    