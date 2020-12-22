class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def printLinkedList(self):
        value = self.head
        while (value):
            print(value.data)
            value = value.next

    def transverse(self):
        if self.head is None:
            print("This is an empty list")
            return 0
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next
   
    def length(self):
        l = 0
        if self.head is None:
             pass
        else:
            n = self.head
            while n is not None:
                l += 1
                n = n.next
        return l
            

    def reverse(self):
        if self.head is None:
            print("This is an empty list")
            return 0
        else:
            l = LinkedList.length(self)
            address = [0] * l
            reverse = LinkedList()
            n = self.head
            while n is not None:
                if n == self.head:
                    address[l-1] = Node(self.head.data,None)
                else:
                    address[l-1] = Node(n.data,address[l])
                n = n.next
                l -= 1
            reverse.head = address[0]
            return reverse


linkedlist = LinkedList()
third = Node(1,None)
second = Node(0,third)
linkedlist.head = Node(2,second)

LinkedList.printLinkedList(linkedlist)
LinkedList.transverse(linkedlist)
print(LinkedList.length(linkedlist))
LinkedList.transverse(LinkedList.reverse(linkedlist))
 #
 #
 #
 #
 #
 #
 #
 #
 #
 #
 #
 #
