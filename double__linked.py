class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head == None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
            new_node.next = None

    def preppend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.pre = None

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
    def add_after_node(self, key, data):
        curr = self.head
        while curr:
            if curr.next is None and curr.data == key:
                self.append(data)
                return
            elif curr.data == key:
                new_node = Node(data)
                nxt = curr.next
                curr.next = new_node
                new_node.next = nxt
                nxt.prev = new_node
            curr = curr.next

    def add_before_node(self, key, data):
        curr = self.head
        while curr:
            if curr.prev is None and curr.data == key:
                self.preppend(data)
            elif curr.data == key:
                new_node = Node(data)
                new_node.data = data
                prev = curr.prev
                prev.next = new_node
                curr.prev = new_node
                new_node.next = curr
                

            curr = curr.next
    def delete(self, key):
        curr = self.head
        while curr:

            if curr.data == key and curr == self.head:
                #case 1
                if not curr.next:
                    curr = None
                    self.head = None
                    return
                else:
                    #case 2
                    nxt = curr.next
                    curr.next = None
                    nxt.prev = None
                    curr = None
                    self.head = nxt
                    return

            #case 3
            elif curr.data == key:
                if curr.next:
                    nxt = curr.next
                    prev = curr.prev
                    prev.next = nxt
                    nxt.prev = prev
                    curr.next = None
                    curr.prev = None
                    curr = None
                    return
                # case 4
                else:
                    prev = curr.prev
                    prev.next = None
                    curr.prev = None
                    curr = None
                    return
            curr = curr.nex
    def delete_node(self, node):
        curr = self.head
        while curr:

            if curr ==node and curr == self.head:
                #case 1
                if not curr.next:
                    curr = None
                    self.head = None
                    return
                else:
                    #case 2
                    nxt = curr.next
                    curr.next = None
                    nxt.prev = None
                    curr = None
                    self.head = nxt
                    return

            #case 3
            elif curr == node:
                if curr.next:
                    nxt = curr.next
                    prev = curr.prev
                    prev.next = nxt
                    nxt.prev = prev
                    curr.next = None
                    curr.prev = None
                    curr = None
                    return
                # case 4
                else:
                    prev = curr.prev
                    prev.next = None
                    curr.prev = None
                    curr = None
                    return
            curr = curr.next
    def reverse(self):
        tmp = None
        curr = self.head
        while curr:
            tmp = curr.prev
            curr.prev = curr.next
            curr.next = tmp
            curr = curr.prev
        if tmp:
            self.head = tmp.prev
    def remove_duplicates(self):
        pass

dllist = DoubleLinkedList()
dllist.append("1")
dllist.append("2")
dllist.append("3")
dllist.append("4")
dllist.print_list()
print()
dllist.add_before_node("2", 12)
dllist.print_list()
