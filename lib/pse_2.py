class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

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
    #[4, 1, 8, 4, 5] -- A
    #[5, 6, 1, 8, 4, 5] -- B 

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