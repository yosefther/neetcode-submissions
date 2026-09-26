"""Render from the repository root: manim -pql "Data Structures & Algorithms/is-palindrome/visualization.py" ValidPalindromeScene."""

import sys
from pathlib import Path

# Manim loads this file by path; make the shared helpers importable.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from visualizations.common import AlgorithmScene


class ValidPalindromeScene(AlgorithmScene):
    def construct(self):
        import re
        source = "No 'x' in Nixon"
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', source).lower()
        self.begin("Valid Palindrome", "Keep ASCII letters and digits, lowercase, then compare to reverse", list(cleaned))
        self.step("Remove punctuation and spaces; lowercase", f"original = {source!r}\ncleaned = {cleaned!r}")
        reversed_text = cleaned[::-1]
        self.step("Create the reversed copy with [::-1]", f"cleaned = {cleaned}\nreverse = {reversed_text}")
        # Expand the string equality into visible character comparisons.
        for index, (character, reversed_character) in enumerate(zip(cleaned, reversed_text)):
            self.step(
                f"Compare position {index}: {character!r} == {reversed_character!r}",
                f"cleaned = {cleaned}\nreverse = {reversed_text}\ncomparison = {character!r} == {reversed_character!r}",
                active=[index],
                matched=range(index),
                pointers={"compare": index},
            )
            if character != reversed_character:
                self.finish(False, "Time: O(n) | Extra space: O(n)")
                return
        self.step("Both complete strings match", f"{cleaned!r} == {reversed_text!r}", matched=range(len(cleaned)))
        self.finish(cleaned == reversed_text, "Time: O(n) | Extra space: O(n)")
