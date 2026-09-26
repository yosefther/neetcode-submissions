"""Render from the repository root: manim -pql "Data Structures & Algorithms/duplicate-integer/visualization.py" ContainsDuplicateScene."""

import sys
from pathlib import Path

# Manim loads this file by path; make the shared helpers importable.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from visualizations.common import AlgorithmScene


class ContainsDuplicateScene(AlgorithmScene):
    def construct(self):
        nums = [1, 2, 3, 1]
        self.begin("Contains Duplicate", "Check membership before adding each value to the set", nums)
        seen = set()
        for index, value in enumerate(nums):
            duplicate = value in seen
            self.step(f"Is {value} already in seen? {duplicate}", f"seen = {sorted(seen)}", active=[index])
            if duplicate:
                matches = [i for i, number in enumerate(nums[:index + 1]) if number == value]
                self.step("The repeated value ends the search", f"seen = {sorted(seen)}", matched=matches, pointers={"first": matches[0], "repeat": index})
                self.finish(True, "Time: O(n) expected | Extra space: O(n)")
                return
            seen.add(value)
            self.step(f"Add {value} to seen", f"seen = {sorted(seen)}", active=[index])
