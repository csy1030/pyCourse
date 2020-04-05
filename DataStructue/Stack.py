from LinkedList import Node

"""
    栈的顺序结构
    重点代码
"""
# 自定义栈错误
class StackError(Exception):
    pass

# 基于列表实现顺序栈
class SStack:
    def __init__(self):
        # 约定列表的最后一个元素为栈顶元素
        self._elems = []
    def top(self):
        if not self._elems:
            raise StackError("stack is empty.")
        return self._elems[-1]

    def is_emtpy(self):
        return self._elems == []

    def push(self,val):
        self._elems.append(val)
    def pop(self):
        if self.is_emtpy():
            raise StackError("stack is empty")
        return self._elems.pop()


    def show(self):
        for item in self._elems:
            print(item)


if __name__ == "__main__":
    st = SStack()

    st.push(1)
    st.push(2)
    st.push(3)
    while not st.is_emtpy():
        print(st.pop())




"""
    栈的链式存储
"""

class StackError(Exception):
    pass

class LStack:
    def __init__(self):
        # 标记栈顶位置
        self._top = None

    def is_empty(self):
        return self._top is None

    def push(self,val):
        self._top = Node(val,self._top)
        # node = Node(val)
        # node.next = self._top
        # self._top = node

    def pop(self):
        if self._top is None:
            raise StackError("Stack is empty.")
        p = self._top
        self._top = p.next
        return p.val

    def top(self):
        if self._top is None:
            raise StackError("Stack is empty.")
        return self._top.val


if __name__ == "__main__":
    st = LStack()
    st.push(1)
    st.push(3)
    st.push(5)
    print(st.pop())
    print(st.top())
    print(st.top())

