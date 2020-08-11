class Node:
    def __init__(self,value):
        self.value=value
        self.next_node=None


# n1=Node(10)
# n2=Node(15)
# n1.next_node=n2
# n1.value
# print(n1.next_node.value)
# n3=Node(11)
# n2.next_node=n3
# print(n1.next_node.next_node.value)

class LinkList:
    def __init__(self,L=None):
        if not L:
            self.head=None
            return
        self.head=Node(L[0])
        current_node=self.head
        for e in L[1:]:
            current_node.next_node=Node(e)
            current_node= current_node.next_node

    def display(self,separator=','):
        E=[]
        current_node=self.head
        while current_node:
            E.append(current_node.value)
            current_node=current_node.next_node
            #当现在的node存在时，就把他们拼到E里面去
        print(separator.join(str(e)for e in E))

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
        while self.head.value!=value_2:
            current_node=current_node.next_node
        if current_node.next_node.value==value_2:
            new_node=Node(value_1)
            new_node.next_node=current_node.next_node
            current_node.next_node=new_node
            return True
        return False




LL=LinkList([1,10,4])
LL.insert_before(-10,1)
# LL.display('---')
# print(len(LL))
# LL.insert_at_beginning(20)
# LL.display()
LL.insert_before(62,10)
LL.display()
LL.insert_before(6,4)
LL.display()
# print(LL.head.value)
# print(LL.head.next_node.value)
# print(LL.head.next_node.next_node.value)


