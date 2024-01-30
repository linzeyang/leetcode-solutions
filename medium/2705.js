//

/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function (obj) {
  if (Array.isArray(obj)) {
    return obj
      .filter(
        (item) => Boolean(item) || (Array.isArray(item) && item.length > 0),
      )
      .map(compactObject);
  } else if (typeof obj === "object" && obj !== null) {
    return Object.fromEntries(
      Object.entries(obj)
        .map(([key, value]) => {
          const simplifiedValue = compactObject(value);
          if (
            simplifiedValue &&
            (typeof simplifiedValue !== "object" ||
              Object.keys(simplifiedValue).length > 0)
          ) {
            return [key, simplifiedValue];
          }
        })
        .filter((entry) => entry),
    );
  }
  return obj;
};
