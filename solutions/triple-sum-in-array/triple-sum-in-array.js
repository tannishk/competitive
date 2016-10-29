'use strict';

var array = [1,8,5,7];
var sum, numbers, firstNumber, secondNumber, thirdNumber, arrayHaveTheNumbers = false;
var tripleSum = [];
alert("With the array: " + array + " wich 3 numbers you want to sum?");
numbers = prompt ( array + " Numbers separated by comas, only will sum the first 3 numbers: " );
tripleSum = numbers.split(',');
if(tripleSum.length === 3) {
  arrayHaveTheNumbers =
  array.indexOf(parseInt(tripleSum[0])) > -1 &&
  array.indexOf(parseInt(tripleSum[1])) > -1 &&
  array.indexOf(parseInt(tripleSum[2])) > -1 ? true : false;
  if(arrayHaveTheNumbers) {
    firstNumber = array.indexOf(parseInt(tripleSum[0]));
    secondNumber = array.indexOf(parseInt(tripleSum[1]));
    thirdNumber = array.indexOf(parseInt(tripleSum[2]));
    sum = array[firstNumber] + array[secondNumber] + array[thirddNumber];
    alert("The sum of the 3 numbers is: " + sum);
  } else {
    alert("The numbers not match");
  }
} else {
  alert("This program only sum 3 numbers of an array separated by comas");
}
