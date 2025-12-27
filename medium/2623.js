// 2623. Memoize

/**
 * @param {Function} fn
 */
function memoize(fn) {
  const storage = {};

  return function (...args) {
    const key = JSON.stringify(args);

    if (key in storage) {
      return storage[key];
    } else {
      const result = fn(...args);
      storage[key] = result;
      return result;
    }
  };
}

/**
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1
 */
