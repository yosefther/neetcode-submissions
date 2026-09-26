from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_speed = max(piles)

        for speed in range(1, max_speed + 1):
            hours = 0
            for pile in piles:
                hours += (pile + speed - 1) // speed
            if hours <= h:
                return speed
