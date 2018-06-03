class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoublyLinkedList():
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def insertfromhead(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
        else:
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode
        print("new node inserted at head position")
        self.size+=1
    def insertfromtail(self,data):
        newnode=Node(data)
        if self.tail==None:
            self.head=newnode
            self.tail=newnode
        else:
            self.tail.next=newnode
            newnode.prev=self.tail
            self.tail=newnode
        print("newnode inserted at the tail position")
        self.size+=1
    def deletefromhead(self):
        if self.head==None:
            print("linked list empty")
        else:
            value=self.head.data
            print("Deleted node is ",value)
            self.head=self.head.next
            self.head.prev=None
            self.size-=1
    def deletefromtail(self):
        if self.head==None:
            print("linked list is empty")
        else:
            current=self.head
            while (current.next!=None):
                prevnode=current
                current=current.next
            value=current.data
            prevnode.next=None
            print("deleted value is",value)
            self.tail=prevnode
            self.size-=1
    def traversalofLL(self):
        current=self.head
        while current!=None:
            print(current.data)
            current=current.next
        print("end")
    def search(self,value):
        self.n=0
        current=self.head
        while current!=None:
            self.n+=1
            if current.data!=value:
                current=current.next
            else:
                return True
        return False
    def deletevalue(self,value):
            current=self.head
            while current!=None and current.data!=value:
                prevnode=current
                current=current.next
            if current==None:
                print("node not found")
            else:
                self.size-=1
                if current==self.head:
                    self.head=current.next
                elif current==self.tail:
                    prevnode.next=current.next
                    self.tail=prev
                else:
                    prevnode.next=current.next
                print("value deleted successfully")
                
    def PrintList(self):
        currentNode=self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode=currentNode.next
d=DoublyLinkedList()
print("menu")
print("1. Insert from head \n2.insert from tail \n3. delete from tail \n4. delete from head")
print("5. search for a value \n6. delete a value \n7. display linked list \n8.Exit")
choice=int(input("enter your choice"))
while choice!=8:
    
    if choice==1:
        value=int(input("enter value to be inserted"))
        d.insertfromhead(value)
    if choice==2:
         value=int(input("enter value to be inserted at tail"))
         d.insertfromtail(value)
    if choice==3:
         d.deletefromtail()
    if choice==4:
        d.deletefromhead()
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
        print("the linked list contains the following elements")
        d.traversalofLL()
    choice =int(input("enter your choice again"))
