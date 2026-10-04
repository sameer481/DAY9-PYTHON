"""
Day 9: Python While Loops & Nested Loops - Part 4
Topic: Nested Loop Optimization, Performance Profiling & Refactoring Anti-Patterns

Improperly structured nested loops can turn an otherwise clean program into an O(N^2) or
O(N^3) performance bottleneck.

Key Concepts Covered:
1. Identifying common nested loop anti-patterns (O(N^2) list lookups, Pyramid of Doom).
2. Loop Invariant Code Motion (Hoisting static computations out of loop bodies).
3. Hash Set / Hash Map Optimization (Reducing O(N*M) nested scans to O(N+M) set operations).
4. Utilizing itertools module for efficient iterator combinations.
5. Empirical Performance Profiling (Benchmarking execution speed differences using time.perf_counter).
"""

import itertools
import time
from typing import List, Set, Tuple


def header(title: str) -> None:
    """Print a styled visual section header for terminal output formatting."""
    print("\n" + "=" * 75)
    print(f" {title.upper()} ")
    print("=" * 75)


# ==============================================================================
# 1. ANTI-PATTERN 1: O(N^2) LIST LOOKUP IN NESTED LOOPS VS O(N) SET LOOKUP
# ==============================================================================
def demonstrate_list_vs_set_optimization() -> None:
    """
    Demonstrates the classic O(N^2) anti-pattern: linear 'in list' searching inside a loop,
    refactored to O(N+M) using hash set lookup.
    """
    header("1. O(N^2) List Lookup Anti-Pattern vs. O(N+M) Set Optimization")
    
    # Generate test datasets
    list1 = list(range(1, 10001))
    list2 = list(range(5000, 15000))
    
    # --- Slow Anti-Pattern: O(N * M) List Scanning ---
    start_time = time.perf_counter()
    common_elements_slow = []
    for item in list1:
        if item in list2:  # 'in list2' performs an O(M) linear scan for every single element!
            common_elements_slow.append(item)
    slow_duration = time.perf_counter() - start_time
    
    # --- Fast Refactored Pattern: O(N + M) Set Lookup ---
    start_time = time.perf_counter()
    set2: Set[int] = set(list2)  # O(M) conversion to Hash Set
    common_elements_fast = []
    for item in list1:
        if item in set2:  # 'in set2' is an O(1) hash lookup!
            common_elements_fast.append(item)
    fast_duration = time.perf_counter() - start_time

    print(f"Dataset Size: Collection A ({len(list1)} items) x Collection B ({len(list2)} items)")
    print(f"  Slow O(N*M) List Search Execution Time: {slow_duration * 1000:.3f} ms")
    print(f"  Fast O(N+M) Set Search Execution Time:  {fast_duration * 1000:.3f} ms")
    
    if fast_duration > 0:
        speedup = slow_duration / fast_duration
        print(f"  >>> PERFORMANCE SPEEDUP: {speedup:.1f}x Faster! <<<")
    assert len(common_elements_slow) == len(common_elements_fast)


# ==============================================================================
# 2. ANTI-PATTERN 2: LOOP INVARIANT RECALCULATION (HOISTING)
# ==============================================================================
def demonstrate_loop_invariant_hoisting() -> None:
    """
    Demonstrates Loop Invariant Code Motion (Hoisting).
    Computations that produce the exact same value across loop iterations should be
    computed ONCE outside the loop rather than repeatedly recalculated inside.
    """
    header("2. Loop Invariant Code Motion (Hoisting Static Calculations)")
    
    data = list(range(1, 5000))
    config_factor = 42
    
    # --- Anti-Pattern: Computing invariant inside nested loops ---
    start_t = time.perf_counter()
    total_sum_slow = 0
    for i in range(len(data)):
        for j in range(100):
            # Anti-pattern: len(data) * config_factor is constant across all 500,000 inner cycles!
            invariant_val = len(data) * config_factor
            total_sum_slow += data[i] + invariant_val + j
    slow_t = time.perf_counter() - start_t

    # --- Optimized Pattern: Hoisting invariant outside loop ---
    start_t = time.perf_counter()
    total_sum_fast = 0
    # Hoist invariant calculation outside the loop structure
    invariant_val_hoisted = len(data) * config_factor
    data_len = len(data)  # Hoisted attribute lookup
    
    for i in range(data_len):
        base_val = data[i] + invariant_val_hoisted
        for j in range(100):
            total_sum_fast += base_val + j
    fast_t = time.perf_counter() - start_t

    print(f"Total loop operations: {len(data) * 100:,} cycles")
    print(f"  Unhoisted Loop Invariant Time: {slow_t * 1000:.3f} ms")
    print(f"  Hoisted Loop Invariant Time:   {fast_t * 1000:.3f} ms")
    assert total_sum_slow == total_sum_fast


# ==============================================================================
# 3. REFACTORING PYRAMID OF DOOM WITH ITERTOOLS
# ==============================================================================
def demonstrate_itertools_refactoring() -> None:
    """Demonstrates flattening multi-nested loop pyramids using itertools.product."""
    header("3. Refactoring Deeply Nested Loops with itertools")
    
    colors = ["Red", "Green", "Blue"]
    sizes = ["S", "M", "L"]
    fabrics = ["Cotton", "Silk"]

    # --- Anti-Pattern: 3 Levels of Nested Loops ---
    print("Anti-Pattern: 3-Level Nested Loops")
    combinations_nested: List[Tuple[str, str, str]] = []
    for c in colors:
        for s in sizes:
            for f in fabrics:
                combinations_nested.append((c, s, f))

    print(f"  Generated {len(combinations_nested)} Cartesian combinations using 3 nested for loops.")

    # --- Pythonic Clean Pattern: itertools.product ---
    print("\nRefactored Pythonic Pattern: itertools.product()")
    combinations_itertools = list(itertools.product(colors, sizes, fabrics))
    
    print(f"  Generated {len(combinations_itertools)} combinations in a single clean expression.")
    print(f"  Sample generated SKU tuples: {combinations_itertools[:4]}")
    assert combinations_nested == combinations_itertools


# ==============================================================================
# MAIN EXECUTION ROUTINE
# ==============================================================================
def main() -> None:
    print("=" * 75)
    print("   DAY 9 - MODULE 04: NESTED LOOP OPTIMIZATION & ANTI-PATTERNS   ")
    print("=" * 75)
    
    demonstrate_list_vs_set_optimization()
    demonstrate_loop_invariant_hoisting()
    demonstrate_itertools_refactoring()


if __name__ == "__main__":
    main()
