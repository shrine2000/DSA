/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func insertGreatestCommonDivisors(head *ListNode) *ListNode {
    // Helper function to calculate GCD
    gcd := func(a, b int) int {
        for b != 0 {
            a, b = b, a%b
        }
        return a
    }

    dummy := &ListNode{Val: 0, Next: head}
    prev := dummy

    current := head
    for current != nil && current.Next != nil {
        currNode := current
        nextNode := current.Next

        gcdVal := gcd(currNode.Val, nextNode.Val)
        newNode := &ListNode{Val: gcdVal}

        prev.Next = currNode
        currNode.Next = newNode
        newNode.Next = nextNode

        prev = newNode
        current = nextNode
    }

    return dummy.Next
}
