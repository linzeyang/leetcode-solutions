// 2625. Flatten Deeply Nested Array

/**
 * @param {any[]} arr
 * @param {number} depth
 * @return {any[]}
 */

var flat = function (arr, n) {
    if (n <= 0) return arr.slice(0);

    // recursively flatten sub-arrays with depth-1
    return arr.reduce((acc, val) => {
        // if element is an array and depth is less than n, push it as-is
        if (Array.isArray(val) && n > 0) {
            acc.push(...flat(val, n - 1));
        } else {
            // otherwise, push the element
            acc.push(val);
        }
        return acc;
    }, []);
};
