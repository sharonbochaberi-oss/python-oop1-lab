# Python OOP Bookstore Lab

This lab demonstrates core **Object-Oriented Programming (OOP)** concepts in Python by modeling a simple bookstore with two main objects: `Book` and `Coffee`. The goal is to practice creating classes, properties, and methods, while implementing input validation and simple behaviors.


## Features

### **Book**
- Attributes:
  - `title` – the name of the book
  - `page_count` – number of pages (must be an integer)
- Methods:
  - `turn_page()` – simulates turning a page

### **Coffee**
- Attributes:
  - `size` – Small, Medium, or Large (validated)
  - `price` – price of the coffee
- Methods:
  - `tip()` – prints a tip message and increases price by 1


## Installation

1. **Clone the repository**:
```bash
git clone <https://github.com/sharonbochaberi-oss/python-oop1-lab.git>
cd python-oop1-lab


## set up environment
pipenv install      # Install dependencies
pipenv shell        # Enter virtual environment


## run tests to verify functionality
pytest -x


## screenshot
All tests passing for Book and Coffee classes.

![Tests Passing](Screenshot(22).png)  

