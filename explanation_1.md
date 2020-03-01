# Why I choose this data structure
I chose a python list as my queue to store the cache, but it's different from normal queue. When an item in the cache is recently used, it will be put in the tail again.
python list has 2 functions, append() and pop(0), that can be used as enque() and deque(). 
python list has 1 function, remove(key) and append(), that are used to move a item to the tail of the queue.

I also chose to use python set to store the data in cache. When the size of the set reaches 5, the limit of the cache, I will know I have to deque() before I can enque() another item.

# Time Complexity
get(): O(n):
Because I use list.remove(), the time complexity becomes O(n)

set(): O(n):
I use list.remove(), which has a time complexity of O(n)