"""Render from the repository root: manim -pql "Data Structures & Algorithms/validate-parentheses/visualization.py" ValidParenthesesScene."""

import sys
from pathlib import Path

# Manim loads this file by path; make the shared helpers importable.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from visualizations.common import AlgorithmScene


class ValidParenthesesScene(AlgorithmScene):
    def construct(self):
        text, stack = "([{}])", []
        pairs = {')': '(', ']': '[', '}': '{'}
        self.begin("Valid Parentheses", "Push openers; each closer must match the top of the stack", list(text))
        for index, char in enumerate(text):
            if char in "([{":
                stack.append(char)
                self.step(f"Push opener {char!r}", f"stack (bottom -> top) = {stack}", active=[index])
            else:
                self.step(f"Closer {char!r} requires top {pairs[char]!r}", f"stack (bottom -> top) = {stack}", active=[index])
                if not stack or stack[-1] != pairs[char]:
                    self.finish(False, "Time: O(n) | Extra space: O(n)")
                    return
                stack.pop()
                self.step("Matching opener: pop the stack", f"stack (bottom -> top) = {stack}", matched=[index])
        self.finish(not stack, "Time: O(n) | Extra space: O(n)")
