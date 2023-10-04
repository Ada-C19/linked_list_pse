class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

# Solution from class
# Time complexity: O(m+n)--> O(n)
# Space complexity: O(n) --> due to the set
def intersection_node(head_a, head_b):
    """
    Given the heads of two singly linked-lists `head_a` and `head_b`, 
    return the node at which the two lists intersect.
  
    Parameters:
    head_a (Node): head node of list A
    head_b (Node): head node of list B
  
    Returns:
    Node: the node at which list A and list B intersect, 
    or None if they do not intersect.
    """

    # create a set for storing all nodes of the first linked list
    nodes = set()
    # traverse the first linked list with a loop and put each node in the set
    while head_a:
        nodes.add(head_a)
        head_a = head_a.next
    # then loop through second linked list and check if each node is in the set
    while head_b:
        if head_b in nodes: 
            return head_b
        head_b = head_b.next
    
    # if node is in the set, then return that node 
    # if there is no intersection, return None
    return None

# Time complexity: O(m*n) --> worst case scenario m and n are same size --> O(n*n) --> O(n^2)
# Time complexity: O(1) 
# Visual shown in class: https://lh4.googleusercontent.com/zDRIcBToS6sC_ZdFN6p5vdel95-kPq736LHU4ldIHQWNtURwNxVC_4iRxbS9RE6q06pb-KWujO7ISc7yiJhLBg1_Bl7tGUxeKrbiwdBJHEFO-QeSPckvJrFSF1ctEtdo6Wpw4Yzy
def intersection_node(head_a, head_b):
    while head_b:
        node_to_search = head_a
        while node_to_search:
            if node_to_search == head_b:
                return head_b
            node_to_search = node_to_search.next
        head_b = head_b.next
    return None

# Solution shown in Learn: spend some time debugging with the debugger or pen/paper to help you see how the pointers work
# Time complexity: O(A + B) where A is the size of list A and B is the size of list B. The loop will traverse through the lists at most twice.
# Space complexity: O(1) as the added space needed does not scale with the input data (two additional pointers)
def intersection_node(head_a, head_b):
    # assign l1 and l2 to point to the heads of list A and list B
    l1, l2 = head_a, head_b
    # while l1 and l2 do not reference the same node or None
    while l1 != l2:
        # once we've traversed through an entire list, we will set the pointer for the smaller list to the beginning of the other list
        # on the next iteration of the lists:
        #   if there is NO intersection, both pointers will reach None at the same time.
        #   if there is an intersection, both pointers will reach the intersecting Node at the same time.

        # set l1 to be l1.next if l1 is not None, otherwise set l1 to be the head of list B 
        l1 = l1.next if l1 else head_b
        # likewise, set l2 to be l2.next if l2 is not None, otherwise set l2 to be the head of list A
        l2 = l2.next if l2 else head_a
    return l1