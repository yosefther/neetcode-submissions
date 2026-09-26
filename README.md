# NeetCode Practice

My working collection of data structures and algorithms solutions.

This repository is less about collecting green checkmarks and more about building a focused reference for the patterns I have learned. Each problem folder keeps the strongest solution from my attempts.

## Progress

<!-- progress:start -->
**15 problems · 18 Python submissions**

| Pattern | Problems |
| --- | --- |
| Arrays & hashing | [Contains Duplicate](<Data Structures & Algorithms/duplicate-integer>), [Valid Anagram](<Data Structures & Algorithms/is-anagram>), [Two Sum](<Data Structures & Algorithms/two-integer-sum>), [Group Anagrams](<Data Structures & Algorithms/anagram-groups>), [Top K Frequent Elements](<Data Structures & Algorithms/top-k-elements-in-list>), [Encode and Decode Strings](<Data Structures & Algorithms/string-encode-and-decode>) |
| Two pointers | [Valid Palindrome](<Data Structures & Algorithms/is-palindrome>), [Two Sum II](<Data Structures & Algorithms/two-integer-sum-ii>), [3Sum](<Data Structures & Algorithms/three-integer-sum>) |
| Stack | [Valid Parentheses](<Data Structures & Algorithms/validate-parentheses>), [Min Stack](<Data Structures & Algorithms/minimum-stack>), [Evaluate Reverse Polish Notation](<Data Structures & Algorithms/evaluate-reverse-polish-notation>) |
| Binary search | [Binary Search](<Data Structures & Algorithms/binary-search>), [Search a 2D Matrix](<Data Structures & Algorithms/search-2d-matrix>), [Koko Eating Bananas](<Data Structures & Algorithms/koko-eating-bananas>) |
<!-- progress:end -->

## Repository layout

```text
Data Structures & Algorithms/
└── problem-name/
    ├── submission-N.py
    └── visualization.py
```

Each problem has its own directory and one or more synced submissions. The numeric suffix preserves each solution's original submission number.

## Solution visualizations

Each problem includes a Manim Community scene that traces its submitted algorithm on a small example. Moving arrows point to the current input values: `i` marks the current index, and search scenes name their pointers (`left`, `mid`, `right`, or `fixed`/`scan`). Yellow cells mark the current step, green cells mark a match or selection, and faded cells mark eliminated search candidates. Boxed values show the working sets, maps, and stacks; stack tops are labeled. Each step pauses so you can read its explanation. Indices beneath cells are zero-based; Two Sum II returns one-based positions.

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and the native dependencies for your operating system using the [Manim installation guide](https://docs.manim.community/en/stable/installation.html). From the repository root, set up the environment once:

```bash
uv venv --python 3.12
uv pip install -r requirements-visualizations.txt
```

Render a scene using `uv run`:

```bash
uv run manim -pql "Data Structures & Algorithms/duplicate-integer/visualization.py" ContainsDuplicateScene
```

For example, to render the Koko Eating Bananas binary search solution:

```bash
uv run manim -pqm "Data Structures & Algorithms/koko-eating-bananas/visualization.py" KokoBinarySearchScene
```

Replace the file path and scene name with an entry below to render another problem. `-pql` renders a low quality preview and opens it; use `-pqm` for a sharper 720p preview with more readable text; use `-qh` for high quality output, or omit `-p` when running without a desktop. Generated videos are saved under `media/videos/`.

The scenes use `Text` and do not require LaTeX. Shared layout helpers live in [visualizations/common.py](visualizations/common.py). The animation code is separate from the submissions and is not included in the Python submission count.

| Problem | Visualization source | Scene name |
| --- | --- | --- |
| Contains Duplicate | [visualization.py](<Data Structures & Algorithms/duplicate-integer/visualization.py>) | `ContainsDuplicateScene` |
| Valid Anagram | [visualization.py](<Data Structures & Algorithms/is-anagram/visualization.py>) | `ValidAnagramScene` |
| Two Sum | [visualization.py](<Data Structures & Algorithms/two-integer-sum/visualization.py>) | `TwoSumScene` |
| Group Anagrams | [visualization.py](<Data Structures & Algorithms/anagram-groups/visualization.py>) | `GroupAnagramsScene` |
| Top K Frequent Elements | [visualization.py](<Data Structures & Algorithms/top-k-elements-in-list/visualization.py>) | `TopKFrequentScene` |
| Encode and Decode Strings | [visualization.py](<Data Structures & Algorithms/string-encode-and-decode/visualization.py>) | `EncodeDecodeScene` |
| Valid Palindrome | [visualization.py](<Data Structures & Algorithms/is-palindrome/visualization.py>) | `ValidPalindromeScene` |
| Two Sum II | [visualization.py](<Data Structures & Algorithms/two-integer-sum-ii/visualization.py>) | `TwoSumIIScene` |
| 3Sum | [visualization.py](<Data Structures & Algorithms/three-integer-sum/visualization.py>) | `ThreeSumScene` |
| Valid Parentheses | [visualization.py](<Data Structures & Algorithms/validate-parentheses/visualization.py>) | `ValidParenthesesScene` |
| Min Stack | [visualization.py](<Data Structures & Algorithms/minimum-stack/visualization.py>) | `MinStackScene` |
| Evaluate Reverse Polish Notation | [visualization.py](<Data Structures & Algorithms/evaluate-reverse-polish-notation/visualization.py>) | `ReversePolishNotationScene` |
| Binary Search | [visualization.py](<Data Structures & Algorithms/binary-search/visualization.py>) | `BinarySearchScene` |
| Search a 2D Matrix | [visualization.py](<Data Structures & Algorithms/search-2d-matrix/visualization.py>) | `SearchMatrixScene` |
| Koko Eating Bananas (linear scan) | [visualization.py](<Data Structures & Algorithms/koko-eating-bananas/visualization.py>) | `KokoEatingBananasScene` |
| Koko Eating Bananas (binary search) | [visualization.py](<Data Structures & Algorithms/koko-eating-bananas/visualization.py>) | `KokoBinarySearchScene` |

Koko Eating Bananas includes a [linear scan solution](<Data Structures & Algorithms/koko-eating-bananas/submission-0.py>) with O(n * M) time and a [binary search solution](<Data Structures & Algorithms/koko-eating-bananas/submission-1.py>) with O(n log M) time. Both use O(1) extra space, where M is the largest pile. The binary search scene places `left`, `mid`, and `right` pointers over candidate speeds, calculates `math.ceil(pile / mid)` for each pile, and saves the best feasible speed while narrowing the range.

Render the binary search scene with the command above to create `media/videos/visualization/720p30/KokoBinarySearchScene.mp4`. Generated videos stay local in the ignored `media/` directory.

## Approach

For each problem, I aim to:

1. Get to a correct solution independently.
2. Understand the time and space complexity.
3. Identify the underlying reusable pattern.
4. Revisit the solution when a cleaner approach becomes clear.

The code is intentionally close to the format used by coding platforms, so type hints such as `List` may rely on the platform-provided environment.

---

Built through consistent practice by [@yosefther](https://github.com/yosefther).
