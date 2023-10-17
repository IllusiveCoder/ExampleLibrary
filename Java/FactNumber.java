import java.util.Scanner;

    // This Java program calculates the factorial of a number.
    // It takes user input for the number.
    // It calculates the factorial using a for loop.
    // The result is then printed as the factorial of the given number.

public class FactorialCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int number = scanner.nextInt();
        scanner.close();

        // Calculate factorial
        long factorial = 1;
        for (int i = 1; i <= number; i++) {
            factorial *= i;
        }

        // Output
        System.out.println("The factorial of " + number + " is: " + factorial);
    }
}
