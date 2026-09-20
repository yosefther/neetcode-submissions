"""Render from the repository root: manim -pql "Data Structures & Algorithms/two-integer-sum/visualization.py" TwoSumScene."""

import sys
from pathlib import Path

# Manim loads this file by path; make the shared helpers importable.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from visualizations.common import AlgorithmScene


class TwoSumScene(AlgorithmScene):
    def construct(self):
        nums, target = [2, 7, 11, 15], 9
        self.begin("Two Sum", f"target = {target}; store previous values and indices", nums)
        seen = {}
        for index, value in enumerate(nums):
            needed = target - value
            self.step(f"Need {target} - {value} = {needed}", f"seen = {self.mapping(seen)}", active=[index])
            if needed in seen:
                result = [seen[needed], index]
                self.step("Complement found: return zero-based indices", f"seen = {self.mapping(seen)}", matched=result, pointers={"found": result[0], "i": index})
                self.finish(result, "Time: O(n) expected | Extra space: O(n)")
                return
            seen[value] = index
            self.step(f"Store value {value} at index {index}", f"seen = {self.mapping(seen)}", active=[index])
