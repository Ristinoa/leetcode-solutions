/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */

var argumentsLength = function(...args) {
    return args.length;
};

out = argumentsLength(1, 2, 3)
console.log(out);

/**
 * argumentsLength(1, 2, 3); // 3
 */