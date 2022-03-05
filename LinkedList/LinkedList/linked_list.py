class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
        self.size=0

    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node
        self.size+=1
    def inser_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
        self.size += 1

    def print(self):
        if self.head is None:
            print("Empty")
            return
        itr=self.head
        listr=''
        while itr:
            listr+=str(itr.data)+"-->"
            itr=itr.next
        listr+="END"
        print(listr)
        print(self.size)



if __name__=="__main__":
    ll=LinkedList()
    ll.insert_at_beginning(5)

    ll.insert_at_beginning(6)
    ll.insert_at_beginning(7)
    ll.insert_at_beginning(8)

    ll.print()

