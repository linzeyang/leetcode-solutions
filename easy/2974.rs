// 2974. Minimum Number Game

impl Solution {
    pub fn number_game(nums: Vec<i32>) -> Vec<i32> {
        let mut sorted_nums = nums.clone();
        sorted_nums.sort_unstable();

        let mut out = Vec::with_capacity(sorted_nums.len());

        for idx in (0..sorted_nums.len()).step_by(2) {
            out.push(sorted_nums[idx + 1]);
            out.push(sorted_nums[idx]);
        }

        out
    }
}
