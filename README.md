# Python Lab Project

## Part A - Project Setup Using the CLI

### Command Explanation

I first used `cd ~` to move to my home directory and `mkdir python_lab` to create a new project directory. I then used `cd python_lab` to enter the project directory. The `mkdir src tests docs` command created three subdirectories for source code, testing, and documentation. I used `touch` to create the three empty Python files inside the `src` directory. Finally, I used output redirection with `echo "My Python Lab Project" > docs/README.md` to write the required text into the documentation file without opening an editor. I used a recursive directory listing to verify that all folders and files were correctly created and nested.

### Why Separate src, tests, and docs?

Separating a project into `src`, `tests`, and `docs` is good practice because it keeps different types of project files organized. The `src` directory contains the application's source code, the `tests` directory is reserved for testing the code, and the `docs` directory contains documentation. Even for a small project, this structure makes the project easier to understand, maintain, test, and expand as it becomes larger.


