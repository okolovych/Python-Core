number=int(input("Enter number: "))
if number>1:
    n=0
    n1=1
    print(n)
    print(n1)
    fibonacci = 0
    while fibonacci<number-n:
        fibonacci=n+n1
        print(fibonacci)
        n=n1
        n1=fibonacci