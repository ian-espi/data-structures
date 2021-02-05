# Ian Espinosa
# IanEspinosaBiz@gmail.com
# CS 22 LBCC Spring 2017

#  ANSWER KEY - Implement double linked list Deque
# by Gerry jenkins
#  The idea is to implement the Deque ADT specified in
#
# if you set the debug variable below to True, it will dump your deque out in detail after each test before it tests
# with asserts

debug = True

#
# Listing 3.14, this means that you must implement all the ADT methods
#
#     isEmpty(),
#     addFront(item),
#     addRear(item),
#     removeFront(item)
#     removeRear(item), and
#     size()
#
# I have asked you to implement this ADT with a double linked list implementation and add the pop(i) method.
#
# If you redo you assignment and use the following template, fill in your code in the ???
# the extra code for __str__, dump and main will test your code.
#
# You can use dq.dump() to see the internal structure of the que at any point in the testing
#

# starter code  **** The code below is designed to give you a template to put your code to implement a
# linked list version of deque, you will see lines designated where you replace your code where the line is.
# NOTE, the python keyword pass, does nothing except serve as a placeholder for code, they are there so you can
# work on getting one method at a time working and tested without having syntac errors.
# when you run this file, it fails righ after it trys to addFront(11)
# because both addFront(d) and size() have not been written,
# so these are the first two methods you should write the code for

# picture of nodes in a linked list
#
#                      --------   --------   --------
# self.front  -------> | data |   | data |   | data | <---------- self.rear
#                      | next |-->| next |-->| next |--> None
#             None <-- | prev |<--| prev |<--| prev |
#                      --------   --------    --------
#                        node0     node1       node2
#
# ----------------------------------------------------------------------------------
# Start of code here:


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# these are the defs you need for deque (page 121, Listing 3.14)


