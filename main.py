#!/usr/bin/python
# Non-Deterministic Turing Machine Simulator
# Example: Automata that accepts strings that ends with 'w'
from src.Non_Deterministic_Turing_Machine import TuringMachine

transitions = [(0, 'x', 'x', 'R', 0), (0, 'w', 'w', 's', 1)]
accepted_states = [1]
max_iterations = 50
input_strings = ['aa', 'ab', 'aaab', 'fuck w', 'bba']

turing_machine = TuringMachine(transitions, accepted_states, max_iterations)
for string in input_strings:
    output = turing_machine.validate_string(list(string))
    print(string, output)
