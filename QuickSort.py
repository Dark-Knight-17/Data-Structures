def partition(array,p,r):
    x=array[r]
    i=(p-1)
    print(i)
    j=p
    while(1):
        if array[j]<=x:
            i=(i+1)
            temp=array[j]
            array[j]=array[i]
            array[i]=tempra
        j+=1
        if j==r:
            break
    temp=array[i+1]
    array[i+1]=array[r]
    array[r]=temp
    return (i+1)
def quicksort(array,p,r):
    if p<r:
        q=partition (array,p,r)
        quicksort(array,p,q-1)
        quicksort(array,q+1,r)
alist=[]
n=int(input("enter no of elemnts"))
while(n>0):
    x=int(input("enter elements"))
    alist.append(x)
    n=n-1
print("original list",alist)
quicksort(alist,0,len(alist)-1)
print("sorted list",alist)

