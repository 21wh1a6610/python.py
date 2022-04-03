nterms=int(input("how many terms:"))
f1=0
f2=1
count=0
if nterms<=0:
    print("please enter positive integer")
else:
    print("Fibonacci Sequence")
    while count<nterms:
        print(f1)
        t=f1+f2 #t=temporary variable
        f1=f2
        f2=t
        count=count+1