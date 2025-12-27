// 2649. Nested Array Generator

/**
 * @param {Array} arr
 * @return {Generator}
 */
var inorderTraversal = function* (arr) {
  for (const ele of arr) {
    if (typeof ele === "number") {
      yield ele;
    } else {
      yield* inorderTraversal(ele);
    }
  }
};

/**
 * const gen = inorderTraversal([1, [2, 3]]);
 * gen.next().value; // 1
 * gen.next().value; // 2
 * gen.next().value; // 3
 */
