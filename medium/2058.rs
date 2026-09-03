// 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points
// https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/
// Weekly Contest 265

// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode {
            next: None,
            val
        }
    }
}

impl Solution {
    pub fn nodes_between_critical_points(head: Option<Box<ListNode>>) -> Vec<i32> {
        let mut out: Vec<i32> = vec![-1, -1];

        if head.is_none() || head.as_ref().unwrap().next.is_none() {
            return out;
        }

        let mut first_idx: i32 = -1;
        let mut last_idx: i32 = -1;
        let mut current_idx: i32 = 1;
        let mut prev_val: i32 = head.as_ref().unwrap().val;

        let mut min_dis: i32 = i32::MAX;

        let mut current: Option<&Box<ListNode>> = head.as_ref().unwrap().next.as_ref();

        while let Some(node) = current {
            if node.next.is_none() {
                break;
            }

            if (node.val > prev_val && node.val > node.next.as_ref().unwrap().val) || (
                node.val < prev_val && node.val < node.next.as_ref().unwrap().val
            ) {
                if first_idx == -1 {
                    first_idx = current_idx;
                } else {
                    min_dis = min_dis.min(current_idx - last_idx);
                }

                last_idx = current_idx;
            }

            prev_val = node.val;
            current_idx += 1;
            current = node.next.as_ref();
        }

        if last_idx > first_idx && first_idx > -1 {
            out[0] = min_dis;
            out[1] = last_idx - first_idx;
        }

        out
    }
}
