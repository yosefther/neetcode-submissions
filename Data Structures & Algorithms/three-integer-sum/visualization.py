"""Render from the repository root: manim -pql "Data Structures & Algorithms/three-integer-sum/visualization.py" ThreeSumScene."""

import sys
from pathlib import Path

# Manim loads this file by path; make the shared helpers importable.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from visualizations.common import AlgorithmScene


class ThreeSumScene(AlgorithmScene):
    def construct(self):
        nums = [-1, 0, 1, 2, -1, -4]
        self.begin("3Sum", "Fix one value; scan the rest with a fresh complement map", nums)
        result = set()
        for i in range(len(nums) - 2):
            seen = {}
            self.step(f"Fix index {i}: value {nums[i]}; reset seen", f"seen = {{}}\ntriplets = {sorted(result)}", active=[i], pointers={"fixed": i})
            for j in range(i + 1, len(nums)):
                needed = -nums[i] - nums[j]
                state = f"seen = {self.mapping(seen)}\ntriplets = {sorted(result)}"
                self.step(f"Need {-nums[i]} - {nums[j]} = {needed}", state, active=[i, j], pointers={"fixed": i, "scan": j})
                if needed in seen:
                    triplet = tuple(sorted([nums[i], nums[j], needed]))
                    result.add(triplet)
                    self.step("Sort the triplet; the result set removes duplicates", f"triplets = {sorted(result)}", matched=[i, j, seen[needed]], pointers={"fixed": i, "scan": j, "found": seen[needed]})
                seen[nums[j]] = j
        self.finish([list(item) for item in sorted(result)], "Time: O(n^2) expected | Space: O(n + r), r = result count")
