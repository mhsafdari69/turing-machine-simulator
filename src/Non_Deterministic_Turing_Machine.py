from src.Queue import *


class TuringMachine:
    def __init__(self, transitions, accepted_states, max_iterations):
        self.queue = Queue()
        self.transitions = transitions
        self.accepted_states = accepted_states
        self.max_iterations = max_iterations

    def validate_string(self, string):
        head = 0
        state = self.transitions[0][0]
        iter_count = 1

        self.queue.enqueue(state, head, string, iter_count)

        outputs = self.validate_symbol()
        return self.output(outputs)

    def validate_symbol(self):
        if self.queue.is_empty():
            return [0]

        (state, head, string, iter_count) = self.queue.dequeue()
        outputs = []
        symbol = string[head]

        for (current_state, current_symbol, next_symbol, move, next_state) in self.transitions:
            if state == current_state and (symbol == current_symbol or current_symbol == 'x'):
                if next_state in self.accepted_states and head == len(string) - 1:
                    return [1]

                if iter_count > self.max_iterations:
                    outputs = outputs + ['u']
                else:
                    head_copy, string_copy = head, string

                    if next_symbol != 'x':
                        string_copy[head] = next_symbol

                    (head_copy, string_copy) = self.update_values(head_copy, string_copy, move)

                    self.queue.enqueue(next_state, head_copy, string_copy, iter_count + 1)

        outputs = outputs + self.validate_symbol()
        return outputs

    @staticmethod
    def update_values(head, string, move):
        if move == 'R':
            head += 1
            if head == len(string):
                string = string + ['_']
        elif move == 'L':
            head -= 1
            if head == 0:
                string = ['_'] + string
        return head, string

    @staticmethod
    def output(outputs):
        if 1 in outputs:
            return 'Accepted'
        if 0 in outputs:
            return 'Rejected'
        return 'Undefined'
