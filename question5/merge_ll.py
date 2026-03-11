class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#
def merge_LL(list1, list2):
    # create a temp node to act as the starting point
    temp = LinkedList(-1)
    current = temp # current is 

    # compare heads until one list is exhausted
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1  # add list1 head to current
            list1 = list1.next    # increment list1 head
        else:
            current.next = list2  # add list2 head to current
            list2 = list2.next    # increment list2 head
        
        current = current.next    # move the tail of merged list

    # 3. If one list still has nodes, attach the remainder
    # (Since they are sorted, we just link the rest of the existing list)
    #current.next = list1 if list1 else list2
    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    # return the head (which is the node after temp)
    return temp.next

# LL print wrapper
def print_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "")
        node = node.next
    print()


def main():
    print("--------------------")
    # use example input lists
    # call "recursively" to add all values to LL quickly
    l1 = LinkedList(1, LinkedList(2, LinkedList(4)))
    print("list1:")
    print_list(l1)
    l2 = LinkedList(1, LinkedList(3, LinkedList(4)))
    print("list2:")
    print_list(l2)

    merged_list = merge_LL(l1, l2)

    print("Lists merged, printing result...")
    print_list(merged_list)

    print("--------------------")

if __name__ == "__main__":
    main()