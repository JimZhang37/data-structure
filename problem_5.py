import hashlib
import datetime
import pytz

class Block:
    def __init__(self, num, timestamp, data, previous_block):
        self.id = num
        self.timestamp = timestamp
        self.data = data
        if not previous_block:
            self.previous_hash = None
            self.next = None
        else:
            self.previous_hash = previous_block.hash
            self.next = previous_block
        self.hash = self.calc_hash()


    def calc_hash(self):
        sha = hashlib.sha256()
        string = str(self.timestamp) + str(self.data) + str(self.previous_hash)
        hash_str = string.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self):
        return f'''The id of this block is: {self.id}
It's created at {self.timestamp}
It's content is {self.data}
It's hash is {self.hash}
'''


class BlockChain:
    def __init__(self):
        self.head = None
        self.tail = None
        self.id = 0

    def append(self, value):

        currentTime = datetime.datetime.now(pytz.utc)

        if self.head == None:
            self.head = Block(self.id, currentTime, value, None)
            self.tail = self.head
            self.id += 1
        else:
            new_node = Block(self.id, currentTime, value, self.head)
            new_node.next = self.tail
            self.tail = new_node
            self.id += 1

    def __repr__(self):
        if self.tail is not None:
            s =  f'''
    total number of block is: {self.id}
    the first: {self.tail}
    the second: {self.tail.next}

    
    '''
        if self.tail == None:
            s = f'''
This block chain is empty now. please add its first block!
'''
        return s


list = BlockChain()
list.append(1)
list.append(2)
list.append(3)
print(list) # expect to see block 2, block 1 and block 0


list.append(4)
list.append(5)
print(list) # expect to see block 4, block 3 and block 2

list0 = BlockChain()
print(list0) # expect to see blank block list

list1 = BlockChain()
list1.append(1)
print(list1) # expect to see block 1

list2 = BlockChain()
list2.append()
print(list2)