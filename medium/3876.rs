// 3876. Construct Uniform Parity Array II
// https://leetcode.com/problems/construct-uniform-parity-array-ii/
// Weekly Contest 494

impl Solution {
    pub fn uniform_array(nums1: Vec<i32>) -> bool {
        let mut min_odd: i32 = std::i32::MAX;
        let mut min_even: i32 = std::i32::MAX;

        for num in nums1 {
            if num & 1 == 0 {
                if min_even > num {
                    min_even = num;
                }
            } else {
                if min_odd > num {
                    min_odd = num;
                }
            }
        }

        (min_odd == std::i32::MAX) || (min_even == std::i32::MAX) || (min_even > min_odd)
    }
}
