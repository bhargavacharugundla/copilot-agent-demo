# Copilot Agent Demo

A simple Python calculator project demonstrating basic arithmetic operations including add, subtract, multiply, and divide with proper error handling.

## Features

- **Add**: Add two numbers
- **Subtract**: Subtract two numbers
- **Multiply**: Multiply two numbers
- **Divide**: Divide two numbers with zero-check validation

## Installation

No external dependencies are required. This project uses only Python's standard library.

```bash
pip install -r requirements.txt
```

## Usage

Run the calculator:

```bash
python main.py
```

Follow the interactive prompts to select an operation and enter your numbers.

### Example

```
Simple Calculator
================

Choose operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit

Enter choice (1/2/3/4/5): 1
Enter first number: 5
Enter second number: 3
Result: 8.0
```

## Error Handling

The calculator includes validation for:
- Division by zero: Raises a `ValueError` if attempting to divide by zero
- Invalid input: Handles non-numeric inputs gracefully

## Project Structure

```
copilot-agent-demo/
├── main.py
├── requirements.txt
└── README.md
```

## License

This project is open source and available under the MIT License.
