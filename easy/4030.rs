// 4030. Check ASCII Palindromic
// https://leetcode.com/problems/check-ascii-palindromic/
// Weekly Contest 516

impl Solution {
    pub fn is_palindromic(s: String) -> bool {
        let binary: String = s.chars().map(|c| format!("{:08b}", c as u8)).collect();

        binary.chars().eq(binary.chars().rev())
    }
}
