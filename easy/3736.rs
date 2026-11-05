// 3736. Minimum Moves to Equal Array Elements III
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/
// Biweekly Contest 169

impl Solution {
    pub fn min_moves(nums: Vec<i32>) -> i32 {
        let max_num = *nums.iter().max().unwrap();

        nums.iter().map(|num| max_num - *num).sum()
    }
}
