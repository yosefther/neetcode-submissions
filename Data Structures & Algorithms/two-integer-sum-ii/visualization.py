"""Render from the repository root: manim -pql "Data Structures & Algorithms/two-integer-sum-ii/visualization.py" TwoSumIIScene."""

import sys
from pathlib import Path

# Manim loads this file by path; make the shared helpers importable.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from visualizations.common import AlgorithmScene


class TwoSumIIScene(AlgorithmScene):
    def construct(self):
        numbers, target = [2, 3, 4, 7, 11], 9
        self.begin("Two Sum II", f"target = {target}; this submission uses a two-pass hash map", numbers)
        seen = {}
        for index, value in enumerate(numbers):
            seen[value] = index
            self.step(f"Pass 1: store {value} -> index {index}", f"seen = {self.mapping(seen)}", active=[index])
        for index, value in enumerate(numbers):
            needed = target - value
            self.step(f"Pass 2: look up complement {needed}; require a different index", f"seen = {self.mapping(seen)}", active=[index])
            if needed in seen and seen[needed] != index:
                indices = [index, seen[needed]]
                self.step("Convert both indices to one-based positions", f"zero-based = {indices}", matched=indices, pointers={"i": index, "found": seen[needed]})
                self.finish([i + 1 for i in indices], "Time: O(n) expected | Extra space: O(n)")
                return
