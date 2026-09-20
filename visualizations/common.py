"""Shared, readable Manim layout with moving pointers and state cards."""

import ast
from collections import defaultdict

from manimpango import list_fonts

from manim import (
    Arrow, DOWN, FadeIn, FadeOut, LEFT, RIGHT, RoundedRectangle,
    Scene, Text, Transform, UP, VGroup,
)

AVAILABLE_FONTS = set(list_fonts())
FONT = next((name for name in ("Inter", "DejaVu Sans", "Arial") if name in AVAILABLE_FONTS), "")

BACKGROUND = "#0B1220"
PANEL = "#131F33"
BORDER = "#2D4260"
INK = "#F1F5F9"
MUTED = "#94A8C4"
ACCENT = "#56CFE1"
CURRENT = "#FFD166"
MATCH = "#70E1A1"
POINTER_COLORS = (CURRENT, ACCENT, "#C4A1FF")


class AlgorithmScene(Scene):
    """Keep input, working state, explanation, and result in fixed regions."""

    def begin(self, title, description, values):
        self.camera.background_color = BACKGROUND
        self.step_number = 0
        self.pointer_side = UP
        self.state_position = DOWN * 1.05
        heading = self.label(title, 36, 11.7).move_to(UP * 3.35)
        subtitle = self.label(description, 21, 12).move_to(UP * 2.8)
        subtitle.set_color(MUTED)
        input_panel = self.panel(12.8, 2.15).move_to(UP * 1.5)
        state_panel = self.panel(12.8, 2.25).move_to(DOWN)
        caption_panel = self.panel(12.8, 0.8).move_to(DOWN * 2.7)
        input_label = self.label("INPUT", 16, 1.2, MUTED).move_to(LEFT * 5.8 + UP * 2.3)
        state_label = self.label("WORKING STATE", 16, 3, ACCENT).move_to(LEFT * 4.95 + DOWN * 0.14)
        self.counter = self.label("STEP 00", 16, 1.5, MUTED).move_to(RIGHT * 5.55 + DOWN * 0.14)
        self.cells = VGroup(*[self.cell(value, index) for index, value in enumerate(values)])
        self.cells.arrange(RIGHT, buff=0.22)
        if self.cells.width > 11.5:
            self.cells.scale_to_fit_width(11.5)
        self.cells.move_to(UP * 1.35)
        self.state = self.state_view("Ready to begin")
        self.caption = self.label("Follow the arrow to see which value is being read.", 23, 11.8).move_to(DOWN * 2.7)
        self.pointers = VGroup()
        self.add(input_panel, state_panel, caption_panel, input_label, state_label, self.counter)
        self.play(FadeIn(heading), FadeIn(subtitle), FadeIn(self.cells), FadeIn(self.state), FadeIn(self.caption))
        self.wait(0.7)

    @staticmethod
    def panel(width, height):
        return RoundedRectangle(width=width, height=height, corner_radius=0.16,
                                stroke_color=BORDER, stroke_width=1.3,
                                fill_color=PANEL, fill_opacity=1)

    @staticmethod
    def label(value, size=25, width=11, color=INK):
        label = Text(str(value) or " ", font_size=size, color=color, font=FONT)
        if label.width > width:
            label.scale_to_fit_width(width)
        return label

    def cell(self, value, index):
        box = RoundedRectangle(width=0.95, height=0.72, corner_radius=0.12,
                               stroke_color=BORDER, stroke_width=2,
                               fill_color="#1D304B", fill_opacity=1)
        display = repr(value) if isinstance(value, str) else value
        value_label = self.label(display, 27, 0.8)
        index_label = self.label(index, 17, 0.7, MUTED).next_to(box, DOWN, buff=0.12)
        return VGroup(box, value_label, index_label)

    def state_view(self, state):
        """Turn list/dictionary/set values into individual readable chips."""
        lines = VGroup()
        for line in str(state).splitlines():
            key, separator, raw = line.partition(" = ")
            if not separator:
                key, separator, raw = line.partition(" -> ")
            if not separator:
                lines.add(self.label(line, 25, 11.4))
                continue
            name = self.label(key, 22, 3.3, ACCENT)
            try:
                value = ast.literal_eval(raw)
            except (ValueError, SyntaxError):
                value = None
            if isinstance(value, dict):
                entries = [f"{k!r}: {v!r}" for k, v in value.items()]
            elif isinstance(value, (list, tuple, set)):
                entries = [repr(item) for item in value]
            else:
                entries = None
            if entries is not None:
                chips = VGroup()
                for entry in entries or ["empty"]:
                    text = self.label(entry, 23, 7)
                    box = self.panel(max(0.65, text.width + 0.3), 0.46)
                    box.set_fill("#203752", opacity=1)
                    chips.add(VGroup(box, text))
                display = chips.arrange(RIGHT, buff=0.1)
                if "stack" in key.lower() and entries:
                    top = self.label("top", 15, 0.6, CURRENT)
                    top.next_to(display[-1], RIGHT, buff=0.12)
                    display.add(top)
                if display.width > 7.5:
                    display.scale_to_fit_width(7.5)
            else:
                display = self.label(raw, 25, 7.5)
            lines.add(VGroup(name, display).arrange(RIGHT, buff=0.3))
        lines.arrange(DOWN, aligned_edge=LEFT, buff=0.17)
        if lines.height > 1.5:
            lines.scale_to_fit_height(1.5)
        if lines.width > 11.4:
            lines.scale_to_fit_width(11.4)
        return lines.move_to(self.state_position)

    def pointer_view(self, pointers, matched):
        grouped = defaultdict(list)
        for name, index in pointers.items():
            if 0 <= index < len(self.cells):
                grouped[index].append(name)
        result = VGroup()
        for order, (index, names) in enumerate(grouped.items()):
            color = MATCH if index in matched else POINTER_COLORS[order % len(POINTER_COLORS)]
            box = self.cells[index][0]
            if self.pointer_side is LEFT:
                end = box.get_left() + LEFT * 0.05
                start = end + LEFT * 0.5
                arrow = Arrow(start, end, buff=0, color=color, stroke_width=4, tip_length=0.14)
                label = self.label(" / ".join(names), 18, 1.3, color).next_to(arrow, LEFT, buff=0.08)
            else:
                end = box.get_top() + UP * 0.06
                start = end + UP * 0.4
                arrow = Arrow(start, end, buff=0, color=color, stroke_width=4, tip_length=0.14)
                label = self.label(" / ".join(names), 18, 1.45, color).next_to(arrow, UP, buff=0.06)
            result.add(VGroup(arrow, label))
        return result

    def step(self, caption, state, active=(), matched=(), discarded=(), pointers=None):
        active, matched, discarded = tuple(active), tuple(matched), tuple(discarded)
        if pointers is None:
            pointers = {"i" if len(active) == 1 else f"i{rank + 1}": index
                        for rank, index in enumerate(active)}
            if not pointers and 0 < len(matched) <= 3:
                pointers = {f"match {rank + 1}": index for rank, index in enumerate(matched)}
        animations = []
        for index, cell in enumerate(self.cells):
            color = MATCH if index in matched else CURRENT if index in active else BORDER
            opacity = 0.22 if index in discarded else 1
            highlighted = index in matched or index in active
            animations.append(cell[0].animate.set_stroke(color, opacity=opacity, width=3 if highlighted else 2)
                              .set_fill(color if highlighted else "#1D304B", opacity=0.22 if highlighted else opacity))
            animations.extend(part.animate.set_opacity(opacity) for part in cell[1:])
        new_pointers = self.pointer_view(pointers, matched)
        if len(self.pointers) and len(new_pointers):
            animations.append(Transform(self.pointers, new_pointers))
        elif len(new_pointers):
            self.pointers = new_pointers
            animations.append(FadeIn(self.pointers))
        elif len(self.pointers):
            animations.append(FadeOut(self.pointers))
        self.step_number += 1
        new_counter = self.label(f"STEP {self.step_number:02}", 16, 1.5, MUTED).move_to(self.counter)
        animations.extend([
            Transform(self.state, self.state_view(state)),
            Transform(self.caption, self.label(caption, 23, 11.8).move_to(DOWN * 2.7)),
            Transform(self.counter, new_counter),
        ])
        self.play(*animations, run_time=0.65)
        if not len(new_pointers):
            self.pointers = VGroup()
        self.wait(0.85)

    def finish(self, result, complexity):
        output = self.label(f"RESULT  {result}", 28, 11.8, MATCH).move_to(DOWN * 3.4)
        self.play(FadeIn(output))
        self.wait(1.5)
        self.play(Transform(self.caption, self.label(complexity, 22, 11.8, MUTED).move_to(DOWN * 2.7)))
        self.wait(2)

    @staticmethod
    def mapping(mapping):
        return "{ " + ", ".join(f"{key!r}: {value!r}" for key, value in mapping.items()) + " }"
