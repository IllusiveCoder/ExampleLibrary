import java.util.ArrayList;
import java.util.Scanner;

// This Java program is a simple console-based to-do list application. 
// It uses an ArrayList to store tasks and provides options to add, 
// remove, and view tasks. The program continues to run until the user 
// chooses to exit (option 3). It demonstrates the use of collections 
// and basic user interaction in Java.

public class ToDoListApp {
    public static void main(String[] args) {
        ArrayList<String> tasks = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);
        
        while (true) {
            System.out.println("To-Do List:");
            for (int i = 0; i < tasks.size(); i++) {
                System.out.println((i + 1) + ". " + tasks.get(i));
            }
            System.out.println("Menu:");
            System.out.println("1. Add Task");
            System.out.println("2. Remove Task");
            System.out.println("3. Exit");
            
            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline
            
            switch (choice) {
                case 1:
                    System.out.print("Enter a task: ");
                    String task = scanner.nextLine();
                    tasks.add(task);
                    break;
                case 2:
                    System.out.print("Enter the task number to remove: ");
                    int taskNumber = scanner.nextInt();
                    scanner.nextLine(); // Consume newline
                    if (taskNumber > 0 && taskNumber <= tasks.size()) {
                        tasks.remove(taskNumber - 1);
                    }
                    break;
                case 3:
                    scanner.close();
                    System.exit(0);
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }
}
