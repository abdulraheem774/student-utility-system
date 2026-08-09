# Student Utility System

A menu driven command line application built in Python that combines multiple
small utilities into one tool - built as a practice project to strengthen
Python fundamentals (functions, conditionals, error handling, and standard
library modules).

## Features

- **Student Result** — Enter marks for 4 subjects, get total, percentage,
  and grade automatically. Option to save the result to a file.
- **Student ID Generator** — Enter a name, get a random 4-digit student ID.
- **Random Motivation** — Displays a random motivational message.
- **Platform Information** — Shows system, OS version, platform, and
  processor details.
- **Math Tools** — Square root, power, factorial, ceiling, and floor,
  all in a sub-menu.

## Concepts Used

- Functions and code organization
- Conditional statements (if / elif / else)
- Loops (menu keeps running until the user exits)
- Error handling (try / except) for invalid input
- File handling (saving results to a text file)
- Python standard library: `math`, `random`, `platform`
- Formatted output using f-strings

## How to Run

```bash
git clone https://github.com/abdulraheem774/student-utility-system.git
cd student-utility-system
python3 main.py
```

Requires Python 3.6+. No external libraries needed - everything used is
part of the Python standard library.

## Example

```
===== Student Utility System =====
1. Student Result
2. Student ID
3. Random Motivation
4. Platform Information
5. Math Tools
6. Exit
Enter your choice:
```

## Future Improvements

- Add a GUI version (Tkinter)
- Store results in a CSV/JSON file instead of plain text
- Add unit tests for grade calculation and math tools

## Author

Abdul Raheem Shah
