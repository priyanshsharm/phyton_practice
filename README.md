# phyton_practice
my phyton learning problem

# Student Record Manager

A simple menu-based Python program to manage student records (name and marks) from the terminal. Records are saved to a text file, so they are still there the next time you run the program.

Built as a practice project while learning Python (functions, classes, lists, loops and file handling).

## Features

- Add a student with name and marks (marks must be between 0 and 100)
- View all students with their grade
- Search a student by name (not case-sensitive)
- Update a student's marks
- Delete a student
- Save students to a file (`students.txt`) and load them automatically when the program starts
- Show the topper (highest marks)
- Show the class average
- List only the students who passed

## Grading

| Marks | Grade |
|-------|-------|
| 90 and above | grade a |
| 75 to 89 | grade b |
| 40 to 74 | grade c |
| below 40 | grade d |

A student passes with 40 marks or more.

## How to run

1. Install Python 3.
2. Download `student_manager.py`.
3. Run it from the terminal:

```
python student_manager.py
```

## Menu

```
1. Add student
2. View all students
3. search_student
4. update_student
5. delete_student
6. save_student
7. show_topper
8. show_average
9. show_passed
10. exit
```

Note: choose **6 (save)** before exiting, otherwise new changes are not written to the file.

## How it works

- Each student is an object of a `Student` class with `name` and `marks`, plus `check()` (pass or fail) and `grade()` methods.
- All students are kept in a list while the program runs.
- Saving writes one student per line as `name,marks` in `students.txt`. Loading reads the file line by line, splits each line at the comma and rebuilds the students.
- If `students.txt` does not exist yet, the program starts with an empty list.

## Concepts practiced

- Functions and a `while True` menu loop
- Classes and objects
- Lists and `for` loops
- Searching, updating and deleting items in a list
- File reading and writing
- Basic error handling with `try` and `except`

## Possible improvements

- Save automatically on exit
- Show a number in front of each student and the total count
- Sort students by marks
- Handle names that contain a comma
