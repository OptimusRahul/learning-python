# Python Learning Journey ☕

A comprehensive, hands-on Python learning repository covering fundamental to advanced concepts through practical examples and projects. This repository uses a unique "chai" (tea) theme throughout many examples to make learning more engaging and memorable.

## 📚 Project Overview

This repository is structured as a progressive learning path, starting from Python basics and advancing to modern Python features like async programming and Pydantic. Each section contains practical, runnable examples that demonstrate core concepts in action.

## 🗂️ Repository Structure

### 00. Basics (`00_basics/`)
- Introduction to Python
- Environment setup verification
- Running your first Python script

### 01. Virtual Environments (`01_virtual/`)
- Setting up isolated Python environments
- Managing dependencies with `requirements.txt`
- Working with Flask and requests libraries

### 02. Data Types (`02_datatypes/`)
**11 chapters covering:**
- Strings, numbers, and boolean values
- Lists, tuples, and dictionaries
- Sets and frozensets
- Type conversion and manipulation
- Data structure operations

### 03. Conditionals (`03_conditionals/`)
**Practical projects:**
- `chai_price_calculator.py` - Price calculation with if-else logic
- `fees_waiver_system.py` - Conditional eligibility checking
- `mini_story_1.py` - Interactive storytelling
- `railway_app.py` - Transportation system logic
- `smart_thermostat_system.py` - IoT simulation
- `snack_suggestion.py` - Recommendation system

### 04. Loops (`04_loops/`)
**10 exercises covering:**
- For and while loops
- Loop control (`break`, `continue`, `pass`)
- For-else construct
- Walrus operator (`:=`)
- Iterating over dictionaries
- Queue and batch processing examples

### 05. Functions (`05_functions/`)
**12 topics including:**
- Function definition and calling
- Parameters and arguments
- Return values
- Scope (local, nonlocal, global)
- Built-in functions
- Code organization and reusability
- Function complexity management

### 06. Chai Business (`06_chai_business/`)
**Complete project demonstrating:**
- Package structure with `__init__.py`
- Module organization
- Recipe management system
- Utility functions
- Practical application of Python modules

### 07. Comprehensions (`07_comprehensions/`)
**4 types covered:**
- List comprehensions
- Set comprehensions
- Dictionary comprehensions
- Generator expressions

### 08. Generators & Decorators (`08_generators_decorators/`)
**Advanced topics:**
- Generator basics and benefits
- Infinite generators
- Sending values to generators
- Generator lifecycle management

### 09. Decorators (`09_decorators/`)
**Practical examples:**
- Basic decorator syntax
- Logger decorator
- Authorization decorator
- Function wrapping with `functools.wraps`

### 10. Object-Oriented Programming (`10_oops/`)
**11 comprehensive topics:**
- Classes and objects
- Namespaces and attributes
- The `self` parameter
- `__init__` constructor
- Inheritance and composition
- Method Resolution Order (MRO)
- Static methods and class methods
- Property decorators

### 11. Exceptions (`11_exceptions/`)
**8 lessons on error handling:**
- Try-except blocks
- Complex exception handling
- Multiple exception types
- Custom exceptions
- File handling with exceptions
- Real-world error scenarios

### 12. Threading & Concurrency (`12_threads_concurrency/`)
**12 examples covering:**
- Threading basics
- Multiprocessing
- Global Interpreter Lock (GIL) understanding
- Thread synchronization and locks
- Process queues and shared values
- Concurrent downloads
- Thread-safe operations

### 13. Async Python (`13_async_python/`)
**9 advanced topics:**
- Async/await syntax
- Asyncio fundamentals
- Combining threads with async
- Process-based async operations
- Background workers
- Daemon vs non-daemon threads
- Race conditions

### 14. Pydantic (`14_pydantic/`)
**Modern Python data validation:**
- Basic models
- Field validation
- Nested models
- Self-referencing models
- Computed properties
- Advanced validation techniques
- Serialization and deserialization

