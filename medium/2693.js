// 2693. Call Function with Custom Context

/**
 * @param {Object} context
 * @param {Array} args
 * @return {null|boolean|number|string|Array|Object}
 */
Function.prototype.callPolyfill = function (context, ...args) {
  if (typeof this !== "function") {
    throw new Error("Not a function");
  }

  const fn = this;
  const obj = context || globalThis;
  const fnName = Symbol();
  obj[fnName] = fn;
  const result = obj[fnName](...args);
  delete obj[fnName];
  return result;
};

/**
 * function increment() { this.count++; return this.count; }
 * increment.callPolyfill({count: 1}); // 2
 */
