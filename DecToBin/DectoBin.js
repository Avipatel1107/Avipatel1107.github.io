const binaryNumber = document.getElementById("binary");
const decimalNumber = document.getElementById("decimal");
const convertButton = document.getElementById("btn");
const refreshButton = document.getElementById("refresh");

let bins;

binaryNumber.addEventListener("input", e => {
  bins = e.target.value;
});

const binToDec = () => {
  for (let i = 0; i < bins.length; i++) {
    if (bins.charAt(i) > 1) {
      alert("please insert a binary number");
    }
  }
  const decimal = parseInt(bins, 2);
  decimalNumber.innerHTML = decimal;
};

const refreshNumbers = () => {
  location.reload();
};

refreshButton.addEventListener("click", refreshNumbers);

convertButton.addEventListener("click", binToDec);
