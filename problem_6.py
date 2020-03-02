import copy

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = "{"
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        out_string += "}"
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next
        new_node = Node(value)
        node.next = new_node
        new_node.prev =node

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    # Your Solution Here
    llist_1 = copy.deepcopy(llist_1)
    llist_2 = copy.deepcopy(llist_2)
    if llist_1.head is None:
        return setlist(llist_2)
    else:
        node = llist_1.head
        while node.next:
            node = node.next
        node.next = llist_2.head
        return setlist(llist_1)


def setlist(llist):

    if llist.head is None:
        return llist
    else:
        s = set()
        node = llist.head
        s.add(node.value)
        next = node.next
        while next:
            if next.value not in s:
                s.add(next.value)
                node = next
                next = next.next
            else:
                node.next = next.next
                next = next.next
        return llist


def intersection(llist_1, llist_2):
    # Your Solution Here
    list3 = LinkedList()
    if (llist_2.size() == 0) or (llist_1.size() == 0) :
        return list3

    llist_1 = copy.deepcopy(llist_1)
    llist_2 = copy.deepcopy(llist_2)
    llist_1 = setlist(llist_1)
    llist_2 = setlist(llist_2)

    size1 = llist_1.size()
    size2 = llist_2.size()
    if size1 > size2:
        newlist = llist_1
        llist_1 = llist_2
        llist_2 = newlist

    node = llist_1.head
    while node:
        node2 = llist_2.head
        while node2:
            if node.value == node2.value:
                list3.append(node.value)
                if node2 is llist_2.head:
                    llist_2.head = node2.next
                else:
                    node2.prev.next = node2.next
                    if node2.next is not None:
                        node2.next.prev = node2.prev
                break
            else:
                node2 = node2.next

        node = node.next


    return list3


# Test case 1
print("test 1")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1,linked_list_2)) #expect {32, 65, 2, 35, 3, 4, 6, 1, 9, 11, 21}

print(intersection(linked_list_1,linked_list_2)) # expect {4, 21, 6}

# Test case 2
print("test2")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3,linked_list_4)) # expect {65, 2, 35, 3, 4, 6, 1, 7, 8, 9, 11, 21, 23}
print(intersection(linked_list_3,linked_list_4)) # expect {}

# Test case 3
print("test 3")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [2, 2]
element_2 = [1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3,linked_list_4)) # expect {1, 2}
print(intersection(linked_list_3,linked_list_4)) # expect {}