var age = prompt("What is your age")

var startDate = new Date();
var year = startDate.getFullYear();
var birthYear = year - age;

document.write(birthYear);