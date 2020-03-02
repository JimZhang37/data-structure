# Why I choose this data structure
I use `python list` to store the list of sub folders inside a folder.
If it is a file, I will check its suffix.

If it is a folder, I will use the recursive function to find if it contains the file with 
the suffix.

# Time Complexity
I used a for loop for a list has O(n).
I also used the recursion by calling the function itself.
I think the time complexity is still O(n) because all folders or sub folders are visited only once.

# Space Complexity
O(n)
n means the number of files and folders in the path.
In the worst case, the recursive function will create a deep stack which will consume
lots of resources.
All folders and files will be 