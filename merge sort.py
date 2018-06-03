

def mergesort(alist):
    print("splitting",alist);
    if len(alist)>1:
        mid=len(alist)//2;
        lefthalf=alist[:mid];
        righthalf=alist[mid:];
        mergesort(lefthalf);
        mergesort(righthalf);
        i=0;
        j=0;
        k=0;
        while i <len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i];
                i=i+1;
            else:
                alist[k]=righthalf[j]
                j=j+1;
            k=k+1;
        while i<len(lefthalf):
            alist[k]=lefthalf[i];
            i=i+1;
            k=k+1;
        while j<len(righthalf):
            alist[k]=righthalf[j];
            j=j+1;
            k=k+1;
        print("merging",alist);
unsortedlist=list()
number=int(input("Enter the number of elements "))
while True:
    item=int(input("Enter element"))
    unsortedlist.append(item)
    if len(unsortedlist)==number:
        break
alist=mergesort(unsortedlist)
print("sorted list using merge sort");
