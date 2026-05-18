  HOW TO RUN THE PROJECT

  Step 1: Make sure Python is installed
  → Open your terminal 
  → Type this and press Enter:
      python --version
  → If you see an error, download Python from: https://python.org

  Step 2: Go to the folder where todo.py is saved
  → Type this in terminal:
      cd path/to/todo_app

  Step 3: Run the app!
  → Type this and press Enter:
      python todo.py
  → The app will start and show you a menu!

  Step 4: Use the app
  → Press 1 to see your tasks
  → Press 2 to add a task
  → Press 3 to delete a task
  → Press 4 to quit

  WHAT EACH PART OF THE CODE DOES

  tasks = []
  → This is a Python LIST. 
  → When you add tasks, they go inside this list.
  → Example after adding tasks: ["Buy milk", "Study Python", "Call mom"]

  def show_menu():
  → 'def' means we are DEFINING a function 
  → This function just prints the menu options on screen

  def view_tasks():
  → Shows all tasks using a FOR LOOP
  → enumerate() adds numbers like 1, 2, 3 to each task

  def add_task():
  → Uses input() to ask the user to type a task
  → Uses .append() to add that task to our list

  def delete_task():
  → Shows tasks, asks which number to remove
  → Uses .pop() to remove the task from the list
  → Uses try/except to handle if user types letters instead of numbers

  while True:
  → Keeps the app running in a loop
  → Only stops when user picks option 4 (quit) which triggers 'break'

  if __name__ == "__main__":
  → This means: "only run this if I directly run this file"
  → It's a Python best practice even beginners should know

  PYTHON CONCEPTS USED

  1. LISTS
     → tasks = []
     → Store multiple items in one variable
     → Add with .append(), remove with .pop()

  2. FUNCTIONS
     → def function_name():
     → Reusable blocks of code
     → Keeps code organized and clean

  3. if / elif / else
     → Make decisions based on what user types

  4. while loop
     → Repeat code until a condition is met
     → 'break' exits the loop

  5. for loop + enumerate()
     → Go through each item in a list
     → enumerate() gives position number + value

  6. input()
     → Get text typed by the user

  7. print()
     → Display text on the screen

  8. int() and str()
     → Convert between text and numbers

  9. try / except
     → Handle errors gracefully without crashing

  10. len()
      → Count how many items are in a list

  11. .strip()
      → Remove extra spaces from user input

  12. if __name__ == "__main__"
      → Python best practice for running scripts


