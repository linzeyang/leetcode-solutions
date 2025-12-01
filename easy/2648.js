// 2648. Generate Fibonacci Sequence

/**
 * @return {Generator<number>}
 */
var fibGenerator = function* () {
  yield 0;
  yield 1;

  let a = 0;
  let b = 1;

  while (true) {
    yield a + b;
    const temp = a;
    a = b;
    b = temp + a;
  }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */
