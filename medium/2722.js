// 2722. Join Two Arrays by ID

/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function (arr1, arr2) {
  let map = new Map();

  for (let i = 0; i < arr1.length; i++) {
    map.set(arr1[i].id, arr1[i]);
  }

  for (let i = 0; i < arr2.length; i++) {
    if (map.has(arr2[i].id)) {
      map.set(arr2[i].id, { ...map.get(arr2[i].id), ...arr2[i] });
    } else {
      map.set(arr2[i].id, arr2[i]);
    }
  }

  let out = Array.from(map.values());

  return out.sort((a, b) => a.id - b.id);
};
