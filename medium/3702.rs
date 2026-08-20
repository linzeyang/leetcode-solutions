// 3702. Longest Subsequence With Non-Zero Bitwise XOR
// https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/
// Weekly Contest 514

impl Solution {
    pub fn longest_subsequence(nums: Vec<i32>) -> i32 {
        let all_xor: i32 = nums.iter().fold(0, |acc, num| acc ^ num);

        if all_xor != 0 {
            return nums.len() as i32;
        }

        if nums.iter().all(|num| num == &0) {
            return 0;
        }

        nums.len() as i32 - 1
    }
}
