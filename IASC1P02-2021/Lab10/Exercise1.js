function addingMech(){
  var firstValue = Number(document.getElementById('value1').value);
  var secondValue = Number(document.getElementById('value2').value);
  document.getElementById("outputs").innerHTML =  firstValue + secondValue;
}

function subtractionMech(){
  var firstValue = Number(document.getElementById('value1').value);
  var secondValue = Number(document.getElementById('value2').value);
  document.getElementById("outputs").innerHTML = firstValue - secondValue;
}

function multiplicationMech(){
  var firstValue = Number(document.getElementById('value1').value);
  var secondValue = Number(document.getElementById('value2').value);
  document.getElementById("outputs").innerHTML = firstValue * secondValue;
}

function divisionMech(){
  var firstValue = Number(document.getElementById('value1').value);
  var secondValue = Number(document.getElementById('value2').value);
  document.getElementById("outputs").innerHTML = firstValue / secondValue;
}