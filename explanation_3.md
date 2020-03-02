# Why I choose this data structure
I copied Queue, Tree and Node from the course notebook.

I used a set object to store all the unique char.

I modified Node to store both char and its count.

I modified Tree so that I can combine 2 trees by adding a new root and connecting the new root to the two trees' roots.

I used a python list to store all the trees. So I can use this list's index later.

I used PriorityQueue to arrange trees. item's priority is associated with the count of tree root.

# Time Complexity
encoding's time complexity is O(n + log(n)) or O(n)
There is a `for loop` for building the priority queue, which has time complexity of O(n), in which
n means the number of chars in the message to encode.
The `while loop` has a time complexity of O(log(n)) because the size of the queue is shrinking.

The decoding's time complexity is also O(n)
There is a for loop for the input which is "0" or "1" string.

# Space Complexity
O(n)
In the worst case, the input is comprised of unique chars, so there is no way to compress.
There will be n leaves in the tree, where n is the number of chars in a input to be encoded.
