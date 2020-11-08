#locked
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
#locked

    def removeDuplicates(self,head):
        #Write your code here
        currValue = head
        while currValue is not None and currValue.next is not None:
            while currValue.next is not None and currValue.data is currValue.next.data:
                currValue.next = currValue.next.next
            currValue = currValue.next
        return head
        
#locked
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head);
#locked