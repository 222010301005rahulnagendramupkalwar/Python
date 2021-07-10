print("Hello World !")

i=1
while i<=5:
    j=1
    while j<=i:
        print("@ ",end="")
        j+=1
    i+=1
    print()
i=1
while i<=6:
    j=6
    while j>=i:
        print("@ ",end="")
        j-=1
    i+=1
    print()