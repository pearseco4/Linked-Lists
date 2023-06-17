# given a linked list of N nodes, reverse the list

# define the ListNode class
class ListNode: 
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # the method reverseList takes a parameter named "head" of type "Optional[ListNode]" and returns "Optional[ListNode]"
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head 
        # this while loop will iterate until curr becomes None, indicate all the nodes have been processed
        while curr:
            # the current node's next node is temporarily stored in the temp variable 
            temp = curr.next
            # the current node's next pointer is updated to point to the previous node, reversing the direction of the link 
            curr.next = prev 
            # the prev variable is now updated to point to the current node 
            prev = curr 
            # the curr variable is updated to the temp variable, which holds the reference to the orignial next node
            curr = temp
        # once the loop finishes, the entire list has been reversed. The method returns prev, which now points to the new head of the reversed list
        return prev

# create an instance of the Solution class
solution = Solution()

# create linked list for testing
# example: 1 -> 2 -> 3 -> 4 -> 5

head = ListNode(1)
head.next = ListNode(2)

