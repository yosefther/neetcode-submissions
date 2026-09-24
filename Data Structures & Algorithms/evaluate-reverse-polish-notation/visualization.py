"""Render from the repository root: manim -pql "Data Structures & Algorithms/evaluate-reverse-polish-notation/visualization.py" ReversePolishNotationScene."""

import sys
from pathlib import Path

# Manim loads this file by path; make the shared helpers importable.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from visualizations.common import AlgorithmScene


class ReversePolishNotationScene(AlgorithmScene):
    def construct(self):
        tokens = ["7", "-3", "/", "2", "*"]
        self.begin("Evaluate Reverse Polish Notation", "Push operands; pop right then left for each operator", tokens)
        stack = []
        for index, token in enumerate(tokens):
            if token not in ("+", "-", "*", "/"):
                stack.append(int(token))
                self.step(f"Push operand {token}", f"stack (bottom -> top) = {stack}", active=[index])
                continue
            right, left = stack.pop(), stack.pop()
            if token == "+":
                value = left + right
            elif token == "-":
                value = left - right
            elif token == "*":
                value = left * right
            else:
                value = int(left / right)
            self.step(f"Pop right = {right}, left = {left}; compute {left} {token} {right}", f"remaining stack = {stack}\noperation result = {value}", active=[index])
            stack.append(value)
            caption = "Division truncates toward zero" if token == "/" else "Push the operation result"
            self.step(caption, f"stack (bottom -> top) = {stack}", matched=[index])
        self.finish(stack[0], "Time: O(n) | Extra space: O(n)")
