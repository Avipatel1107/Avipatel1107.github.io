function adding(){
  var firstValue = Number(document.getElementById('value1').value);
  var secondValue = Number(document.getElementById('value2').value);
  document.getElementById("outputs").innerHTML =  firstValue + secondValue;
}

function subtraction(){
  var firstValue = Number(document.getElementById('value1').value);
  var secondValue = Number(document.getElementById('value2').value);
  document.getElementById("outputs").innerHTML = firstValue - secondValue;
}

function multiplication(){
  var firstValue = Number(document.getElementById('value1').value);
  var secondValue = Number(document.getElementById('value2').value);
  document.getElementById("outputs").innerHTML = firstValue * secondValue;
}

function division(){
  var firstValue = Number(document.getElementById('value1').value);
  var secondValue = Number(document.getElementById('value2').value);
  document.getElementById("outputs").innerHTML = firstValue / secondValue;
}