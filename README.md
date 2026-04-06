# Quantum Password Security Checker

## Problem
Weak passwords can be cracked more easily. Future quantum computers may crack them even faster.

## Solution
This project checks whether a password is weak, medium, or strong.

It also demonstrates a simple quantum search using Grover's Algorithm with Qiskit.

## Files
- main.py -> Password checker
- quantum_demo.py -> Quantum search demo
- requirements.txt -> Required packages

## Tools Used
- Python
- Qiskit
- Qiskit Aer
- VS Code

## How to Run

1. Run the password checker:
py main.py

2. Run the quantum demo:
py quantum_demo.py

## Example Output
Password Strength: Medium
Quantum Risk: Moderate

Quantum Password Search Result:
{'11': 1000}

## Future Improvement
- Add a graphical interface
- Check more password combinations
- Use a larger quantum circuit