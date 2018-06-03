#CIRCULAR LINKED LIST
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class CircularLL():
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def insertfromhead(self,data):#here 
        newnode=Node(data)
        if self.head == None:
            self.head=self.tail=newnode
            newnode.next=newnode
        else:
            newnode.next=self.head
            self.head=newnode
            self.tail.next=newnode
        print("new node inserted at head position")
        self.size+=1
    def insertfromtail(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=self.tail=newnode
            newnode.next=newnode
        else:
            self.tail.next=newnode
            self.tail=newnode
            self.tail.next=self.head
        print("newnode inserted at the tail position")
        self.size+=1
    def deletefromhead(self):
        current=self.head
        if self.head==None:
            print("Circular linked list empty")
        elif self.head.next==self.head:
            self.head=None
        else:
            self.head=self.head.next
            self.tail.next=self.head
            print("Deleted node at head")
            self.size-=1
    def deletefromtail(self):
        if self.head==None:
            print("circular linked list is empty")
        elif self.head==self.tail:
            self.head=None
        else:
            current=self.head
            while current.next!=self.head:
                prevnode=current
                current=current.next
           
            prevnode.next=self.head
            self.tail=prevnode
            print("deleted value is",value)
            self.size-=1
    def traversalofCLL(self):
        if self.head ==None:
            print("circluar linked list is empty")
        else:
            
            current=self.head
            while (current.next!=self.head):
                
                print(current.data)
                current=current.next
            print(current.data)    
            print("end")
    def search(self,value):
        self.n=0
        current=self.head
        while (current!=None):
            self.n+=1
            if current.data!=value:
                current=current.next
            else:
                return True
    def deletevalue(self,value):
            current=self.head
            if self.head == None:
                print("list is empty")
            else:
                
                while current.data!=value and current.next!=self.head:
                    prevnode=current
                    current=current.next
                if current==self.head and self.head.next!=self.head:
                    self.head=self.head.next
                    self.tail.next=self.head
                elif current==self.head and self.head.next==self.head:
                    self.head=None
                elif current.data==value:
                    prevnode.next=current.next
                
                
                else:
                    
                    print("value not found")
                

d=CircularLL()
print("menu")
print("1. Insert from head \n2.insert from tail \n3 delete from head \n4 delete from tail ")
print("5. search for a value \n6 delete a value \n7 display linked list \n8.Exit")
choice=int(input("enter your choice"))
while choice!=8:
    
    if choice==1:
        value=int(input("enter value to be inserted"))
        d.insertfromhead(value)
    if choice==2:
         value=int(input("enter value to be inserted"))
         d.insertfromtail(value)
    if choice==3:
         d.deletefromhead()
    if choice==4:
        d.deletefromtail()
    if choice==5:
        value=int(input("enter value to be searched"))
        result=d.search(value)
        if result==True:
            print("value found at a node ",d.n,"in the linked list")
        else:
            print("value not found")
    if choice==6:
        value=int(input("enter value to be deleted"))
        d.deletevalue(value)
    if choice==7:
        d.traversalofCLL()
    choice =int(input("enter your choice again"))
