# Turing machine simulator
## Deterministic Turing Machine
A turing machine simulator that accepts a string and processes it according to a given set of transitions.

## Non-Deterministic Turing Machine
Implementation of a non-deterministic turing machine that accepts or rejects string based on a given set of transitions.

In contrast to a deterministic Turing machine, in a nondeterministic Turing machine (NTM) the set of rules may prescribe more than one action to be performed for any given situation. Look main.py for more example

## a sample call of method Non_Deterministic_Turing_Machine
```python
transitions = [(0, 'x', 'x', 'R', 0), (0, 'w', 'w', 's', 1)]
accepted_states = [1]
max_iterations = 50
input_strings = ['aa', 'ab', 'aaab', 'fuck w', 'bba']

turing_machine = TuringMachine(transitions, accepted_states, max_iterations)
for string in input_strings:
    output = turing_machine.validate_string(list(string))
    print(string, output)```
