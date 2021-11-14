
function Name(){
  document.getElementsByName("onLoad").innerHTML = onLoad;
}

var elementOne = document.getElementById("firstNumber");
var elementTwo = document.getElementById("secondNumber");

function sum() {
  var calculation = Number(elementOne.value) + Number(elementTwo.value);
  document.getElementById("Answer").innerHTML = calculation;
}

function difference() {
  var calculation = Number(elementOne.value) - Number(elementTwo.value);
  document.getElementById("Answer").innerHTML = calculation;
}

function product() {
  var calculation = Number(elementOne.value) * Number(elementTwo.value);
  document.getElementById("Answer").innerHTML = calculation;
}

function quotient() {
  var calculation = Number(elementOne.value) / Number(elementTwo.value);
  document.getElementById("Answer").innerHTML = calculation;
}
