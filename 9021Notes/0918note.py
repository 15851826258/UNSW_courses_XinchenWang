class Node:
    def __init__(self,value):
        self.value = value
        self.next_node= None

n1 = Node(10)
n2 = Node(15)
n1.next_node=n2
n3=Node(11)
n2.next_node=n3
n1.next_node.next_node.value


class linkedlist:
    def __init__(self,l=None):
        if not l:
            self.head=None
            return
        self.head=Node(l[0])
        current_node=self.head
        for e in l[1:]:
            new_node=Node(e)
            current_node.next_node=Node(e)
            current_node=current_node.next_node
    def display(self,separateor=','):
        E=[]
        current_node=self.head
        while current_node:
            E.append(current_node.value)
            current_node=current_node.next_node
        print(separateor.join(str(e) for e in E))
    def __len__(self):
        if not self.head:
            return 0
        length=0
        current_node=self.head
        while current_node:
            length+=1
            current_node=current_node.next_node
        return length
    def append(self,value):
        new_node=Node(value)
        if not self.head:
            self.head=new_node
            return
        current_node=self.head
        while current_node.next_node:
            current_node=current_node.next_node
        current_node.next_node=new_node

    def insert_at_beginning(self,value):
        new_node=Node(value)
        if not self.head:
            self.head=new_node
            return
        new_node.next_node=self.head
        self.head=new_node

    def insert_before(self,value_1,value_2):
        if not self.head:
            return False
        if self.head.value==value_2:
            new_node=Node(value_1)
            new_node.next_node=self.head
            self.head=new_node
            return True
        current_node=self.head
        while current_node.value!=value_2:
            current_node=current_node.next_node
        if current_node.next_node.value==value_2:
            new_node=Node(value_1)
            new_node.next_node=current_node.next_node
            current_node.next_node=new_node
            return False
        return False


    def reverse(self):
        pass






ll=linkedlist([1,10,4])
ll.display('-----')
len(ll)
ll.append(7)
ll.display()
# ll.insert_at_beginning(20)
# ll.display()
ll.insert_before(62,10)
ll.display()


