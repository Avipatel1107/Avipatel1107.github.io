//Sets the initial colours of the three elements on page load
document.getElementById("blue").onclick=mix;
document.getElementById("green").onclick=mix;
document.getElementById("red").onclick=mix;

//A function to change colours of elements when called
function mix(){
	
	var first = "#00BB00";
	var second = "#BB9320";
	var third = "#AB00FF";
	
	document.body.style.color="first";
	document.body.style.color="second";
	document.body.style.color="third";
	return false;
}

