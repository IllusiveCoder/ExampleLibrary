import time

'''Enhance the previous quiz game to include a countdown 
timer for each question. Users have a limited time to answer 
each question before it moves on to the next one. The program 
will keep track of the time remaining for each question and 
calculate the final score based on correct answers and time taken.'''

class QuizGameWithTimer(QuizGame):
    def __init__(self):
        super().__init__()
        self.timer_duration = 10  # Time per question in seconds

    def start_game(self):
        for question in self.questions:
            print(question)
            for option in self.questions[question]:
                print(option)
            start_time = time.time()
            user_answer = input("Your answer: ")
            end_time = time.time()

            if user_answer.lower() == self.correct_answers[question]:
                elapsed_time = end_time - start_time
                if elapsed_time <= self.timer_duration:
                    self.score += 1
                    print("Correct! You answered within the time limit.")
                else:
                    print("Correct, but you exceeded the time limit.")
            else:
                print("Wrong!")

# Usage example
quiz_with_timer = QuizGameWithTimer()
quiz_with_timer.add_question("What is the capital of France?", ["A) London", "B) Paris", "C) Rome", "D) Berlin"], "b")
quiz_with_timer.add_question("Which planet is known as the 'Red Planet'?", ["A) Jupiter", "B) Mars", "C) Venus", "D) Saturn"], "b")
quiz_with_timer.start_game()
print("Your final score:", quiz_with_timer.score)
