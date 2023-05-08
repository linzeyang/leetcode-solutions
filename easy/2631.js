// 2631. Group By

/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function (fn) {
  let out = {};

  for (let ele of this) {
    let key = fn(ele);

    if (!out.hasOwnProperty(key)) {
      out[key] = [ele];
    } else {
      out[key].push(ele);
    }
  }

  return out;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */
