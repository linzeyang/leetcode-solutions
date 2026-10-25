// 4088. Difference Between Peaks and Valleys
// https://leetcode.com/problems/difference-between-peaks-and-valleys/
// Biweekly Contest 194

impl Solution {
    pub fn peak_valley_difference(nums: Vec<i32>) -> i32 {
        let mut peak_sum = 0;
        let mut valley_sum = 0;

        for idx in 1..nums.len() - 1 {
            let num = nums[idx];

            if num > nums[idx - 1] && num > nums[idx + 1] {
                peak_sum += num;
            } else if num < nums[idx - 1] && num < nums[idx + 1] {
                valley_sum += num;
            }
        }

        peak_sum - valley_sum
    }
}
