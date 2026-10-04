"""
Day 9: Python While Loops & Nested Loops - Part 1
Topic: While Loop Fundamentals, Sentinel Control, Loop Mechanics & while-else Syntax

A 'while' loop in Python implements indefinite iteration. It repeatedly executes a block
of statements as long as a test expression (condition) evaluates to True.

Key Mechanics Covered:
1. Basic while loop structure and state counter updates.
2. Sentinel-controlled loops and interactive condition state machines.
3. The 'while...else' clause and natural termination vs. forced break.
4. Controlled infinite loops ('while True') with timeout safety guards.
5. User input validation and retry loops.
"""

from typing import List, Optional


def header(title: str) -> None:
    """Print a styled visual section header for terminal output formatting."""
    print("\n" + "=" * 75)
    print(f" {title.upper()} ")
    print("=" * 75)


# ==============================================================================
# 1. BASIC WHILE LOOP MECHANICS & STATE UPDATE
# ==============================================================================
def demonstrate_basic_while_loop() -> None:
    """Demonstrates basic while loop iteration, step increments, and bounds checking."""
    header("1. Basic While Loop Mechanics & State Variables")
    
    # Simple increment counter
    counter = 1
    max_count = 5
    
    print(f"Starting increment loop (Target: {max_count}):")
    while counter <= max_count:
        print(f"  Iteration {counter}: Loop condition ({counter} <= {max_count}) is True")
        counter += 1  # Crucial state update to prevent infinite looping
        
    print(f"Loop exited! Final counter value: {counter}")
    
    # Decrement step loop
    countdown = 10
    print("\nCountdown sequence with step decrement:")
    while countdown > 0:
        print(f"  T-minus {countdown} seconds...", end=" ")
        countdown -= 2  # Decrementing by 2
    print("\n  [LAUNCH] Ignition & Liftoff!")


# ==============================================================================
# 2. SENTINEL-CONTROLLED LOOPS & STATE FLAGS
# ==============================================================================
def demonstrate_sentinel_loops() -> None:
    """Demonstrates sentinel value checking for stream reading and state control."""
    header("2. Sentinel-Controlled Loops & State Flags")
    
    # Simulated stream data with a sentinel termination flag ("END")
    data_stream = ["PACKET_001", "PACKET_002", "PACKET_003", "END", "PACKET_004"]
    stream_idx = 0
    sentinel = "END"
    processed_packets: List[str] = []
    
    print(f"Processing stream until sentinel value '{sentinel}' is encountered...")
    while stream_idx < len(data_stream) and data_stream[stream_idx] != sentinel:
        current_packet = data_stream[stream_idx]
        print(f"  [ACCEPTED] Processing {current_packet}")
        processed_packets.append(current_packet)
        stream_idx += 1
        
    print(f"\nSentinel value reached or stream ended. Processed {len(processed_packets)} packets.")
    print(f"Unprocessed remaining stream elements: {data_stream[stream_idx:]}")


# ==============================================================================
# 3. WHILE-ELSE CLAUSE MECHANICS
# ==============================================================================
def demonstrate_while_else() -> None:
    """
    Demonstrates the Python-exclusive 'while...else' clause.
    - 'else' block executes ONLY IF the while condition becomes False naturally.
    - 'else' block IS SKIPPED if the loop exits via a 'break' statement.
    """
    header("3. Python 'while...else' Construct Mechanics")
    
    def search_target(numbers: List[int], target: int) -> None:
        idx = 0
        print(f"\nSearching for target {target} in dataset: {numbers}")
        while idx < len(numbers):
            if numbers[idx] == target:
                print(f"  [FOUND] Target {target} found at index {idx}! Executing 'break'...")
                break  # Bypasses the loop's 'else' clause
            idx += 1
        else:
            # Executes only if loop finished naturally without hitting break
            print(f"  [NOT FOUND] Target {target} NOT found in entire list! 'else' block executed.")

    search_target([12, 45, 67, 89, 23], 67)  # Target present -> break triggered -> else skipped
    search_target([12, 45, 67, 89, 23], 99)  # Target absent -> condition False -> else executed


# ==============================================================================
# 4. CONTROLLED INFINITE LOOPS & SAFETY TIMEOUT GUARDS
# ==============================================================================
def demonstrate_controlled_infinite_loops() -> None:
    """Demonstrates 'while True' event loops paired with conditional break & safety guards."""
    header("4. Controlled Infinite Loops ('while True') & Safety Guards")
    
    buffer_size = 0
    max_capacity = 100
    iteration_guard = 0
    max_safe_iterations = 1000  # Defensive programming against runaway loops
    
    print("Simulating event buffer filling...")
    while True:
        iteration_guard += 1
        if iteration_guard > max_safe_iterations:
            print("  [ALERT] SAFETY EMERGENCY BRAKE: Iteration guard threshold exceeded!")
            break
            
        buffer_size += 25
        print(f"  Buffer fill step {iteration_guard}: Capacity at {buffer_size}/{max_capacity}")
        
        if buffer_size >= max_capacity:
            print("  [TARGET REACHED] Maximum capacity reached. Emitting break signal.")
            break


# ==============================================================================
# 5. USER INPUT VALIDATION & RETRY SIMULATION
# ==============================================================================
def demonstrate_input_validation_loop() -> None:
    """Simulates robust input validation loop with error handling and attempt limits."""
    header("5. Simulated Input Validation & Retry Loop")
    
    # Mock user input sequence (simulating user typing invalid inputs then a valid one)
    mock_user_inputs = ["invalid_age", "-5", "150", "28"]
    input_pointer = 0
    valid_age: Optional[int] = None
    max_attempts = 5
    attempts = 0

    print("Simulating age validation input loop (Valid range: 18 - 120):")
    while attempts < max_attempts:
        attempts += 1
        raw_input = mock_user_inputs[input_pointer]
        input_pointer = (input_pointer + 1) % len(mock_user_inputs)
        print(f"\nAttempt #{attempts} -> User Input: '{raw_input}'")

        try:
            val = int(raw_input)
            if 18 <= val <= 120:
                valid_age = val
                print(f"  [OK] Input valid! Age accepted: {valid_age}")
                break
            else:
                print(f"  [ERROR] Out of range: {val} is not between 18 and 120.")
        except ValueError:
            print(f"  [ERROR] Type error: '{raw_input}' is not a valid integer.")

    if valid_age is not None:
        print(f"\nRegistration Successful! Confirmed Age: {valid_age}")
    else:
        print("\nRegistration Failed! Maximum validation attempts exceeded.")


# ==============================================================================
# MAIN EXECUTION ROUTINE
# ==============================================================================
def main() -> None:
    print("=" * 75)
    print("   DAY 9 - MODULE 01: WHILE LOOP FUNDAMENTALS & SYNTAX MECHANICS   ")
    print("=" * 75)
    
    demonstrate_basic_while_loop()
    demonstrate_sentinel_loops()
    demonstrate_while_else()
    demonstrate_controlled_infinite_loops()
    demonstrate_input_validation_loop()


if __name__ == "__main__":
    main()
