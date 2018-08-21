# Given the root node to a singly linked list, reverse the last 5 nodes in the list.

class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def reverse_linked_list(root, n=0):
    if root is None:
        print("root not provided")
        return
    if n == 0:
        return
    counter = 0


    runner = root
    nth_from_last = root
    previous = root

    # set the runner n nodes ahead
    while counter < n:
        if runner is None:
            print("not enough nodes in list")
            return
        runner = runner.next
        counter += 1

    # increment runner and nth_from_last until runner hits the end
    while runner:
        runner = runner.next
        previous = nth_from_last
        nth_from_last = nth_from_last.next

    reverse_full = False
    if previous == nth_from_last:
        reverse_full = True

    temp_node = None
    for i in range(n):
        next = nth_from_last.next
        nth_from_last.next = temp_node
        temp_node = nth_from_last
        nth_from_last = next

    if reverse_full:
        root = temp_node
    else:
        previous.next = temp_node
    print("x")
    return root

import unittest

class Test(unittest.TestCase):
    def test_kth_to_last(self):

        head = Node(1,Node(2,Node(3,Node(4))))
        head = reverse_linked_list(head, 3)

        temp_node = head
        for n in range(4):
            print(temp_node.data)
            temp_node = temp_node.next

        temp_node = head
        self.assertEqual(1, temp_node.data)
        temp_node = temp_node.next
        self.assertEqual(4, temp_node.data)
        temp_node = temp_node.next
        self.assertEqual(3, temp_node.data)
        temp_node = temp_node.next
        self.assertEqual(2, temp_node.data)

        head = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7)))))))
        head = reverse_linked_list(head, 7)

        temp_node = head

        for n in range(7):
            print(temp_node.data)
            temp_node = temp_node.next

        temp_node = head

        self.assertEqual(7, temp_node.data)
        temp_node = temp_node.next
        self.assertEqual(6, temp_node.data)
        temp_node = temp_node.next
        self.assertEqual(5, temp_node.data)
        temp_node = temp_node.next
        self.assertEqual(4, temp_node.data)
        temp_node = temp_node.next
        self.assertEqual(3, temp_node.data)
        temp_node = temp_node.next
        self.assertEqual(2, temp_node.data)
        temp_node = temp_node.next
        self.assertEqual(1, temp_node.data)



if __name__ == "__main__":
    unittest.main()
