"""
Day 9: Python While Loops & Nested Loops - Part 3
Topic: Advanced Algorithmic Patterns Using While Loops & Retries with Backoff

While loops are the core building block for dynamic algorithmic patterns where loop bounds
are calculated on the fly rather than known upfront.

Key Patterns Covered:
1. Two-Pointer Technique (Palindrome Verification, Array Reversal, Container with Most Water).
2. Sliding Window Pattern (Variable Window Expansion & Shrinking with While Loops).
3. Binary Search Algorithm (Logarithmic O(log N) Space Halving Loop).
4. Mathematical Trajectory & Euclidean Algorithms (GCD & Collatz Conjecture).
5. State Machine Retry Engine with Exponential Backoff & Jitter Simulation.
"""

import math
import random
from typing import List, Tuple


def header(title: str) -> None:
    """Print a styled visual section header for terminal output formatting."""
    print("\n" + "=" * 75)
    print(f" {title.upper()} ")
    print("=" * 75)


# ==============================================================================
# 1. TWO-POINTER TECHNIQUE USING WHILE LOOPS
# ==============================================================================
def demonstrate_two_pointer_technique() -> None:
    """Demonstrates Two-Pointer convergence pattern (Left & Right pointers moving inwards)."""
    header("1. Two-Pointer Converging Pattern (O(N) Traversal)")
    
    # Example A: Palindrome Verification
    def is_palindrome(text: str) -> bool:
        clean_text = "".join(ch.lower() for ch in text if ch.isalnum())
        left = 0
        right = len(clean_text) - 1
        
        while left < right:
            if clean_text[left] != clean_text[right]:
                return False
            left += 1
            right -= 1
        return True

    test_phrases = [
        "A man, a plan, a canal: Panama!",
        "Race a car",
        "Was it a car or a cat I saw?"
    ]
    
    print("Palindrome Verification:")
    for phrase in test_phrases:
        result = is_palindrome(phrase)
        status = "[YES]" if result else "[NO]"
        print(f"  {status:<7} '{phrase}'")

    # Example B: Container With Most Water (Greedy Two-Pointer)
    def max_water_area(heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0
        
        while left < right:
            width = right - left
            current_height = min(heights[left], heights[right])
            area = width * current_height
            max_area = max(max_area, area)
            
            # Move the pointer pointing to the shorter vertical bar
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                
        return max_area

    bars = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"\nContainer With Most Water Heights: {bars}")
    print(f"  Maximum Water Capacity: {max_water_area(bars)} units")


# ==============================================================================
# 2. SLIDING WINDOW PATTERN USING WHILE LOOPS
# ==============================================================================
def demonstrate_sliding_window() -> None:
    """Demonstrates dynamic sliding window pattern (Expanding & Shrinking window bounds)."""
    header("2. Dynamic Sliding Window Pattern (Variable Window Shrinking)")
    
    def min_subarray_len_with_sum(target_sum: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_len = float("inf")
        
        right = 0
        while right < len(nums):
            current_sum += nums[right]
            
            # Shrink window from left as long as target_sum condition is met
            while current_sum >= target_sum:
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len
                current_sum -= nums[left]
                left += 1  # Shrink window left edge
                
            right += 1  # Expand window right edge

        return int(min_len) if min_len != float("inf") else 0

    dataset = [2, 3, 1, 2, 4, 3]
    target = 7
    result_len = min_subarray_len_with_sum(target, dataset)
    print(f"Dataset: {dataset} | Target Minimum Sum: {target}")
    print(f"  Minimum Subarray Length satisfying condition: {result_len}")


# ==============================================================================
# 3. BINARY SEARCH ALGORITHM USING WHILE LOOPS
# ==============================================================================
def demonstrate_binary_search() -> None:
    """Demonstrates Binary Search log(N) search space halving loop."""
    header("3. Binary Search Algorithm (O(log N) Search Halving)")
    
    sorted_data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91, 104, 150]
    target = 56
    
    left = 0
    right = len(sorted_data) - 1
    step_count = 0
    found_index = -1

    print(f"Sorted Dataset ({len(sorted_data)} elements): {sorted_data}")
    print(f"Target Search Value: {target}\n")

    while left <= right:
        step_count += 1
        mid = left + (right - left) // 2
        mid_val = sorted_data[mid]
        print(f"  Step {step_count}: Low={left}, High={right}, MidIndex={mid} -> Value={mid_val}")

        if mid_val == target:
            found_index = mid
            break
        elif mid_val < target:
            left = mid + 1  # Target is in right half
        else:
            right = mid - 1  # Target is in left half

    if found_index != -1:
        print(f"\n  [FOUND] Target {target} located at Index {found_index} in {step_count} binary steps!")
    else:
        print(f"\n  [NOT FOUND] Target {target} is not present in the list.")


