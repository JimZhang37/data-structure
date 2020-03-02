# Why I choose this data structure
I chose a double linked list and a dictionary to implement LRU.
As the dictionary has O(1) time complexity to assess data and all its keys are unique, to read  items in the cache is fast.

Since the size of the cache is limited, the double linked list is used to delete item in the head
of the queue. There are one pointer to the head and another to the tail. So to add to the tail or
to delete the head has a time complexity of O(1)
When a item in the cache is hit, the operation is to remove the item in the queue and re-add it
in the tail. To remove an item in the middle of the queue, the dictionary is used. The value of the
dictionary is the node, which contains both pointers to previous and next node. 
So to remove an item requires only O(n) time.
# Time Complexity
get(): O(1):

set(): O(1):

# Space Complexity
O(1)
The space used is constant as the size of the dictionary and queue don't change. They all 
depends on the capacity parameter, not the input.
