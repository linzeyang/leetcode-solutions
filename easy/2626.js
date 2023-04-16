// 2626. Array Reduce Transformation

/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */

var reduce = function(nums, fn, init) {
    if (nums.length === 0) {
        return init;
    }

    var out = init;

    for (let i = 0; i < nums.length; i++) {
        out = fn(out, nums[i]);
    }

    return out;
};
