"""Render from the repository root: manim -pql "Data Structures & Algorithms/anagram-groups/visualization.py" GroupAnagramsScene."""

import sys
from pathlib import Path

# Manim loads this file by path; make the shared helpers importable.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from visualizations.common import AlgorithmScene


class GroupAnagramsScene(AlgorithmScene):
    def construct(self):
        words = ["eat", "tea", "tan", "ate", "nat", "bat"]
        self.begin("Group Anagrams", "Sort each lowercase word to form its dictionary key", words)
        groups = {}
        for index, word in enumerate(words):
            key = "".join(sorted(word.lower()))
            groups.setdefault(key, []).append(word)
            state = "\n".join(f"{key!r} -> {values}" for key, values in groups.items())
            self.step(f"{word!r} -> sorted key {key!r} -> append to group", state, active=[index])
        self.finish(list(groups.values()), "Time: O(n * m log m) | Space: O(n * m), m = maximum word length")
