impl Solution {
    pub fn insert_greatest_common_divisors(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        fn gcd(mut a: i32, mut b: i32) -> i32 {
            while b != 0 {
                let temp = b;
                b = a % b;
                a = temp;
            }
            a
        }

        let mut dummy = Some(Box::new(ListNode::new(0)));
        let mut prev = &mut dummy;

        let mut current = head;
        while let Some(mut curr_node) = current.take() {
            if let Some(next_node) = curr_node.next.take() {
                let gcd_val = gcd(curr_node.val, next_node.val);
                let new_node = Some(Box::new(ListNode::new(gcd_val)));

                prev.as_mut().unwrap().next = Some(curr_node);
                prev.as_mut().unwrap().next.as_mut().unwrap().next = new_node;
                prev = &mut prev.as_mut().unwrap().next.as_mut().unwrap().next;
                current = Some(next_node);
            } else {
                prev.as_mut().unwrap().next = Some(curr_node);
                break;
            }
        }

        dummy.unwrap().next
    }
}
