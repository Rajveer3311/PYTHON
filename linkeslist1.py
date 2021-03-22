class  Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class linkedlist:
    def __init__(self):
        self.head=None
    def insert_at_begginning(self,data):
        node = Node(data,self.head)
        self.head = node
    def print(self):
        if self.head is None:
            print('linked listis empty')
            return
        itr=self.head
        llstr=''
        while itr:
            llstr += str(itr.data) + "-->"
            itr=itr.next
        print(llstr) 
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next=Node(data,None)    

if __name__ == '__main__':
    ll=linkedlist()
    # ll.insert_at_begginning(5)  
    # ll.insert_at_begginning(50)
    # ll.insert_at_begginning(15)   
    # ll.insert_at_begginning(55)  
    # ll.insert_at_begginning(500)
    # ll.insert_at_begginning(150)
    ll.insert_at_end(200)
    ll.insert_at_end(1150)    
    ll.print()                                

