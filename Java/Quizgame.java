import java.util.Scanner;

public class QuizGame {
    private int score;

    // Sample questions and options
    private String[] questions = {
        "What is the capital of France?",
        "Which planet is known as the 'Red Planet'?",
        "Who painted the Mona Lisa?"
    };

    private String[][] options = {
        {"A) London", "B) Paris", "C) Rome", "D) Berlin"},
        {"A) Jupiter", "B) Mars", "C) Venus", "D) Saturn"},
        {"A) Leonardo da Vinci", "B) Pablo Picasso", "C) Vincent van Gogh", "D) Michelangelo"}
    };

    private int[] answers = {2, 2, 1}; // Index of the correct option (1-based) for each question

    public void startGame() {
        Scanner scanner = new Scanner(System.in);

        for (int i = 0; i < questions.length; i++) {
            System.out.println(questions[i]);
            for (String option : options[i]) {
                System.out.println(option);
            }

            System.out.print("Enter your answer (1-4): ");
            int userAnswer = scanner.nextInt();

            if (userAnswer == answers[i]) {
                System.out.println("Correct!");
                score++;
            } else {
                System.out.println("Wrong!");
            }

            System.out.println();
        }

        System.out.println("Quiz finished. Your score: " + score);
    }

    public static void main(String[] args) {
        QuizGame quizGame = new QuizGame();
        quizGame.startGame();
    }
}
