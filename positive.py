list1=[]
n=int(input("enter size of the list"))
for i in range(0,n):
    e=int(input("enter the element :"))
    list1.append(e)
for number in list1:
    if number>= 0:
        print (number,end=" ")
        