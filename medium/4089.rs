// 4089. Count Subarrays With Loose Bounds
// https://leetcode.com/problems/count-subarrays-with-loose-bounds/
// Biweekly Contest 194

impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, min_k: i32, max_k: i32) -> i64 {
        let mut out: i64 = 0;
        let mut current: i64 = 0;

        for &num in &nums {
            if min_k <= num && num <= max_k {
                current += 1;
            } else if current > 0 {
                out += current * (current + 1) / 2;
                current = 0;
            }
        }

        if current > 0 {
            out += current * (current + 1) / 2;
        }

        out
    }
}
