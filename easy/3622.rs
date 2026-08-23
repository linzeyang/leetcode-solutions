// 3622. Check Divisibility by Digit Sum and Product
// https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/
// Weekly Contest 459

impl Solution {
    pub fn check_divisibility(n: i32) -> bool {
        let digits: Vec<i32> = n.to_string().chars().map(|c| c.to_digit(10).unwrap() as i32).collect();
        let sum: i32 = digits.iter().sum();
        let prod: i32 = digits.iter().product();
        n % (sum + prod) == 0
    }
}
