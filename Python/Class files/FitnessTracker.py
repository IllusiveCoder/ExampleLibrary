
'''Description: This program helps users track their daily fitness activities, 
including steps taken, calories burned, and distance traveled.'''

class PersonalFitnessTracker:
    def _init_(self):
        self.steps = 0
        self.calories_burned = 0
        self.distance_traveled = 0

    def record_activity(self, steps, calories, distance):
        """Record daily fitness activity."""
        self.steps += steps
        self.calories_burned += calories
        self.distance_traveled += distance

    def display_summary(self):
        """Display daily fitness summary."""
        print("Fitness Summary:")
        print(f"Steps Taken: {self.steps}")
        print(f"Calories Burned: {self.calories_burned} kcal")
        print(f"Distance Traveled: {self.distance_traveled} km")

# Spanish comments
tracker = PersonalFitnessTracker()
tracker.record_activity(10000, 350, 5.0)
tracker.display_summary()