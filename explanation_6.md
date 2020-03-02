# Why I choose this data structure
- union function


In union function, the first step is to connect 2 lists together by assigning last item in the first list a new next value.
This new next value is the head of the second list. This operation has time complexity of O(n) which n is the length of the first list.

In the second step, I use python's set in this project so I can have constant search time and handle duplicates.
I use a for loop to go through all items to see if it has appeared before. If it is the first appearance, I put it in a set.
If it is not the first appearance, I would delete it.

I adopted double linked list so I have O(1) time complexity to remove an item from the list.

- intersection

In the first design, my time complexity is O(n**2) as I have 2 nested `for loop` that can compare every item in list 1 with every item in list 2.
To improve its performance, in the inner for loop, I will delete the item in the second list when I found it has the same value of a item from another list.

Another improvement is I put the shorter list in the outer loop and longer list in the inner loop.


# Time Complexity

The time complexity is O(n) for union and O(n * log(n)) in the intersection function. 
In the worst case, if list 1 and list 2 have nothing in common, the time complexity for
intersection will be O(n**2) because the inner loop's list will never be deceasing.

# Space 
I use deep copy to copy inputs to a new space, so that the original lists will not be tampered. I use inplace algorithm in both union
and intersection. So the space complexity for both function is O(n)