# start with a node class, the building block of a linked list. 
class Node(object):
    # constructor method that initializes a node object. The constructor takes two parameters, 'd' and 'n'
    # 'd' represents the data being stored
    # 'n' represents the next node in the linked list
    def __init__(self, d, n = None):
        self.data = d 
        self.next_node = n
    # getter & setter functions for "data" and "next" node 
    def get_next(self):
        return self.next_node
    def set_next(self, n):
        self.next_node = n
    def get_data(self):
        return self.data
    def set_data(self, d):
        self.data = d

# Linked List class 
class LinkedList(object):
    # set up variables for the root and the size
    def __init__(self, r = None):
        self.root = r
        self.size = 0
    # get function for the size
    def get_size(self):
        return self.size
    # add function
    def add(self, d):
        # take a piece of data (d) and create a new node
        new_node = Node(d, self.root)
        self.root = new_node
        # increment size by 1 
        self.size += 1
    # remove function 
    def remove(self, d):
        # current node that we're looking at
        this_node = self.root
        prev_node = None
        # use a while loop to iterate through the list
        while this_node: 
            # iterate through the list to find the node we're looking for 
            if this_node.get_data() == d: 
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else: 
                    self.root = this_node
                self.size -= 1
                # return True to indicate we've successfully returned the data 
                return True
            else: 
                # advance the pointer from the previous node to the next node
                prev_node = this_node
                # advance the pointer from this node to next node
                this_node = this_node.get_next()
        # if we exit out of our while loop without finding the data we're looking for, return False to indicate that we did not find the data
        return False 
    # find function 
    def find(self, d):
        # start at the root node
        this_node = self.root
        while this_node:
            # look at each node to compare the data against the data we're looking for. When we find it, return the data (d).
            if this_node.get_data() == d: 
                return d
            # if we dont find it, advance to the next node
            else: 
                this_node = this_node.get_next()
        # if we exit the loop without finding the data, return None
        return None

# to use the list, we can instantiate a new list 
myList = LinkedList()
# example operations
myList.add(5)
myList.add(8)
myList.add(12)
myList.remove(8)
print(myList.remove(12))
print(myList.find(5))
