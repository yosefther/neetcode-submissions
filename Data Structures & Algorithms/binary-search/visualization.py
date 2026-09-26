"""Render from the repository root: manim -pql "Data Structures & Algorithms/binary-search/visualization.py" BinarySearchScene."""

import sys
from pathlib import Path

# Manim loads this file by path; make the shared helpers importable.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from visualizations.common import AlgorithmScene


class BinarySearchScene(AlgorithmScene):
    def construct(self):
        nums, target = [-1, 0, 3, 5, 9, 12], 9
        self.begin("Binary Search", f"target = {target}; repeatedly halve the sorted search interval", nums)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            discarded = [i for i in range(len(nums)) if i < left or i > right]
            self.step(f"mid = ({left} + {right}) // 2 = {mid}", f"left = {left}, mid = {mid}, right = {right}\nnums[mid] = {nums[mid]}", active=[mid], discarded=discarded, pointers={"left": left, "mid": mid, "right": right})
            if nums[mid] == target:
                self.step("Target found at the midpoint", f"index = {mid}", matched=[mid], discarded=discarded, pointers={"left": left, "mid": mid, "right": right})
                self.finish(mid, "Time: O(log n) | Extra space: O(1)")
                return
            if nums[mid] < target:
                left = mid + 1
                reason = "Midpoint value is too small: move left to mid + 1"
            else:
                right = mid - 1
                reason = "Midpoint value is too large: move right to mid - 1"
            self.step(reason, f"left = {left}, right = {right}", discarded=[i for i in range(len(nums)) if i < left or i > right], pointers={"left": left, "right": right})
        self.finish(-1, "Time: O(log n) | Extra space: O(1)")
