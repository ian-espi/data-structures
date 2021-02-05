class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1


class PriorityQueue:
    def __init__(self):
        self.bh = BinHeap()

    def enqueue(self, item):
        self.bh.insert(item)

    def dequeue(self):
        return self.bh.delMin()


myQueue = PriorityQueue()
myQueue.enqueue(2)
myQueue.enqueue(20)
myQueue.enqueue(30)
myQueue.enqueue(5)
myQueue.enqueue(7)

print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.dequeue())

import random
for n in [1,2,5,10,20]: # do sequence of each of these lengths
    l1 = [ i+1 for i in range(n)] # list from 1 to n
    l2 = l1.copy() # duplicate the list l1
    random.shuffle(l2) # shuffle it before adding to priority queue pq
    pq = PriorityQueue()
    print("test inserts from: ",l2)
    for i in l2: # add each element from l2
        pq.enqueue(i)
    for i in l1: # check that when dequeued they are lowest to highest [1,2,3...n]
        assert i == pq.dequeue()

print("ALL PASSED")

