"""Render from the repository root: manim -pql "Data Structures & Algorithms/search-2d-matrix/visualization.py" SearchMatrixScene."""

import sys
from pathlib import Path

# Manim loads this file by path; make the shared helpers importable.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from visualizations.common import AlgorithmScene


class SearchMatrixScene(AlgorithmScene):
    def construct(self):
        from manim import DOWN, LEFT, Transform, UP, VGroup

        matrix, target = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 16
        rows, cols = len(matrix), len(matrix[0])
        values = [value for row in matrix for value in row]
        self.begin("Search a 2D Matrix", f"target = {target}; search virtual flat indices without copying the matrix", values)
        # Reuse the flat-index cells, now arranged as matrix rows.
        grid = VGroup(*[self.cell(value, index) for index, value in enumerate(values)])
        for cell in grid:
            cell[0].stretch_to_fit_height(0.46)
            cell[1].scale(0.85)
            cell[2].scale(0.85).next_to(cell[0], DOWN, buff=0.03)
        grid.arrange_in_grid(rows=rows, cols=cols, buff=(1.25, 0.03)).move_to(UP * 1.5)
        self.play(Transform(self.cells, grid))
        self.pointer_side = LEFT
        lo, hi = 0, rows * cols - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            row, col = divmod(mid, cols)
            value = matrix[row][col]
            discarded = [i for i in range(len(values)) if i < lo or i > hi]
            self.step(f"divmod({mid}, {cols}) -> row {row}, column {col}", f"lo = {lo}, mid = {mid}, hi = {hi}\nmatrix[{row}][{col}] = {value}", active=[mid], discarded=discarded, pointers={"mid": mid})
            if value == target:
                self.step("Target found in the matrix", f"row = {row}, column = {col}", matched=[mid], discarded=discarded, pointers={"found": mid})
                self.finish(True, "Time: O(log(m * n)) | Algorithm extra space: O(1)")
                return
            if value < target:
                lo = mid + 1
            else:
                hi = mid - 1
        self.finish(False, "Time: O(log(m * n)) | Algorithm extra space: O(1)")
