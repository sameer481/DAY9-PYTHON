"""
Day 9: Python While Loops & Nested Loops - Part 2
Topic: Nested Loops, Multidimensional Structure Traversal & Multi-Level Break Techniques

Nested loops occur when one loop statement is placed inside another loop statement.
For every single iteration of the outer loop, the inner loop executes its complete cycle.

Key Concepts Covered:
1. Nested loop execution flow (Outer vs Inner cycles, Time Complexity O(N*M)).
2. Combinations of loop types (nested while, nested for, mixed while-for).
3. 2D Matrix traversal, coordinate scanning & multi-dimensional indexing.
4. Multi-level break strategies (Flags, Functions, Custom Exceptions, itertools.product).
5. Algorithmic Pattern Generation (Pyramids, Diamonds, Multiplication Tables & Coordinate Grids).
"""

import itertools
from typing import List, Optional, Tuple


def header(title: str) -> None:
    """Print a styled visual section header for terminal output formatting."""
    print("\n" + "=" * 75)
    print(f" {title.upper()} ")
    print("=" * 75)


# ==============================================================================
# 1. NESTED LOOP MECHANICS & ITERATION COUNTING
# ==============================================================================
def demonstrate_nested_iteration_mechanics() -> None:
    """Demonstrates outer vs inner loop execution cycles and iteration multiplication."""
    header("1. Nested Loop Iteration Mechanics & Cycles")
    
    outer_limit = 3
    inner_limit = 4
    total_iterations = 0

    print(f"Executing Outer Loop ({outer_limit} times) x Inner Loop ({inner_limit} times):")
    
    i = 1
    while i <= outer_limit:
        print(f"\n[OUTER LOOP] Iteration i = {i}")
        j = 1
        while j <= inner_limit:
            total_iterations += 1
            print(f"   -> [INNER LOOP] Step j = {j} (Total Iteration Count: {total_iterations})")
            j += 1
        i += 1

    print(f"\nSummary: Outer ({outer_limit}) * Inner ({inner_limit}) = {total_iterations} Total Operations [O(N*M)]")


# ==============================================================================
# 2. 2D MATRIX TRAVERSAL & MULTIDIMENSIONAL SEARCH
# ==============================================================================
def demonstrate_matrix_traversal() -> None:
    """Demonstrates row-major and column-major nested iteration over 2D data grids."""
    header("2. 2D Matrix Traversal & Multi-Dimensional Grid Search")
    
    grid = [
        [15, 28, 34, 42],
        [51, 67, 79, 83],
        [90, 14, 25, 36]
    ]

    rows = len(grid)
    cols = len(grid[0])
    
    print(f"Grid dimensions: {rows} Rows x {cols} Columns")
    print("\nVisualizing Matrix Layout with Row/Col Coordinate Mapping:")
    
    r = 0
    while r < rows:
        print(f"  Row {r}: ", end="")
        c = 0
        while c < cols:
            val = grid[r][c]
            print(f"[{r},{c}]={val:02d}", end="  ")
            c += 1
        print()
        r += 1


# ==============================================================================
# 3. ESCAPING MULTI-LEVEL NESTED LOOPS (4 STRATEGIES)
# ==============================================================================
class MatrixFoundSignal(Exception):
    """Custom control flow exception to break out of arbitrary nested loops cleanly."""
    def __init__(self, row: int, col: int, value: int):
        self.row = row
        self.col = col
        self.value = value


def demonstrate_multi_level_breaks() -> None:
    """Demonstrates four techniques to escape multi-level nested loops when target is found."""
    header("3. Escaping Multi-Level Nested Loops (4 Techniques)")
    
    matrix = [
        [10, 20, 30],
        [40, 99, 60],  # Target 99 is at row 1, col 1
        [70, 80, 90]
    ]
    target = 99
    
    # --- Strategy A: Flag Variable ---
    print("\n--- Strategy A: Boolean Flag Variable ---")
    found_flag = False
    target_pos: Optional[Tuple[int, int]] = None
    
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == target:
                found_flag = True
                target_pos = (r, c)
                break  # Breaks inner loop
        if found_flag:
            break  # Breaks outer loop
            
    print(f"  [FLAG METHOD] Target {target} found at position {target_pos}")

    # --- Strategy B: Helper Function with Early Return ---
    print("\n--- Strategy B: Helper Function Early Return ---")
    def search_matrix_func(data: List[List[int]], val: int) -> Optional[Tuple[int, int]]:
        for r_idx, row_data in enumerate(data):
            for c_idx, cell in enumerate(row_data):
                if cell == val:
                    return (r_idx, c_idx)  # Instantly exits ALL nested levels
        return None

    pos = search_matrix_func(matrix, target)
    print(f"  [FUNCTION METHOD] Target {target} found at position {pos}")

    # --- Strategy C: Custom Control Flow Exception ---
    print("\n--- Strategy C: Custom Exception Signal ---")
    try:
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == target:
                    raise MatrixFoundSignal(r, c, target)
    except MatrixFoundSignal as sig:
        print(f"  [EXCEPTION METHOD] Signal Caught! Target {sig.value} found at ({sig.row}, {sig.col})")

    # --- Strategy D: itertools.product Flattening ---
    print("\n--- Strategy D: itertools.product Flattening ---")
    pos_d = None
    for r, c in itertools.product(range(len(matrix)), range(len(matrix[0]))):
        if matrix[r][c] == target:
            pos_d = (r, c)
            break  # Single loop break suffices because Cartesian product is flattened!
            
    print(f"  [ITERTOOLS METHOD] Target {target} found at position {pos_d}")


# ==============================================================================
# 4. ALGORITHMIC PATTERN GENERATION WITH NESTED LOOPS
# ==============================================================================
def demonstrate_pattern_generation() -> None:
    """Generates geometric patterns using nested loop coordinate calculations."""
    header("4. Algorithmic Pattern Rendering")
    
    rows = 5

    # Pattern 1: Right-Angled Triangle
    print("Pattern A: Right-Angled Triangle")
    i = 1
    while i <= rows:
        j = 1
        while j <= i:
            print("*", end=" ")
            j += 1
        print()
        i += 1

    # Pattern 2: Centered Pyramid
    print("\nPattern B: Centered Pyramid")
    r = 1
    while r <= rows:
        # Spaces loop
        spaces = rows - r
        s = 0
        while s < spaces:
            print(" ", end=" ")
            s += 1
        # Stars loop
        stars = (2 * r) - 1
        k = 0
        while k < stars:
            print("*", end=" ")
            k += 1
        print()
        r += 1

    # Pattern 3: Multiplication Table Grid (1 to 5)
    print("\nPattern C: Multiplication Grid (1 to 5)")
    for x in range(1, 6):
        for y in range(1, 6):
            print(f"{x * y:4d}", end="")
        print()


# ==============================================================================
# MAIN EXECUTION ROUTINE
# ==============================================================================
def main() -> None:
    print("=" * 75)
    print("   DAY 9 - MODULE 02: NESTED LOOPS & MULTIDIMENSIONAL STRUCTURES   ")
    print("=" * 75)
    
    demonstrate_nested_iteration_mechanics()
    demonstrate_matrix_traversal()
    demonstrate_multi_level_breaks()
    demonstrate_pattern_generation()


if __name__ == "__main__":
    main()
