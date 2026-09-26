"""Render from the repository root: manim -pql "Data Structures & Algorithms/is-anagram/visualization.py" ValidAnagramScene."""

import sys
from pathlib import Path

# Manim loads this file by path; make the shared helpers importable.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from visualizations.common import AlgorithmScene


class ValidAnagramScene(AlgorithmScene):
    def construct(self):
        s, t = "anagram", "nagaram"
        self.begin("Valid Anagram", f"s = {s!r}, t = {t!r}; compare character counts", list(s))
        count_s, count_t = {}, {}
        for index in range(len(s)):
            count_s[s[index]] = count_s.get(s[index], 0) + 1
            count_t[t[index]] = count_t.get(t[index], 0) + 1
            state = f"countS = {self.mapping(count_s)}\ncountT = {self.mapping(count_t)}"
            self.step(f"Read s[{index}] = {s[index]!r} and t[{index}] = {t[index]!r}", state, active=[index])
        self.step("The two frequency maps are equal", state, matched=range(len(s)))
        self.finish(count_s == count_t, "Time: O(n) | Extra space: O(u), u = distinct characters")
