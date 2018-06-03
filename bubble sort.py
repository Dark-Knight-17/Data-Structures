# bubble sort
def bubblesort(alist):
    for i in range (len(alist)-1,0,-1):
        for j in range(i):
            if alist[j]>alist[j+1]:
                temp=alist[j]
                alist[j]=alist[j+1]
                alist[j+1]=temp
alist=[]
n=int(input("enter number of elements"))
while n>0:
    x=int(input("enter element"))
    alist.append(x)
    n=n-1
bubblesort(alist)
print(alist)
