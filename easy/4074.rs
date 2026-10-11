// 4074. Maximum Product Pair With Target Sum
// https://leetcode.com/problems/maximum-product-pair-with-target-sum/
// Biweekly Contest 193

use std::collections::HashMap;

impl Solution {
    pub fn max_product_pair(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut out: Vec<i32> = vec![-1, -1];

        let mut max_product: i32 = -10001;

        let mut register: HashMap<i32, i32> = HashMap::new();

        for (idx, num) in nums.iter().enumerate() {
            if num * 2 == target {
                continue;
            }

            let diff = target - num;

            if !register.contains_key(&diff) {
                register.insert(*num, idx as i32);
            } else if num * diff > max_product {
                max_product = num * diff;

                if *num > diff {
                    out = vec![idx as i32, *register.get(&diff).unwrap()];
                } else {
                    out = vec![*register.get(&diff).unwrap(), idx as i32];
                }
            }
        }

        out
    }
}
