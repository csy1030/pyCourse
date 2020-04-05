from Stack import *

# 检测括号是否成对出现
def is_paired(data):
    left_p = ["(","[","{"]
    right_p = [")","]","}"]
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    st = SStack()
    i = 0
    for item in data:
        i = 0
        if item in left_p:
            st.push(item)
        elif item in right_p:
            if not st.is_emtpy():
                if pairs[item] == st.top():
                    st.pop()
            else:
                return False

    return st.is_emtpy()

def parenth(text):
    parenths = ["(",")","[","]","{","}"]
    dict01 = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    i,text_len = 0, len(text)
    while True:
        while i < text_len and text[i] not in parenths:
            i += 1
        if i >= text_len:
            return
        else:
            yield text[i],i
            i += 1

data = "A (stack) is[ a] linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner. In stack, a new element is adde{d [at on]e end and[ an element is removed] from t}hat end only. The insert and delete operations are often called push and pop."

# for item,i in parenth(data):
#     print(item,i)


if __name__ == "__main__":
    data = "A (stack) is[ a] linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner. In stack, a new element is adde{d [at on]e end and[ an element is removed] from t}hat end only. The insert and delete operations are often called push and pop."
    data1 = "(((([]))))1212"
    # print(is_paired(data1))



"""
    作业
    逆波兰表达式
    1 2 + p = 3
    2 3 + 6 - 7 + p = 6
    用链栈解决
"""
def re_poland(line):
    st = LStack()
    sign = ["+","-","*","/"]
    for item in line:
        if item != " ":
            if item in sign:
                b = int(st.pop())
                a = int(st.pop())
                if item == "+":
                    c = a + b
                elif item == "-":
                    c = a - b
                elif item == "*":
                    c = a * b
                else:
                    c = a / b
                st.push(c)

            elif item == "p":
                return st.top()
            else:
                st.push(item)

print(re_poland("1 2 + 3 / 6 * p"))
