// 2629. Function Composition

/**
 * @param {Function[]} functions
 * @return {Function}
 */

var compose = function (functions) {
  var fun = function (num) {
    for (let i = 0; i < functions.length; i++) {
      num = functions[functions.length - 1 - i](num);
    }

    return num;
  };

  return fun;
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */
