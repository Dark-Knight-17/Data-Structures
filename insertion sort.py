def insertionsort(alist):
    for i in range(1,len(alist)):
        current=alist[i]
        hole=i
        while hole>0 and alist[hole-1]>current:
            alist[hole]=alist[hole-1]
            hole=hole-1
        alist[hole]=current
alist=[]
n=int(input("enter number of elemens"))
while(n>0):
    x=int(input("enter element"))
    alist.append(x)
    n=n-1
insertionsort(alist)
print(alist)

