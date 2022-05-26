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

