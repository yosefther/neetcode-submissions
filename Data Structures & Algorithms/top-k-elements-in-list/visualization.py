"""Render from the repository root: manim -pql "Data Structures & Algorithms/top-k-elements-in-list/visualization.py" TopKFrequentScene."""

import sys
from pathlib import Path

# Manim loads this file by path; make the shared helpers importable.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from visualizations.common import AlgorithmScene


class TopKFrequentScene(AlgorithmScene):
    def construct(self):
        nums, k = [1, 1, 1, 2, 2, 3], 2
        self.begin("Top K Frequent Elements", f"k = {k}; count values, then use frequency buckets", nums)
        counts = {}
        for index, value in enumerate(nums):
            counts[value] = counts.get(value, 0) + 1
            self.step(f"Increment the count for {value}", f"counts = {self.mapping(counts)}", active=[index])
        buckets = [[] for _ in range(len(nums) + 1)]
        for value, frequency in counts.items():
            buckets[frequency].append(value)
            state = "\n".join(f"frequency {i}: {bucket}" for i, bucket in enumerate(buckets) if bucket)
            self.step(f"Put {value} into bucket {frequency}", state)
        result = []
        for frequency in range(len(nums), 0, -1):
            self.step(f"Scan frequency {frequency} from largest to smallest", f"bucket = {buckets[frequency]}\nresult = {result}")
            for value in buckets[frequency]:
                result.append(value)
                self.step(f"Select {value}", f"result = {result}", matched=[i for i, num in enumerate(nums) if num in result])
                if len(result) == k:
                    self.finish(result, "Time: O(n) expected | Extra space: O(n)")
                    return
