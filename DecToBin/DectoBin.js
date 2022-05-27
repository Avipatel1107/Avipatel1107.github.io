// The visible unit converter
let visible = "binary";
// Get the divs 
const binToDecimal = document.getElementById('binToDecimal');
const decimalToBin = document.getElementById('decimalToBin');
const visibleDiv = document.getElementById('visibleDiv');
// Convert to decimal function
function convertToDecimal(){
    // Get the number from input
    // Store in in array
    // Reverse the array
    const arr_numberBinnary = document.getElementById('binary').value.split('');
    const reverse_arr = arr_numberBinnary.reverse(); 

    // Get the spans and reset the error span
    const err_span = document.getElementsByClassName('err')[0];
    err_span.textContent = '';
    const decimal_res_span = document.getElementById('decimal_res');
    
    // Intialize the output variable
    let output = 0;
    // For Loop 
    for (number in reverse_arr){
        // Convert strings from array to integers
        const int = parseInt(reverse_arr[number],10);
        // Check if the format is invalid
        if(int != 0 && int != 1){
            // Print the error
            err_span.textContent = "Invalid format! Use only 1 and 0!";
            decimal_res_span.textContent = '';
            return; // Stop the function
        }
        // Calculate the output
        output +=  int*Math.pow(2,number);
    }

    // Display the result if there is no error
        decimal_res_span.textContent = output;
}

// Convert to binary function
function convertToBinary(){
    // Get the number in decimal
    const numberDecimal = document.getElementById('decimal').value;

    // Get the spans and reset the error span
    const err_span = document.getElementsByClassName('err')[0];
    err_span.textContent = '';
    const binary_res_span = document.getElementById('binary_res');

    // Create a new regex and check if the regex is valid
    const regex = new RegExp("^[0-9]*$");
    const regex_test = regex.test(numberDecimal);
    // If the regex is invalid print the the error
    if(!regex_test){
        err_span.textContent = "Invalid format! Please use only digits!";
        binary_res_span.textContent = ''; 
        return;
    }

    // Intialize output variable, quotien and remainder
    let output = '';
    let quotient = numberDecimal;
    let remainder;
    // Check if the q is higher than zero
    while(quotient > 0){
        // Check if the remainder is divisible by 2
        remainder = quotient % 2;
        // Divide the q
        quotient = parseInt(quotient/2);
        // Add the values to the output
        if(remainder == 1){
            output = (1)+output;
        } else {
            output = (0)+output;
        }
    }

    // Show the result
    binary_res_span.textContent = output;
}

// Change the convert units
function changeDiv(){
    if(visible =="binary"){
        visibleDiv.innerHTML  = decimalToBin.innerHTML;
        visible = "decimal";
    } else {
        visibleDiv.innerHTML  = binToDecimal.innerHTML;
        visible = "binary";
    }
}
changeDiv();