## 🚀 Getting Started

### Prerequisites

- Python 3.7+ installed on your system
- Basic understanding of programming concepts (helpful but not required)
- A code editor (VS Code, PyCharm, etc.)

### Installation

1. **Clone or download this repository:**
   ```bash
   cd /Users/ghost/Developer/python
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r 01_virtual/requirements.txt
   ```

### Running Examples

Navigate to any directory and run the Python files:

```bash
# Example: Run the first basics script
python 00_basics/testpython.py

# Example: Test a chai calculator
python 03_conditionals/chai_price_calculator.py

# Example: Explore decorators
python 09_decorators/01_basics.py

# Example: Try async programming
python 13_async_python/01_async_one.py
```

## 🎯 Learning Path

### For Beginners
1. Start with `00_basics/` and `02_datatypes/`
2. Move to `03_conditionals/` and `04_loops/`
3. Master `05_functions/`
4. Practice with `06_chai_business/` project

### For Intermediate Learners
1. Dive into `07_comprehensions/`
2. Explore `08_generators_decorators/` and `09_decorators/`
3. Master `10_oops/` concepts
4. Handle errors with `11_exceptions/`

### For Advanced Learners
1. Concurrent programming with `12_threads_concurrency/`
2. Modern async patterns in `13_async_python/`
3. Data validation with `14_pydantic/`

## 🌟 Key Features

- **Progressive Learning**: Topics build upon each other logically
- **Practical Examples**: Real-world scenarios instead of abstract concepts
- **Themed Content**: Chai/tea theme makes examples relatable and fun
- **Comprehensive Coverage**: From basics to advanced topics
- **Runnable Code**: Every example can be executed immediately
- **Modern Python**: Covers contemporary features like async/await and Pydantic
- **Best Practices**: Demonstrates proper code organization and patterns

## 📝 Code Style

This repository follows Python best practices:
- PEP 8 style guidelines
- Clear variable and function names
- Commented code where necessary
- Modular and reusable code structure

## 🛠️ Configuration

The project includes `pyrightconfig.json` for type checking and IDE support.

## 🤝 Contributing

This is a personal learning repository, but feel free to:
- Fork and create your own learning journey
- Suggest improvements or corrections
- Add your own examples using the chai theme

## 📖 Topics Summary

| Category | Focus Area | Files |
|----------|-----------|-------|
| Fundamentals | Syntax, data types, control flow | 30+ files |
| Functions | Organization, scope, parameters | 12 files |
| OOP | Classes, inheritance, methods | 11 files |
| Advanced | Generators, decorators, async | 20+ files |
| Concurrency | Threading, multiprocessing, async | 21 files |
| Modern Python | Pydantic, type validation | 10+ files |

## 🎓 Learning Outcomes

After completing this repository, you'll be able to:
- ✅ Write clean, Pythonic code
- ✅ Build modular applications with proper structure
- ✅ Handle errors gracefully
- ✅ Work with concurrent and asynchronous code
- ✅ Apply object-oriented programming principles
- ✅ Validate data using modern tools like Pydantic
- ✅ Understand Python internals (GIL, MRO, etc.)

## 📚 Dependencies

Main dependencies (see `01_virtual/requirements.txt`):
- `requests==2.31.0` - HTTP library
- `flask==3.1.0` - Web framework
- `pydantic` - Data validation (for section 14)

## 💡 Tips for Learning

1. **Type the code yourself** - Don't just read, practice!
2. **Experiment** - Modify examples and see what happens
3. **Break things** - Learn from errors
4. **Build projects** - Apply concepts to your own ideas
5. **Review regularly** - Revisit earlier topics as you advance

## 📞 Support

For Python documentation and resources:
- [Official Python Documentation](https://docs.python.org/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python](https://realpython.com/)
- [Python Package Index (PyPI)](https://pypi.org/)

---

**Happy Coding! ☕🐍**

*Remember: The best way to learn programming is by doing. Run every example, break the code, fix it, and make it your own!*

