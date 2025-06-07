class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_segment(start_node, end_node):
            prev = None
            curr = start_node
            while curr != end_node:
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
            return prev

        if not head or k == 1:
            return head

        dummy_head = ListNode(0)
        dummy_head.next = head

        prev_group_end = dummy_head

        while True:
            k_nodes_start = prev_group_end.next
            k_nodes_end = k_nodes_start
            count = 0

            while count < k and k_nodes_end:
                k_nodes_end = k_nodes_end.next
                count += 1

            if count < k:
                break

            next_segment_start = k_nodes_end

            new_group_head = reverse_segment(k_nodes_start, k_nodes_end)

            prev_group_end.next = new_group_head

            k_nodes_start.next = next_segment_start
            prev_group_end = k_nodes_start

        return dummy_head.next
