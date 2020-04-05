"""
    单链表
    重点程序
"""

# 创建结点类
class Node:
    def __init__(self,val,next = None):
        self.val = val # 有用数据
        self.next = next

# 链表的操作
class LinkList:
    def __init__(self):
        self.head = Node(None)# 将头结点指向无用的一个结点

    def init_list(self,target):
        p = self.head # 可移动变量p
        for item in target:
            p.next = Node(item)
            p = p.next

    def show(self):
        p = self.head.next
        if p is not None:
            while p:
                print(p.val,end = ' ')
                p = p.next
            print()
        else: print("Linkedlist is empty.")

    #在尾部插入新结点
    def append(self,target):
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(target)

    # 获取链表长度
    def get_len(self):
        count = 0
        p = self.head
        while p.next:
            count += 1
            p = p.next
        return count

    # 判断链表是否为空
    def is_empty(self):
        return True if self.get_len() == 0 else False

    # 清空链表
    def clear(self):
        self.head.next = None

    # 获取元素值
    def get_item(self,pos):
        p = self.head.next
        count = 0
        # try:
        #     if self.get_len() < pos:
        #         raise IndexError("list index out of range")
        # except:
        while count < pos and p:
            p = p.next
            count += 1
        if p is None:
            raise IndexError("List index out of range")
        else:
            return p.val

    # 在某个索引位置插入数据
    def insert(self,pos,val):
        if pos < 0 or pos > self.get_len():
            raise IndexError("List index out of range.")
        p = self.head.next
        count = 0
        while count < pos:
            count += 1
            p = p.next
        node = Node(val)
        node.next = p.next
        p.next = node

    # 删除元素
    def delete(self,target):
        p = self.head
        while p.next:
            if p.next.val == target:
                p.next = p.next.next
                break
            p = p.next
        else: raise ValueError("x not in list.")





if __name__ == "__main__":
    link = LinkList()
    # 初始数据
    l = [1,2,3,4,5,6]
    link.init_list(l)
    link.append(10)
    link.show()
    print("length=",link.get_len())
    # link.clear()
    # link.show()
    # print(link.get_item(9))
    link.insert(3,19)
    link.show()
    link.delete(19)
    link.show()

