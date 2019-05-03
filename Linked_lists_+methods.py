class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node isnt in the list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        cur_node = self.head
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return
        prev = None
        count = 1
        while cur_node and count != pos:
             prev = cur_node
             cur_node = cur_node.next
             count += 1
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None

    def len_iterative(self):
        cur_node = self.head
        count = 0
        while cur_node:
            count+=1
            cur_node = cur_node.next
        return count
    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)
    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return
        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next
        if not curr_1 or not curr_2:
            return
        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def print_helper(self, node, name):
        if node is None:
            print(name + ": None")
        else:
            print(name + ":" + node.data)

    def reverse_iterative(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            self.print_helper(prev, "PREV")
            self.print_helper(curr, "CURR")
            self.print_helper(nxt, "NXT")
            prev = curr
            curr = nxt
        self.head = prev
    def reverse_recursive(self):

        def _reverse_recursive(curr, prev):
            if not curr:
                return prev

            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            return _reverse_recursive(curr, prev)
        self.head = _reverse_recursive(curr=self.head, prev=None)

    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None
        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
        new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p
        return new_head
    def remove_duplicates(self):
        curr = self.head
        prev = None
        dup_values = dict()

        while curr:
            if curr.data in dup_values:
                #remove node
                prev.next = curr.next
                curr = None
            else:
                #have not included node before
                dup_values[curr.data] = 1
                prev = curr
            curr = prev.next
    def n_to_the_last_node(self, n):
        #find length of list
        total_len = self.len_iterative()
        curr = self.head


        #move through list until at position
        while curr:
             if total_len ==n:
                 print(curr.data)
                 return curr
             total_len -= 1
             curr = curr.next
             if curr is None:
                return


        return curr.data
    def _n_to_the_last_node(self, n):
        p = self.head
        q = self.head

        count = 0
        while q and count < n:
            q = q.next
            count += 1
        if not q:
            print( str(n) + " is greater than the length of the list.")
            return
        while p and q:
            p = p.next
            q = q.next
        return p.data
    def count_occurances_iterative(self, data):
        count = 0
        curr = self.head
        while curr:
            if curr.data == data:
                count += 1
            curr = curr.next
        return count

    def count_occurances_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurances_recursive(node.next, data)
        else:
            return self.count_occurances_recursive(node.next, data)


#    1 -> 1 -> 6 -> 1 -> 7 -> 1 -> 10

llist = Linked_List()
llist.print_list()
llist.append(1)
llist.append(1)
llist.append(6)
llist.append(1)
llist.append(7)
llist.append(1)
llist.append(10)


#print("   ")
#def unique_in_order(iterable):
#    iterable = list(iterable)
#    a = 0
 #   b = 1
 #   try:
  #      while iterable[b]:
  #         if iterable[a] == iterable[b]:
 #               iterable.pop(a)
#            a = a + 1
 #           b = b + 1
#
   # return(iterable)

x = "12"
for a in x[0:2]:
    print(a)
