// 4031. Find All Numbers Disappeared in an Array II
// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array-ii/
// Weekly Contest 516

impl Solution {
    pub fn find_disappeared_numbers(nums: Vec<i32>, lower: i32, upper: i32) -> Vec<Vec<i32>> {
        let mut nums: Vec<i32> = nums.into_iter().collect();
        nums.sort_unstable();
        nums.dedup();

        let mut out: Vec<Vec<i32>> = Vec::new();

        let mut current: i32 = lower;

        for num in nums {
            if num < lower || num > upper {
                continue;
            }

            if num == current {
                current += 1;
            } else {
                out.push(vec![current, num - 1]);
                current = num + 1;
            }
        }

        if current <= upper {
            out.push(vec![current, upper]);
        }

        out
    }
}
