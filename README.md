# Course Schedule Manager
This Course Schedule Manager is a simple Python script that helps users manage their course schedules. It detects collisions in course schedules and displays the schedule in both the console and a graphical user interface (GUI) using the tkinter library.

# Features
+ Add courses with details like course code, name, classroom, instructor, day, and start and end times
+ Check for collisions in the course schedule
+ Print course schedule in the console
+ Display the course schedule in a GUI using the tkinter library
# Dependencies
+ Python 3.x
+ tkinter (included in the Python standard library)
# Usage
1. Clone the repository or download the Python script.
2. Open the script in your favorite Python IDE or text editor.
3. Add courses by creating instances of the Course class and calling the schedule.add_course() method with each course instance.
4. Run the script to print the course schedule in the console and display it in the GUI.
# Example
```
schedule = Schedule()
schedule.add_course(
  Course("EEF 211E", "Basics of Electrical Circuits", "EEB 5102",
         "Metin Hüner", "Monday", 9, 12))
schedule.add_course(
  Course("MAT 202E", "Numerical Methods", "EEB 5304", "Emine Ayaz", "Monday",
         13, 16))
# ... add more courses as needed

schedule.print_schedule()
root = Tk()
schedule.print_table(root)
root.mainloop()
```
# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
