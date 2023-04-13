// 2634. Filter Elements from Array

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */

var filter = function (arr, fn) {
    const len = arr.length;
    const newArray = [];

    for (let i = 0; i < len; i++) {
        if (fn(arr[i], i)) {
            newArray.push(arr[i]);
        }
    }
    return newArray;
};
