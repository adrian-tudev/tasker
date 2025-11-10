# Tasker
A minimalistic command-line task manager written in python and typer.

## Features
- Add, list and archive tasks
- Priority levels: **[LOW]**, **[MEDIUM]**, **[HIGH]**
- Tags to organize tasks
- Persistent storage through SQLite (`.todo.db`)

## Usage
```bash
$ tasker add "eat ice cream 😁" --prio HIGH
Added task "eat ice cream 😁" with prio [HIGH🟥]

$ tasker archive 2
Woho! finished task 2 👌

$ tasker ls
1: [HIGH🟥] eat ice cream
2: [LOW 🟩] buy sum groceries
3: [MEDIUM 🟨] study 😒
```

## Installation
### Using pip:
```bash
pip install python-tasker
```
