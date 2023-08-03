class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(lst1, lst2):
    preHead = ListNode(-1)
    prev = preHead
    while lst1 and lst2:
        if lst1.val <= lst2.val:
            prev.next = lst1
            lst1 = lst1.next
        else:
            prev.next = lst2
            lst2 = lst2.next
        prev = prev.next
    prev.next = lst1 if lst1 is not None else lst2
    return preHead.next


def create_linked_list(values):
    dummy = ListNode(-1)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def print_linked_list(head):
    current = head
    while current is not None:
        print(current.val, end=' -> ')
        current = current.next
    print("None")


class Solution(object):
    def deleteDuplicates(self, head):
        current_node = head
        while current_node is not None and current_node.next is not None:
            if current_node.val == current_node.next.val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
        return head

    def remove(self, head, val):
        dummy_head = ListNode(-1)
        dummy_head.next = head
        prev_node, curr_node = dummy_head, head
        while curr_node:
            if curr_node.val == val:
                prev_node.next = curr_node.next
            else:
                prev_node = curr_node
            curr_node = curr_node.next
        return dummy_head.next

    def reverseList(self, head):
        prev_node = None
        curr_node = head

        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        return prev_node

    def isPalindrome(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True

    def middleNode(self, head):
        fast = head
        while fast and fast.next:
            head = head.next
            fast = fast.next.next

        return head


l1 = create_linked_list([1, 2, 3])
l2 = create_linked_list([1, 1, 4, 5])
new_lst = Solution().deleteDuplicates(l2)
print(print_linked_list(mergeTwoLists(l1, l2)))
print(print_linked_list(new_lst))