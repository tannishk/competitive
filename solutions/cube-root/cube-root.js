// This solution is based on the Newton-Raphson Method

var cubeRoot = function (number) {
  var guess = 1;
  var accuracy = 0.0001; // The accuracy of your response
  var improve = function (y) {
    return ((number / Math.pow(y, 2)) + (2 * y)) / 3;
  };
  var loop = function () {
    if (!(Math.abs(number - Math.pow(guess, 3)) < accuracy)) {
      guess = improve(guess);
      return loop();
    } else {
      return guess;
    };
  };
  return loop();
};
