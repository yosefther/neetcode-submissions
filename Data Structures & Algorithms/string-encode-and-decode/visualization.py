"""Render from the repository root: manim -pql "Data Structures & Algorithms/string-encode-and-decode/visualization.py" EncodeDecodeScene."""

import sys
from pathlib import Path

# Manim loads this file by path; make the shared helpers importable.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from visualizations.common import AlgorithmScene


class EncodeDecodeScene(AlgorithmScene):
    def construct(self):
        words = ["neet", "a#b", "", "code"]
        self.begin("Encode and Decode Strings", "Length prefixes preserve separators and empty strings", words)
        encoded = ""
        for index, word in enumerate(words):
            segment = f"{len(word)}#{word}"
            encoded += segment
            self.step(f"Append {segment!r}: length + '#' + word", f"encoded = {encoded!r}", active=[index])
        result, offset = [], 0
        while offset < len(encoded):
            separator = encoded.index("#", offset)
            length = int(encoded[offset:separator])
            start = separator + 1
            word = encoded[start:start + length]
            result.append(word)
            self.step(f"At offset {offset}: read length {length}, consume exactly {length} characters", f"encoded = {encoded!r}\ndecoded = {result}", matched=range(len(result)), pointers={"decoded": len(result) - 1})
            offset = start + length
        self.finish(result, "Time: O(L) | Space: O(L + n), L = total characters")
