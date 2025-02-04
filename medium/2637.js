// 2637. Promise Time Limit

/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function (fn, t) {
  return async function (...args) {
    // Create a Promise that gets rejected after t ms
    const timeoutPromise = new Promise((_, reject) => {
      setTimeout(() => {
        reject("Time Limit Exceeded");
      }, t);
    });

    // Use Promise.race to race between fn and timeoutPromise
    try {
      const result = await Promise.race([fn(...args), timeoutPromise]);
      return result;
    } catch (err) {
      throw err;
    }
  };
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */
