// 2635. Apply Transform Over Each Element in Array

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */

var map = function (arr, fn) {
  const len = arr.length;
  const mappedArr = new Array(len);

  for (let i = 0; i < len; i++) {
    mappedArr[i] = fn(arr[i], i);
  }
  return mappedArr;
};
