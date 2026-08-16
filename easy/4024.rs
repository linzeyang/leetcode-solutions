// 4024. Nearest Available Drone
// https://leetcode.com/problems/nearest-available-drone/
// Weekly Contest 515

impl Solution {
    pub fn nearest_drone(drones: Vec<Vec<i32>>, target: Vec<i32>) -> i32 {
        let mut out: i32 = -1;
        let mut min_distance: i32 = i32::MAX;

        for (idx, drone) in drones.iter().enumerate() {
            let distance: i32 = (drone[0] - target[0]).abs() + (drone[1] - target[1]).abs();

            if distance <= drone[2] && distance < min_distance {
                min_distance = distance;
                out = idx as i32;
            }
        }

        out
    }
}
