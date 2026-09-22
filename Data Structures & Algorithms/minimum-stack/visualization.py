"""Render from the repository root: manim -pql "Data Structures & Algorithms/minimum-stack/visualization.py" MinStackScene."""

import sys
from pathlib import Path

# Manim loads this file by path; make the shared helpers importable.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from visualizations.common import AlgorithmScene


class MinStackScene(AlgorithmScene):
    def construct(self):
        values = [-2, 0, -3, -3]
        self.begin("Min Stack", "A second stack stores every new or equal minimum", values)
        stack, minimums = [], []
        for index, value in enumerate(values):
            stack.append(value)
            if not minimums or value <= minimums[-1]:
                minimums.append(value)
                caption = f"Push {value} onto both stacks (new or equal minimum)"
            else:
                caption = f"Push {value} onto the main stack only"
            self.step(caption, f"stack = {stack}\nminimum stack = {minimums}\ngetMin() = {minimums[-1]}", active=[index])
        for _ in range(2):
            value = stack.pop()
            if value == minimums[-1]:
                minimums.pop()
            self.step(f"Pop {value}; pop the minimum stack when its top matches", f"stack = {stack}\nminimum stack = {minimums}\ngetMin() = {minimums[-1]}")
        self.finish(f"top = {stack[-1]}, minimum = {minimums[-1]}", "Time: O(1) per operation | Extra space: O(n)")
