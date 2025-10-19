# Mini Library Management System

This Python project implements a basic Library Management System with the following features:
- Add, update, and delete books (using ISBN as key).
- Register, update, and delete members.
- Search books by title or author.
- Borrow and return books (each member can borrow up to 3 books).
- Unit tests and a demo script are provided.

## Files

- `operations.py` : Core functions and data structures for books and members.
- `demo.py`       : Example script demonstrating key functionality.
- `tests.py`      : Unit tests (using `unittest`) for all operations.
- `UML.png`       : UML class diagram illustrating the system design.
- `Rationale.docx`: Design rationale explaining data structure choices.
- `README.md`     : Instructions (this file).

## Requirements

- Python 3.x (no external libraries required).

## How to Run

1. **Run the Demo**: Execute `python3 demo.py` to see a demonstration of adding books/members, borrowing, returning, etc.
2. **Run Tests**: Execute `python3 -m unittest tests.py` to run the unit tests. All tests should pass.
3. **Using the Functions**: You can also import the functions from `operations.py` into your own scripts.

Make sure all files are in the same directory when running the demo or tests. The system uses simple in-memory data structures, so it resets on each run.

