import java.util.Arrays;

    // This Java program performs basic array operations on an array of integers.
    // It calculates the sum of the array and prints it.
    // It sorts the array in ascending order and prints the sorted array.
    // It finds the maximum value in the array and prints it.

public class ArrayOperations {
    public static void main(String[] args) {
        int[] numbers = {5, 3, 7, 1, 8, 2, 4};

        // Find the sum of the array
        int sum = Arrays.stream(numbers).sum();
        System.out.println("Sum of the array: " + sum);

        // Sort the array in ascending order
        Arrays.sort(numbers);
        System.out.println("Sorted array (ascending): " + Arrays.toString(numbers));

        // Find the maximum value in the array
        int max = Arrays.stream(numbers).max().getAsInt();
        System.out.println("Maximum value: " + max);
    }
}
