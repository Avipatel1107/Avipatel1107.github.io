//Sets the initial colours of the three elements on page load
document.getElementById("blue").onclick=mix;
document.getElementById("green").onclick=mix;
document.getElementById("red").onclick=mix;

//A function to change colours of elements when called
function mix(){
	
	document.getElementById("blue").style.color='#00BB00';
	document.getElementById("green").style.color='#BB9320';
	document.getElementById("red").style.color='#AB00FF';

	}

