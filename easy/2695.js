// 2695. Array Wrapper

/**
 * @param {number[]} nums
 */
var ArrayWrapper = function (nums) {
  this.nums = nums;
  let sum = 0;
  nums.forEach((num) => {
    sum += num;
  });
  this.sum = sum;
};

ArrayWrapper.prototype.valueOf = function () {
  return this.sum;
};

ArrayWrapper.prototype.toString = function () {
  const str = "[" + this.nums.map((num) => `${num}`).join(",") + "]";
  return str;
};

/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */
