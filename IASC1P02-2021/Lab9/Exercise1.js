
var start = new Date();
var startMilli = start.getTime();

console.log(startMilli);

function stopTime() {
  var end = new Date();
  var endMilli = end.getTime();

  var difMilli = endMilli - startMilli;

  var difSecond = difMilli/1000;

  alert("The number of seconds is" + difSecond);
}