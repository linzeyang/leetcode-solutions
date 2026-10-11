// 4078. Three Fibonacci Sum
// https://leetcode.com/problems/three-fibonacci-sum/
// Weekly Contest 523

impl Solution {
    pub fn three_fibonacci_sum(n: i32) -> bool {
        if n & 1 == 1 {
            return false;
        }

        let target = n >> 1;

        let mut a = 0;
        let mut b = 1;

        while a + b < target {
            let temp = b;
            b = a + b;
            a = temp;

            if a + b > target {
                return false;
            }

            if a + b == target {
                return true;
            }
        }

        true
    }
}
