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


class KokoBinarySearchScene(AlgorithmScene):
    """Trace submission-1.py with pointers over candidate eating speeds."""

    def cell(self, value, index):
        # The cells contain speeds, so array indices would be misleading.
        cell = super().cell(value, index)
        cell.remove(cell[2])
        return cell

    def construct(self):
        import math

        piles, h = [3, 6, 7, 11], 8
        max_speed = max(piles)
        left, right = 1, max_speed
        res = right
        best_tested = False
        self.begin(
            "Koko Eating Bananas: Binary Search",
            f"piles = {piles}, h = {h} | cells show speeds in bananas/hour",
            list(range(1, max_speed + 1)),
            input_label_text="",
        )

        def eliminated():
            # Keep the best feasible candidate visible in green.
            return [speed - 1 for speed in range(1, max_speed + 1)
                    if (speed < left or speed > right)
                    and not (best_tested and speed == res)]

        def state(pile_hours, hours):
            return (f"piles = {piles}\n"
                    f"hours per visited pile = {pile_hours}\n"
                    f"total hours = {hours} / {h} allowed; best speed = {res}")

        while left <= right:
            mid = (left + right) // 2
            hours = 0
            pile_hours = []
            pointers = {"left": left - 1, "mid": mid - 1, "right": right - 1}
            matched = [res - 1] if best_tested else []
            self.step(
                f"mid = ({left} + {right}) // 2 = {mid}; test this speed",
                state(pile_hours, hours), active=[mid - 1], matched=matched,
                discarded=eliminated(), pointers=pointers,
            )
            for index, pile in enumerate(piles):
                required = math.ceil(pile / mid)
                hours += required
                pile_hours.append(required)
                self.step(
                    f"Pile {index + 1}: ceil({pile} / {mid}) = {required} hours",
                    state(pile_hours, hours), active=[mid - 1], matched=matched,
                    discarded=eliminated(), pointers=pointers,
                )
            if hours <= h:
                res = min(res, mid)
                best_tested = True
                self.step(
                    f"{hours} <= {h}: feasible! Save best = {res}; try slower speeds",
                    state(pile_hours, hours), matched=[res - 1],
                    discarded=eliminated(), pointers=pointers,
                )
                right = mid - 1
                reason = f"Move right to {right}; keep speed {res} as the best answer"
            else:
                self.step(
                    f"{hours} > {h}: too slow! All speeds <= {mid} also fail",
                    state(pile_hours, hours), active=[mid - 1], matched=matched,
                    discarded=eliminated(), pointers=pointers,
                )
                left = mid + 1
                reason = f"Move left to {left}; search faster speeds"
            self.step(
                reason, f"bounds = left {left}, right {right}\nbest speed = {res}",
                matched=[res - 1] if best_tested else [], discarded=eliminated(),
                pointers={"left": left - 1, "right": right - 1} if left <= right else {"best": res - 1},
            )

        self.step(
            f"left = {left} > right = {right}: search complete; return {res}",
            f"minimum speed = {res} bananas/hour\nhours at this speed = {sum(math.ceil(pile / res) for pile in piles)}",
            matched=[res - 1], discarded=eliminated(), pointers={"best": res - 1},
        )
        self.finish(res, "Time: O(n log M) | Extra space: O(1), M = largest pile")
