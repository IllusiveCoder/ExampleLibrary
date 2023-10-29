
# Description: This program helps users manage their tasks. 
# Users can add, view, and complete tasks. The program stores 
# tasks in an array.

class TaskListManager
    def initialize
      @tasks = []
    end
  
    def add_task(task)
      # Add a new task to the list
      @tasks << task
    end
  
    def view_tasks
      # View the list of tasks
      puts "Task List:"
      @tasks.each_with_index do |task, index|
        puts "#{index + 1}. #{task}"
      end
    end
  
    def complete_task(index)
      # Mark a task as complete
      if index >= 0 && index < @tasks.length
        puts "Completed: #{@tasks[index]}"
        @tasks.delete_at(index)
      else
        puts "Invalid task index."
      end
    end
  end
  
  # Usage example
  task_manager = TaskListManager.new
  task_manager.add_task("Buy groceries")
  task_manager.add_task("Finish report")
  task_manager.view_tasks
  task_manager.complete_task(0)
  task_manager.view_tasks
  