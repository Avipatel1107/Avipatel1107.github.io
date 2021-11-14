function math(type) {

var num1 = parseInt(document.getElementById("num1").value);
var num2 = parseInt(document.getElementById("num2").value);

if(type == "add") {
	document.getElementById("output").innerHTML = num1 + num2;
} else if (type == "subtract") {
	document.getElementById("output").innerHTML = num1 - num2;
} else if (type == "multiply") {
	document.getElementById("output").innerHTML = num1 * num2;
} else if (type == "divide") {
	document.getElementById("output").innerHTML = num1 / num2;
}

}