# Written by **** for COMP9021

from linked_list_adt import *


class ExtendedLinkedList(LinkedList):
    def __init__(self, L=None):
        super().__init__(L)

    def rearrange(self, step):
        count=1
        #count是跳的次数 所以加一再在循环里自增可以得到总长度
        now_node = self.head
        while now_node.next_node:
            now_node = now_node.next_node
            count+=1
        if step==1:
            return
        if count > step:
            #当总长度比步数大的时候才操作，如果步数大于总长度，那么不操作，直接返回原来的长度。
            end_node = now_node
            # 遍历链表，找到最后一个结点跟头连起来
            now_node.next_node = self.head
            # 把头尾相连
            pre_node = end_node
            for i in range(0, step - 1):
                pre_node = pre_node.next_node
            # 对于前项的操作从末尾往前取step-1个
            self.head = pre_node.next_node
            now_node = pre_node.next_node
            pre_node.next_node = pre_node.next_node.next_node
            pre_node = self.head
            # 设定起始的第一个
            while step > 1:
                for i in range(step - 1):
                    now_node = now_node.next_node
                    if now_node == end_node:
                        # 如果走到了尾节点 说明结束了一整个循环 这时候step-1，因为之前的每一个区间都少了一个数
                        step = step - 1
                pre_node.next_node = now_node.next_node
                now_node.next_node = now_node.next_node.next_node
                now_node = pre_node.next_node
                pre_node = now_node
            end_node.next_node = None
        # 最后把头尾断开





