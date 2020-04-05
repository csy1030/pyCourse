from greenlet import greenlet

def test1():
    print("1")
    gr2.switch()
    print("1-1")

def test2():
    print("2")
    gr1.switch()
    print("2-2")

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()  # 执行协程test1
