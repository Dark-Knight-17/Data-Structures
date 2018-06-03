class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList():
    
    def __init__(self,data):
        self.head=None
        
        self.size=0
        
    def insert(self,newnode):
        self.size+=1
        if self.head is None:
            self.head=newnode
        else:
            lastNode=self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode=lastNode.next
            lastNode.next=newnode
    def PrintList(self):
        currentNode=self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode=currentNode.next
    def insertAtEnd(self,newnode):
        item=Node(newnode)
        current=self.head
        while current.next != None:
            current =current.next
        current.next=item
        self.size+=1
    def insertAtBeginning(self,newnode):
        item=Node(newnode)
        if self.head is None:
            self.head=item
        else:
            item.next=self.head
            self.head=item
        self.size+=1
        
    def delete(self,data):
        current=self.head
        previous = None
        found= False
        while current and found is False:
            if current.data==data:
                found=True
                self.size-=1
            else:
                previous=current
                current=current.next
        if current is None:
            print("ELement not found")
        if previous is None:
            self.head=current.next
        else:
            previous.next=current.next
    def InsertAtPos(self,data,Pos):
        current=self.head
        previous=None
        cPos=0
        if Pos>self.size:
            print("position index is out of range")
        else:
            while cPos !=Pos:
                previous=current
                current=current.next
                cPos+=1
            if Pos==cPos:
                previous.next=data
                data.next=current
                self.size+=1
                
            
        
fnode=Node(1)
LinkedList=LinkedList(fnode)
LinkedList.insert(fnode)
snode=Node(2)
LinkedList.insert(snode)
tnode=Node(3)
LinkedList.insert(tnode)
nnode=Node(4)
LinkedList.PrintList()
print("linkedlist after insertion element at end")
LinkedList.insertAtEnd(4)#nnode
LinkedList.PrintList()
print("linkedlist after insertion element at start")
LinkedList.insertAtBeginning(5)
print(LinkedList.PrintList())
print("linkedlist after deletion of  element ")
LinkedList.delete(2)
print(LinkedList.PrintList())

position=int(input("enter position of element in linked list"))
LinkedList.InsertAtPos(Node(6),position)
print("linkedlist after insertion element at particular position")
print(LinkedList.PrintList())       

