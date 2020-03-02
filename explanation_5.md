# Why I choose this data structure
A link structure is chosen here.
I chose to use both head and tail to indicate the two ends of the chain.
By using tail, the operation to append can be easier.

# Time Complexity
O(1)
The time complexity is constant as all the new block is just connected to the tail.
The append() function has a constant time complexity.

# Space Complexity
O(n)
The space required is dependent on the number of block. The more, the bigger.