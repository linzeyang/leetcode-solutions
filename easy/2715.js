// 2715. Timeout Cancellation

/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function (fn, args, t) {
  const executeFn = () => {
    fn(...args);
  };

  const timeoutId = setTimeout(executeFn, t);

  const cancelFn = () => {
    clearTimeout(timeoutId);
  };

  return cancelFn;
};
