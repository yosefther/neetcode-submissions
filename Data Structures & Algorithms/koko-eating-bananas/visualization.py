"""Render: manim -pql "Data Structures & Algorithms/koko-eating-bananas/visualization.py" KokoEatingBananasScene."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from visualizations.common import AlgorithmScene


class KokoEatingBananasScene(AlgorithmScene):
    """Trace the submitted linear scan, including ceiling division per pile."""

    def construct(self):
        piles, h = [3, 6, 7, 11], 8
        max_speed = max(piles)
        self.begin(
            "Koko Eating Bananas",
            f"h = {h}; try speeds 1 through {max_speed} in ascending order",
            piles,
        )
        for speed in range(1, max_speed + 1):
            hours = 0
            pile_hours = []
            self.step(
                f"Try {speed} bananas per hour; reset the total",
                f"speed = {speed}\nhours = 0, allowed = {h}",
            )
            for index, pile in enumerate(piles):
                required = (pile + speed - 1) // speed
                pile_hours.append(required)
                hours += required
                self.step(
                    f"Pile {pile}: ({pile} + {speed} - 1) // {speed} = {required} hours",
                    f"speed = {speed}\nhours per visited pile = {pile_hours}\ntotal hours = {hours}, allowed = {h}",
                    active=[index],
                )
            if hours <= h:
                self.step(
                    f"{hours} <= {h}: the first feasible speed is the minimum",
                    f"speed = {speed}\nhours per pile = {pile_hours}\ntotal hours = {hours}",
                    matched=range(len(piles)),
                )
                self.finish(speed, "Time: O(n * M) | Extra space: O(1), M = largest pile")
                return
            self.step(
                f"{hours} > {h}: this speed is too slow; try the next speed",
                f"speed = {speed}\ntotal hours = {hours}, allowed = {h}",
            )