class Deque:

    def __init__(self):  # construct a empty deque to start
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front == None and self.rear == None

    def addFront(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.front = newNode
            self.rear = newNode
        else:
            newNode.next = self.front
            self.front.prev = newNode
            self.front = newNode

    def addRear(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.rear = newNode
            self.front = newNode
        else:
            newNode.prev = self.rear
            self.rear.next = newNode
            self.rear = newNode

    def removeFront(self):
        # removes front node and returns data reference
        # return None if empty deque
        if self.isEmpty():
            return None
        elif self.size() == 1:
            willRemovedFont = self.front
            self.front = None
            self.rear = None

            return willRemovedFont.data
        else:
            willRemovedFont = self.front
            self.front = self.front.next
            self.front.prev = None

            return willRemovedFont.data

    def removeRear(self):
        # removes rear node and returns data reference
        # return None if empty deque
        if self.isEmpty():
            return None
        elif self.size() == 1:
            willRemovedRear = self.rear
            self.rear = None
            self.front = None

            return willRemovedRear.data
        else:
            willRemovedRear = self.rear
            self.rear = self.rear.prev
            self.rear.next = None

            return willRemovedRear.data

    def pop(self, index):
        # remove noded indexed: index indicated by index 0,1,2 count from front to rear
        # index -1,-2,-3 counts from rear toward front
        # return None if list is empty before pop
        # NOTE: make sure to return the data that was popped, not the node
        if self.isEmpty():
            return None
        elif self.size() == 1:
            return self.removeFront()
        else:
            if index > 0:
                leftSizeOfCurrent = self.front
                current = self.front.next
                dequeIndex = 1
                while dequeIndex != index:
                    dequeIndex += 1
                    leftSizeOfCurrent = current
                    current = current.next
                willPopedNode = current
                rightSizeOfCurrent = current.next
                rightSizeOfCurrent.prev = leftSizeOfCurrent
                leftSizeOfCurrent.next = rightSizeOfCurrent

                return willPopedNode.data
            elif index < 0:  # negative number
                if index == -1:
                    return self.removeRear()
                else:
                    current = self.rear
                    leftSizeOfCurrent = current.prev
                    dequeIndex = -1
                    while dequeIndex != index:
                        dequeIndex -= 1
                        current = leftSizeOfCurrent
                        leftSizeOfCurrent = current.prev
                    willPopedNode = current
                    rightSizeOfCurrent = current.next
                    rightSizeOfCurrent.prev = leftSizeOfCurrent
                    leftSizeOfCurrent.next = rightSizeOfCurrent

                    return willPopedNode.data
            else:
                return self.removeFront()

    def size(self):
        # HINT: count nodes in deque by traversing them
        current = self.front
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

# DO NOT MODIFY ANY OF THE CODE AFTER THIS POINT
    # code after this point, is for the testing, it includes __str__ and dump()
    #-------------------------------------------------------------------------

    # these first items are added to the definition of Deque class

    def __str__(self):  # print deque
        node = self.front
        s = ""
        while node is not None:
            s += str(node.data) + ", "
            node = node.next
        return "[ " + s[0:-2] + " ]"

    _nodes = {}  # dictinary to map node id to n1, n2, n2 to make reading dump easier
    _index = 1  # used to keep track of first n that is not used in node names

    def peekFront(self):  # return front node data reference or None
        if self.front == None:
            return None
        return self.front.data

    def peekRear(self):  # return rear node data reference or None
        if self.rear == None:
            return None
        return self.rear.data

    def dump(self):  # new version to name the nodes found n1, n2, etc.
        # instead of dumping raw id numbers

        def addr(x):
            if x is None:
                return "None"
            else:
                if id(x) in self._nodes:
                    return self._nodes[id(x)]
                else:
                    self._nodes[id(x)] = "n%d" % (self._index)
                    self._index += 1
                    return self._nodes[id(x)]

        print ("  ", "-" * 20, " DUMP of Deque ", "-" * 20)
        print ("    self.front: ", addr(self.front))
        node = self.front

        while node is not None:
            print ("\n     Node: ", addr(node))
            print ("         data: ", node.data)
            print ("         next: ", addr(node.next))
            print ("         prev: ", addr(node.prev))
            node = node.next
        print("\n    self.rear: ", addr(self.rear))
        print("  ", "-" * 50)

    def integrity_check(self):
        if self.front == None:
            assert self.rear is None, "rear is not None for empty deque"
        else:
            forward = []
            node = self.front
            while node is not None:
                forward.append(node)
                node = node.next
            node = self.rear

            node = self.rear
            while node is not None:
                assert forward.pop() == node,\
                    "prev for node does not match \n" +\
                    str(id(forward[len(forward) - 1])) + " <=> " + str(id(node)) +\
                    "for node number " + str(len(forward))
                node = node.prev

# END of Deque Class definition
#----------------------------------------------------

# main() will test your deque class by creating an object of type Deque
# and then do a series of call to your deque object.
#
# for each call involving your class it does the follown
# 1. print out what call it just did and what is on the que when done
# 2. if debug variable is True it will dump the entire structure of the dq object
# 3. does a series of assert statements to test if the call just completed worked
# 4. calls a method called integrity_check which will try to follow all the links in your dq object to see
#    if they are good.
#


def main():

    dq = Deque()
    print("new Deque(), and the size is ", dq.size())  # 0
    print("dq after: ", dq)
    if debug:
        dq.dump()
    dq.integrity_check()

    dq.addFront(11)
    print("dq.addFront(11), dq after: ", dq)  # 0
    if debug:
        dq.dump()  # dump out structure so you can see
    assert dq.size() == 1, "size should now be 1"
    assert dq.peekFront() == 11, "front node data should be 11"
    assert dq.isEmpty() == False, "isEmpty should return False"
    dq.integrity_check()

    dq.addFront(22)
    print("dq.addFront(22), dq after: ", dq)  # 0
    if debug:
        dq.dump()  # dump out structure so you can see
    assert dq.size() == 2, "size should now be 2"
    assert dq.peekFront() == 22, "front node data should be 22"
    assert dq.peekRear() == 11, "rear node data should be 11"
    dq.integrity_check()

    dq.addFront(55)
    print("dq.addFront(55), dq after: ", dq)  # 0
    if debug:
        dq.dump()  # dump out structure so you can see
    assert dq.size() == 3, "size should now be 3"
    assert dq.peekFront() == 55, "font node data should be 22"
    dq.integrity_check()

    data = dq.removeFront()
    print("dq.removeFront(), dq after: ", dq)
    if debug:
        dq.dump()  # dump out structure so you can see
    assert data == 55, "removeFront() should return 55"
    assert dq.peekFront() == 22, "front node data should now be 22"
    assert dq.size() == 2, "size should now be 2"
    dq.integrity_check()

    dq.addRear(9)
    print("dq.addRear(9), dq after: ", dq)
    if debug:
        dq.dump()  # dump out structure so you can see
    assert dq.size() == 3, "size should now be 3"
    assert dq.peekRear() == 9, "front node data should now be 9"
    dq.integrity_check()

    dq.addRear(1)
    print("dq.addRear(1), dq after: ", dq)
    if debug:
        dq.dump()  # dump out structure so you can see
    assert dq.size() == 4, "size should now be 4"
    dq.integrity_check()

    dq.addRear(99)
    print("dq.addRear(1), dq after: ", dq)
    if debug:
        dq.dump()  # dump out structure so you can see
    assert dq.size() == 5, "size should now be 5"
    dq.integrity_check()

    data = dq.removeRear()
    print("dq.removeRear(), dq after: ", dq)
    if debug:
        dq.dump()  # dump out structure so you can see
    assert data == 99, "removeRear() should return 1"
    assert dq.peekRear() == 1, "Rear node data should now be 22"
    assert dq.size() == 4, "size should now be 4"
    dq.integrity_check()

    print("-------\nNOW EXTRA CREDIT TESTS:\n")

    n = dq.pop(1)
    print("dq.pop(1), dq after: ", dq)
    if debug:
        dq.dump()  # dump out structure so you can see
    print("  returned: ", n)
    if debug:
        dq.dump()  # dump out structure so you can see
    assert n == 11, "pop(1) should have returned 9 "
    assert dq.size() == 3, "size should now be 3"
    dq.integrity_check()

    n = dq.pop(-1)
    print("dq.pop(-1), dq after: ", dq)
    print("  returned: ", n)
    if debug:
        dq.dump()  # dump out structure so you can see
    assert n == 1, "pop(-1) should have returned 1 "
    assert dq.size() == 2, "size should now be 2"
    dq.integrity_check()

    n = dq.pop(0)
    print("dq.pop(0), dq after: ", dq)
    print("  returned: ", n)
    if debug:
        dq.dump()  # dump out structure so you can see
    assert n == 22, "pop(0) should have returned 22 "
    assert dq.size() == 1, "size should now be 1"
    dq.integrity_check()

    n = dq.pop(-1)
    print("dq.pop(-1), dq after: ", dq)
    print("  returned: ", n)
    if debug:
        dq.dump()  # dump out structure so you can see
    assert n == 9, "pop(-1) should have returned 9 "
    assert dq.size() == 0, "size should now be 0"
    assert dq.isEmpty() == True, "isEmpty should return True"
    dq.integrity_check()
#----------------------------------------------


# now test it
main()
