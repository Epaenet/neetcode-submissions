class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        old_to_new = {}

        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        curr = head

        while curr:
            copy = old_to_new[curr]

            if curr.next:
                copy.next = old_to_new[curr.next]

            if curr.random:
                copy.random = old_to_new[curr.random]

            curr = curr.next
        return old_to_new[head]