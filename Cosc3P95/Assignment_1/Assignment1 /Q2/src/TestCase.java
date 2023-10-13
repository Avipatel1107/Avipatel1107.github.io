import java.util.Arrays;
import java.util.Random;

public class TestCase {
    public static int[] createRandomArray(int length, int minValue, int maxValue) {
        int[] arr = new int[length];
        Random r = new Random();
        for (int i = 0; i < length; i++) {
            arr[i] = r.nextInt((maxValue - minValue) + 1) + minValue;
        }
        return arr;
    }

    public static boolean runTestCase(int[] arr, int[] reference) {
        int[] copy = Arrays.copyOf(arr, arr.length); // Create a copy of the original array
        Sort.bubbleSort(arr); // Use the provided sorting algorithm

        boolean success = Arrays.equals(arr, reference);

        System.out.println("Input Array: " + Arrays.toString(copy));
        System.out.println("Output Array: " + Arrays.toString(arr));
        System.out.println("Expected Output: " + Arrays.toString(reference));
        System.out.println("Test Result: " + (success ? "PASSED" : "FAILED"));
        System.out.println();

        return success;
    }


    public static void main(String[] args) {
        int numTests = 10;  // Number of random test cases
        int minLength = 5;  // Minimum length of the array
        int maxLength = 20; // Maximum length of the array
        int minValue = 1;   // Minimum integer value
        int maxValue = 100; // Maximum integer value

        for (int test = 0; test < numTests; test++) {
            int arrayLength = minLength + (int)(Math.random() * ((maxLength - minLength) + 1));
            int[] randomArray = createRandomArray(arrayLength, minValue, maxValue);
            int[] referenceArray = Arrays.copyOf(randomArray, randomArray.length);
            Arrays.sort(referenceArray); // Sort with Java's built-in sorting for reference



            runTestCase(randomArray, referenceArray);
        }
    }


}
