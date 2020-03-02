# Why I choose this data structure
The Group class is given, so I don't have to invent a new data structure.

The algorithm chosen is a recursion because either group or its sub groups have similar nature.

# Time Complexity
O(n)
In O(n), n means the number of groups(sub groups) and 
files included in the group input. All users and groups are visited just once, so the run time is 
linear.

# Space Complexity
In the worst case, the space complexity is also O(n).
Imagine a tree that the root has one branch. Every branch in this tree has only one child.
All non-leave nodes are folder and the only leave node is a file.
In this case, the function will create a n-1 level stack.