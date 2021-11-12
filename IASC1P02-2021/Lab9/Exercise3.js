function addition (){

var a = document.getElementById("num1").value;
var b = document.getElementById("num2").value;
var output = parseFloat (a) + parseFloat (b);
if (!Number.isInteger(output)) {
  output = "OUTPUT";
} else {
  output = parseFloat(a) + parseFloat(b);
};
document.getElementById("out").innerHTML = output;

};