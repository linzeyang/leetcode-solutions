// 3498. Reverse Degree of a String
// https://leetcode.com/problems/reverse-degree-of-a-string
// Biweekly Contest 153

impl Solution {
    pub fn reverse_degree(s: String) -> i32 {
        // use iterator
        s.chars()
            .enumerate()
            .map(|(idx, char)| (26 - char as u8 + b'a') as i32 * (idx as i32 + 1))
            .sum::<i32>()
    }
}
