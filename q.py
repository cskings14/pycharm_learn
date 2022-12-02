class Queue:
    def __init__(self, q=[]):
        self.q = q

    def enqueue(self, number):
        self.q.append(number)

    def dequeue(self):
        num = self.q[0]
        self.q.pop(0)
        return num


# qq = Queue()
#
# qq.enqueue(4)
# qq.enqueue(5)
# qq.enqueue(45)
# qq.enqueue(63)

# print(qq.dequeue())
# print(qq.dequeue())




# ss = Stack()
#
# ss.push(5)
# ss.push(4)
# ss.push(3)
# ss.push(422)
# ss.push(11)

# print(ss.pop())
# print(ss.pop())


class Node:
    def __init__(self, number):
        self.number = number
        self.next = None


firstNode = Node(1)
secondNode = Node(2)
thirdNode = Node(3)

firstNode.next = secondNode
secondNode.next = thirdNode




class Stack:
    def __init__(self, s=[]):
        self.s = s

    def push(self, number):
        self.s.insert(0, number)

    def pop(self):
        num = self.s[0]
        self.s.pop(0)
        return num

    def isEmpty(self):
        if len(self.s) > 0:
            return False
        return True





class Test:
    def __init__(self, node):
        self.node = node

    def printInOrder(self):
        print(self.node.number)
        n = self.node

        while n.next is not None:
            n = n.next
            print(n.number)

    def printInReverse(self):
        s = Stack()
        s.push(self.node.number)
        n = self.node
        while n.next is not None:
            n = n.next
            s.push(n.number)
        while s.isEmpty() is False:
            # last number that gets pushed is the first number to be popped
            print(s.pop())














t = Test(firstNode)
t.printInOrder()
t.printInReverse()




















