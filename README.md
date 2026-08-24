# Python Lab Project

## Part A - Project Setup Using the CLI

### Command Explanation

I first used `cd ~` to move to my home directory and `mkdir python_lab` to create a new project directory. I then used `cd python_lab` to enter the project directory. The `mkdir src tests docs` command created three subdirectories for source code, testing, and documentation. I used `touch` to create the three empty Python files inside the `src` directory. Finally, I used output redirection with `echo "My Python Lab Project" > docs/README.md` to write the required text into the documentation file without opening an editor. I used a recursive directory listing to verify that all folders and files were correctly created and nested.

### Why Separate src, tests, and docs?

Separating a project into `src`, `tests`, and `docs` is good practice because it keeps different types of project files organized. The `src` directory contains the application's source code, the `tests` directory is reserved for testing the code, and the `docs` directory contains documentation. Even for a small project, this structure makes the project easier to understand, maintain, test, and expand as it becomes larger.



## Part B - Git Initialization and First Commit

### What is `.gitignore`?

The `.gitignore` file tells Git which files and directories should not be tracked or included in commits. In this project, `__pycache__/` ignores Python cache folders, `*.pyc` ignores compiled Python bytecode files, and `.env` ignores environment files that may contain private configuration or sensitive information. These files are unnecessary for sharing the source code and should generally not be committed to a public repository.

### Why the File Patterns Matter

The `__pycache__/` and `*.pyc` patterns prevent automatically generated Python files from being added to the repository. These files are created by Python when programs are run and can be regenerated when needed. The `.env` pattern is important because environment files can contain passwords, API keys, or other private configuration values that should not be published to GitHub.

### What Does Commit History Show?

Git commit history records the changes made to a project over time. Each commit provides information such as the commit identifier, the author, the date, and the commit message. This allows developers to understand how a project developed, review previous changes, and return to an earlier version when necessary.

### First Commit

The first commit was:

`51ecd1b Add initial Python lab project structure`

This commit records the initial Python lab project structure, including the source files, documentation, `.gitignore`, and project screenshot.

## Part C - Writing and Committing Python Code

### Python Code

The `utils.py` file contains three reusable functions. The `square(n)` function returns the square of a number. The `is_even(n)` function checks whether a number is even by using the remainder operator `%`. The `celsius_to_fahrenheit(c)` function converts a Celsius value to Fahrenheit using the formula `(C * 9 / 5) + 32`.

The `main.py` file imports these functions from `utils.py` and uses them in the main program. It asks the user to enter a number, displays the square of the number, determines whether it is even or odd, and converts the number from Celsius to Fahrenheit.

### How Python Imports Connect the Files

Python's import system allows one Python file to use functions defined in another Python file. In `main.py`, the statement `from utils import square, is_even, celsius_to_fahrenheit` imports the three functions from `utils.py`. Because both files are in the same `src` directory, Python can locate `utils.py` when `main.py` is executed. This keeps the program organized by separating reusable functions from the main program logic.

### Testing

The program was tested using at least three different input values. Each test confirmed that the program correctly calculated the square, determined whether the number was even or odd, and converted the Celsius value to Fahrenheit.

Example test results:

```text
Test 1
Input: 5
Square: 25
Even: False
Fahrenheit: 41.0

Test 2
Input: 10
Square: 100
Even: True
Fahrenheit: 50.0

Test 3
Input: 25
Square: 625
Even: False
Fahrenheit: 77.0
```

### Source Code: `src/utils.py`

```python
def square(n):
    return n ** 2


def is_even(n):
    return n % 2 == 0


def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32
```

### Source Code: `src/main.py`

```python
from utils import square, is_even, celsius_to_fahrenheit


number = float(input("Enter a number: "))

print("Square:", square(number))

if is_even(number):
    print("Even: True")
else:
    print("Even: False")

print("Fahrenheit:", celsius_to_fahrenheit(number))
```

