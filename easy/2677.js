// 2677. Chunk Array

/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function (arr, size) {
  const out = [];

  let sub = [];

  for (let i = 0; i < arr.length; i++) {
    if (sub.length < size) {
      sub.push(arr[i]);
    } else {
      out.push(sub);
      sub = [arr[i]];
    }
  }

  if (sub.length > 0) {
    out.push(sub);
  }

  return out;
};