# ==============================================================================
# 4. MATHEMATICAL TRAJECTORY & EUCLIDEAN GCD LOOPS
# ==============================================================================
def demonstrate_math_algorithms() -> None:
    """Demonstrates Euclid's GCD algorithm and Collatz conjecture simulation."""
    header("4. Mathematical Trajectory & Euclidean GCD Algorithm")
    
    # Euclid's Algorithm for Greatest Common Divisor
    def euclidean_gcd(a: int, b: int) -> Tuple[int, List[Tuple[int, int]]]:
        steps = []
        x, y = a, b
        while y != 0:
            steps.append((x, y))
            x, y = y, x % y
        return x, steps

    num1, num2 = 252, 105
    gcd_val, history = euclidean_gcd(num1, num2)
    print(f"Euclid's GCD({num1}, {num2}):")
    for step_num, (curr_a, curr_b) in enumerate(history, 1):
        print(f"  Step {step_num}: {curr_a} % {curr_b} = {curr_a % curr_b}")
    print(f"  Resulting Greatest Common Divisor (GCD): {gcd_val}")

    # Collatz Conjecture Simulation
    def collatz_sequence(n: int) -> List[int]:
        seq = [n]
        while n > 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            seq.append(n)
        return seq

    start_val = 13
    trajectory = collatz_sequence(start_val)
    print(f"\nCollatz Conjecture Trajectory starting at n = {start_val}:")
    print(f"  Steps Count: {len(trajectory) - 1}")
    print(f"  Sequence: {trajectory}")


# ==============================================================================
# 5. RETRY ENGINE WITH EXPONENTIAL BACKOFF & JITTER
# ==============================================================================
def demonstrate_retry_backoff_engine() -> None:
    """Simulates exponential backoff retry loop for network connections."""
    header("5. Network Retry Loop with Exponential Backoff & Jitter")
    
    max_retries = 4
    base_delay_sec = 0.5
    backoff_factor = 2.0
    
    attempt = 0
    success = False
    random.seed(42)  # Deterministic seed for demonstration output

    print("Initiating Remote Connection Attempt Sequence...")
    while attempt < max_retries and not success:
        attempt += 1
        print(f"\n  [ATTEMPT #{attempt}/{max_retries}] Connecting to remote endpoint...")
        
        # Simulate network failure on first 3 attempts, success on 4th
        simulated_result = (attempt == 3)  # Succeeds on attempt 3
        
        if simulated_result:
            success = True
            print(f"  [SUCCESS] Connection Established on Attempt #{attempt}!")
            break
        else:
            print(f"  [FAILED] Connection refused / timed out.")
            if attempt < max_retries:
                delay = base_delay_sec * (backoff_factor ** (attempt - 1))
                jitter = random.uniform(0, 0.1)
                total_delay = delay + jitter
                print(f"  [BACKOFF] Waiting {total_delay:.3f}s before next attempt...")


# ==============================================================================
# MAIN EXECUTION ROUTINE
# ==============================================================================
def main() -> None:
    print("=" * 75)
    print("   DAY 9 - MODULE 03: ADVANCED WHILE LOOP PATTERNS & ALGORITHMS   ")
    print("=" * 75)
    
    demonstrate_two_pointer_technique()
    demonstrate_sliding_window()
    demonstrate_binary_search()
    demonstrate_math_algorithms()
    demonstrate_retry_backoff_engine()


if __name__ == "__main__":
    main()
