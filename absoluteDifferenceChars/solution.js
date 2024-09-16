/**
 * @param {string} s
 * @return {number}
 */
var scoreOfString = function(s) {
    if (s.length < 2){
        return 0;
    }
    var score = 0;
    for (let i = 0; i < s.length - 1; i++) {
        score += Math.abs(s.charCodeAt(i) - s.charCodeAt(i + 1));
    }

    return score;
};

var input = "hello";
var score = scoreOfString(input);

console.log(score); /* Outputs 13 */