import java.util.function.Function;

public class DeltaDebugging {

    public static String deltaDebugging(String inputStr, Function<String, Boolean> testFunction, int n) {
        // Split the input into n sub-inputs
        String[] subInputs = new String[n];
        for (int i = 0; i < n; i++) {
            StringBuilder subInput = new StringBuilder();
            for (int j = i; j < inputStr.length(); j += n) {
                subInput.append(inputStr.charAt(j));
            }
            subInputs[i] = subInput.toString();
        }

        // Binary search approach
        int low = 0;
        int high = n - 1;

        while (low < high) {
            // Calculate mid-points
            int mid1 = low + (high - low) / 2;
            int mid2 = high - (high - low) / 2;

            // Test the mid-points
            String combinedInput1 = String.join("", subInputs).substring(0, subInputs[mid1].length())
                    + String.join("", subInputs).substring(subInputs[mid2].length());
            String combinedInput2 = String.join("", subInputs).substring(0, subInputs[mid2].length())
                    + String.join("", subInputs).substring(subInputs[mid1].length());

            boolean result1 = testFunction.apply(combinedInput1);
            boolean result2 = testFunction.apply(combinedInput2);


            if (result1) {
                high = mid2 - 1;
            } else {
                low = mid1 + 1;
            }
        }

        // Return the minimized input
        StringBuilder minimizedInput = new StringBuilder();
        for (int i = 0; i < low; i++) {
            minimizedInput.append(subInputs[i]);
        }
        for (int i = high + 1; i < n; i++) {
            minimizedInput.append(subInputs[i]);
        }

        return minimizedInput.toString();
    }

    public static void main(String[] args) {
        // Define a function to test the processString function
        Function<String, Boolean> testProcessString = inputStr -> {
            try {
                processString(inputStr);
                return true;  // The function executed successfully
            } catch (Exception e) {
                return false;  // The function raised an exception
            }
        };

        // Test the deltaDebugging function for the provided input values
        String input1 = "abcdefG1";
        String minimizedInput1 = deltaDebugging(input1, testProcessString, 2);
        System.out.println("Minimized input 1: " + minimizedInput1);

        String input2 = "CCDDEExy";
        String minimizedInput2 = deltaDebugging(input2, testProcessString, 2);
        System.out.println("Minimized input 2: " + minimizedInput2);

        String input3 = "1234567b";
        String minimizedInput3 = deltaDebugging(input3, testProcessString, 2);
        System.out.println("Minimized input 3: " + minimizedInput3);

        String input4 = "8665";
        String minimizedInput4 = deltaDebugging(input4, testProcessString, 2);
        System.out.println("Minimized input 4: " + minimizedInput4);

        String input5 = "Avi43453Gds";
        String minimizedInput5 = deltaDebugging(input5, testProcessString, 2);
        System.out.println("Minimized input 5: " + minimizedInput5);
    }

    public static String processString(String inputStr) {
        StringBuilder outputStr = new StringBuilder();
        for (char c : inputStr.toCharArray()) {
            if (Character.isUpperCase(c)) {
                outputStr.append(Character.toLowerCase(c));
            } else if (Character.isDigit(c)) {
                outputStr.append(c);
            } else {
                outputStr.append(Character.toUpperCase(c));
            }
        }
        return outputStr.toString();
    }
}
