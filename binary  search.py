# binary search
def binarysearch(items,value):
    lb=0
    ub=len(items)-1
    while (lb<=ub):
        mid=int((lb+ub)/2)
        if items[mid]==value:
            return mid
        elif value<items[mid]:
            ub=mid-1
        else:
            lb=mid+1
    return -1
items=list()
num=input("enter no of elements in the list")
print("enter elements in sorted order")
for i in range(0,int(num)):
    n=input("enter elemnt")
    items.append(int(n))
choice="y"
while choice is "y":
    s=input("enter element to be searhed ")
    i=binarysearch(items,int(s))
    if i is -1:
        print("value not found")
    else :
        print("value at position {}".format(i))
        
    choice =raw_input("o you wnat to continue")       
