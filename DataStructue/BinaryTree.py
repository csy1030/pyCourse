def factorial(n):
    if n < 1:
        return 1
    return n * factorial(n - 1)

print("5!=%d" % factorial(5))



"""
    链式存储二叉树
    初始化
    遍历
"""

class TreeNode:
    def __init__(self,data,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right

"""
    二叉树的构建与遍历
    重点代码
"""
class BinaryTree:
    def __init__(self,root = None):
        self.root = root

    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False

    def pre_order(self,node):
        # 先打印根， 再打印左节点，
        # 打印时，把他当做根，打印左右节点 递归
        if node is None:
            return
        print(node.data)
        self.pre_order(node.left)
        self.pre_order(node.right)

    def mid_order(self,node):
        # 左根右
        if node is None:
            return
        self.mid_order(node.left)
        print(node.data)
        self.mid_order(node.right)

    def post_order(self,node):
        # 左根右
        if node is None:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.data)

from MyQueue import *
    def level_Order(self,node):
        qu = SQueue()
        qu.enqueue(node)
        while not qu.is_empty():
            node = qu.dequeue()
            print(node.data)
            if node.left:
                qu.enqueue(node.left)
            if node.right:
                qu.enqueue(node.right)




if __name__ == "__main__":
    # 按照后序遍历增加节点
    b = TreeNode('B')
    f = TreeNode('F')
    g = TreeNode('G')
    d = TreeNode('D',f,g)
    i = TreeNode('I')
    h = TreeNode('H')
    e = TreeNode('E',i,h)
    c = TreeNode('C',d,e)
    a = TreeNode('A',b,c) # 根节点
    bt = BinaryTree(a) # 初始化树对象，传入根节点

    bt.pre_order(a)
    print("mid_order-------")
    bt.mid_order(a)
    print("post_order-------")
    bt.post_order(a)

