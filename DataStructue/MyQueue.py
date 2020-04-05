from LinkedList import Node
"""
    顺序队列
    重点代码
    操作：初始化
         队列是否为空
         入队
         出队
"""

class QueueError(Exception):
    pass

class SQueue:
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def enqueue(self,val):
        self._elems.append(val)

    def dequeue(self):
        if self.is_empty():
            raise QueueError("Queue is empty.")
        return self._elems.pop(0)

# if __name__ == "__main__":
#     sq = SQueue()
#     print(sq.is_empty())
#     sq.enqueue(10)
#     sq.enqueue(20)
#     sq.enqueue(30)
#     while not sq.is_empty():
#         print(sq.dequeue())

"""
    链式队列
"""
class LQueue:
    def __init__(self):
        self.front = Node(None)
        self._rear = Node(None)

    def is_empty(self):
        return self._rear is self.front

    def enqueue(self,val):
        self._rear.next = Node(val)
        self._rear = self._rear.next

    def dequeue(self):
        if self.is_empty():
            raise QueueError("Queue is empty.")

        self.front = self.front.next
        return self.front.val

if __name__ == "__main__":
    qu = LQueue()
    print(qu.is_empty())
    qu.enqueue(9)
    qu.enqueue(8)
    qu.enqueue(12)
    while not qu.is_empty():
        print(qu.dequeue())