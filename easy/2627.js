// 2627. Debounce

/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function (fn, t) {
  let timeoutId;

  return function (...args) {
    // Clear the previous timeout if it exists
    if (timeoutId) {
      clearTimeout(timeoutId);
    }

    // Set a new timeout to execute the function after t milliseconds
    timeoutId = setTimeout(() => {
      fn(...args);
    }, t);
  };
};
