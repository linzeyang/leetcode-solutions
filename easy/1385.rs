// 1385. Find the Distance Value Between Two Arrays
// https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
// Biweekly Contest 22

impl Solution {
    pub fn find_the_distance_value(arr1: Vec<i32>, arr2: Vec<i32>, d: i32) -> i32 {
        let mut arr2 = arr2.clone();
        arr2.sort_unstable();

        let mut out = 0;

        for num1 in arr1 {
            let idx = arr2.partition_point(|&x| x < num1);

            if idx == 0 {
                if arr2[0] - num1 > d {
                    out += 1;
                }
            } else if idx == arr2.len() {
                if num1 - arr2[arr2.len() - 1] > d {
                    out += 1;
                }
            } else if num1 - arr2[idx - 1] > d && arr2[idx] - num1 > d {
                out += 1;
            }
        }

        out
    }
}
