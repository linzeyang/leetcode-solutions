// 4044. Count Good Cyclic Rotations
// https://leetcode.com/problems/count-good-cyclic-rotations/
// Weekly Contest 518

impl Solution {
    pub fn count_good_rotations(nums: Vec<i32>) -> i32 {
        let length: usize = nums.len();

        let mut diff: i64 = nums
            .iter()
            .take(length / 2)
            .map(|&num| i64::from(num))
            .sum::<i64>()
            - nums
                .iter()
                .skip(length / 2)
                .map(|&num| i64::from(num))
                .sum::<i64>();

        let mut out: i32 = if diff > 0 { 1 } else { 0 };

        for idx in 0..length - 1 {
            let a: i64 = i64::from(nums[idx]);
            let b: i64 = i64::from(nums[(idx + length / 2) % length]);

            diff -= (a - b) * 2;

            out += if diff > 0 { 1 } else { 0 };
        }

        out
    }
}
