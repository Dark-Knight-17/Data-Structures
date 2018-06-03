#selection sort
def ses(alist):
    for i in range(len(alist)-1,0,-1):
        
        pos=0
        for loc in range(1,i+1):
            if alist[loc]>alist[pos]:
                pos=loc
        temp=alist[i]
        alist[i]=alist[pos]
        alist[pos]=temp
alist=[]
n=int(input("enter number of elements"))
while n>0:
    x=int(input("enter element"))
    alist.append(x)
    n=n-1
ses(alist)
print(alist)
