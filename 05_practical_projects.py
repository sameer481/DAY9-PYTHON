"""
Day 9: Python While Loops & Nested Loops - Part 5
Topic: Production-Grade Projects Synthesizing While Loops and Nested Loops

This module provides 4 complete, fully interactive and automated real-world mini-applications:
1. ATM Banking CLI Simulator (Auth Retry Loop, Transaction Menu Event Loop).
2. Distributed Microservice Health Monitor (Nested Retries & Backoff Matrix).
3. 2D Grid Dungeon Crawler & Maze Engine (Nested Matrix Rendering & Movement Loop).
4. Streaming Log Parser & Anomaly Detection Pipeline (Sliding Window & Chunk Reader).
"""

import math
import random
import time
from typing import Dict, List, Optional, Tuple


def header(title: str) -> None:
    """Print a styled visual section header for terminal output formatting."""
    print("\n" + "=" * 75)
    print(f" {title.upper()} ")
    print("=" * 75)


# ==============================================================================
# PROJECT 1: ATM BANKING CLI SIMULATOR
# ==============================================================================
class ATMSimulator:
    """Simulates a secure ATM banking terminal using authentication retry and event loops."""
    
    def __init__(self, account_number: str, correct_pin: str, initial_balance: float):
        self.account_number = account_number
        self.correct_pin = correct_pin
        self.balance = initial_balance
        self.transaction_history: List[str] = []
        self.authenticated = False

    def authenticate(self, mock_inputs: List[str]) -> bool:
        """PIN validation loop with a maximum of 3 retry attempts."""
        max_attempts = 3
        attempts = 0
        input_idx = 0
        
        print("\n--- SECURE ATM LOGIN SYSTEM ---")
        while attempts < max_attempts:
            attempts += 1
            pin_entry = mock_inputs[input_idx] if input_idx < len(mock_inputs) else "0000"
            input_idx += 1
            
            print(f"  Attempt {attempts}/{max_attempts} -> Entered PIN: {'*' * len(pin_entry)}")
            if pin_entry == self.correct_pin:
                self.authenticated = True
                print("  [ACCESS GRANTED] PIN Verification Successful!")
                return True
            else:
                remaining = max_attempts - attempts
                print(f"  [ACCESS DENIED] Incorrect PIN! ({remaining} attempts remaining)")
                
        print("  [CARD LOCKED] Maximum security attempts exceeded. Account frozen.")
        return False

    def run_session(self, mock_menu_actions: List[Tuple[str, Optional[float]]]) -> None:
        """Main event loop managing user banking actions."""
        if not self.authenticated:
            print("  [ERROR] User unauthenticated. Cannot start banking session.")
            return

        print("\n--- STARTING BANKING SESSION ---")
        action_idx = 0

        while True:
            if action_idx >= len(mock_menu_actions):
                print("  [SESSION END] No further user commands. Logging out...")
                break

            choice, amount = mock_menu_actions[action_idx]
            action_idx += 1

            print(f"\nMenu Selection: Choice [{choice}]")
            
            if choice == "1":  # Balance Inquiry
                print(f"  [BALANCE] Current Available Balance: ${self.balance:,.2f}")

            elif choice == "2":  # Deposit
                if amount is not None and amount > 0:
                    self.balance += amount
                    record = f"Deposited ${amount:,.2f}"
                    self.transaction_history.append(record)
                    print(f"  [SUCCESS] {record}. New Balance: ${self.balance:,.2f}")
                else:
                    print("  [INVALID] Deposit amount must be positive.")

            elif choice == "3":  # Withdrawal
                if amount is not None and amount > 0:
                    if amount <= self.balance:
                        self.balance -= amount
                        record = f"Withdrew ${amount:,.2f}"
                        self.transaction_history.append(record)
                        print(f"  [SUCCESS] {record}. Remaining Balance: ${self.balance:,.2f}")
                    else:
                        print(f"  [INSUFFICIENT FUNDS] Cannot withdraw ${amount:,.2f}. Balance is ${self.balance:,.2f}.")
                else:
                    print("  [INVALID] Withdrawal amount must be positive.")

            elif choice == "4":  # Statement History
                print("  --- TRANSACTION HISTORY ---")
                if not self.transaction_history:
                    print("  No transactions performed in this session.")
                else:
                    for idx, tx in enumerate(self.transaction_history, 1):
                        print(f"    {idx}. {tx}")

            elif choice == "5":  # Exit
                print("  [LOGOUT] Thank you for banking with us. Ejecting card...")
                break
            else:
                print("  [ERROR] Invalid menu option selected. Please select 1-5.")


def run_project_1() -> None:
    header("Project 1: ATM Banking CLI Simulator")
    atm = ATMSimulator("ACC-88349", "4812", 2500.00)
    
    # 1. Simulate authentication (2 wrong inputs, 1 correct input)
    auth_success = atm.authenticate(["1111", "9999", "4812"])
    
    if auth_success:
        # 2. Simulate menu selections: Balance, Deposit $500, Withdraw $200, Statement, Exit
        actions = [
            ("1", None),          # Balance Check
            ("2", 500.00),        # Deposit
            ("3", 200.00),        # Withdraw
            ("3", 5000.00),       # Failed Withdrawal (Insufficient funds)
            ("4", None),          # History
            ("5", None)           # Exit
        ]
        atm.run_session(actions)


# ==============================================================================
# PROJECT 2: DISTRIBUTED MICROSERVICE HEALTH MONITOR
# ==============================================================================
def run_project_2() -> None:
    header("Project 2: Distributed Microservice Health Monitor")
    
    services = ["auth-service", "database-cluster", "payment-gateway", "cache-redis"]
    max_retries_per_service = 3
    base_backoff_ms = 100
    
    print("Initiating Multi-Service Health Audit Matrix...")
    service_status_matrix: Dict[str, str] = {}
    
    # Outer loop iterating through services
    service_idx = 0
    random.seed(101)  # Seed for reproducible mock network results

    while service_idx < len(services):
        service_name = services[service_idx]
        print(f"\n[AUDITING SERVICE] {service_name.upper()}")
        
        retry_count = 0
        service_healthy = False
        
        # Inner while loop attempting connection retries with backoff
        while retry_count < max_retries_per_service:
            retry_count += 1
            print(f"  Attempt #{retry_count} connecting to {service_name}...", end=" ")
            
            # Simulated ping (database fails twice then succeeds, payment-gateway always fails)
            if service_name == "payment-gateway":
                is_ok = False
            elif service_name == "database-cluster":
                is_ok = (retry_count >= 2)
            else:
                is_ok = True
                
            if is_ok:
                service_healthy = True
                print("-> [HEALTHY 200 OK]")
                break
            else:
                print("-> [UNHEALTHY 503 SERVICE UNAVAILABLE]")
                if retry_count < max_retries_per_service:
                    backoff = base_backoff_ms * (2 ** (retry_count - 1))
                    print(f"     Backoff delay {backoff}ms...")

        if service_healthy:
            service_status_matrix[service_name] = "ONLINE"
        else:
            service_status_matrix[service_name] = "CRITICAL_OFFLINE"

        service_idx += 1

    # Print Final Health Report Matrix using nested iteration
    print("\n" + "-" * 55)
    print("           FINAL SYSTEM HEALTH SUMMARY REPORT          ")
    print("-" * 55)
    print(f"{'SERVICE NAME':<25} | {'HEALTH STATUS':<18}")
    print("-" * 55)
    for name, status in service_status_matrix.items():
        flag = "[OK]" if status == "ONLINE" else "[FAIL]"
        print(f"{name:<25} | {flag} {status}")
    print("-" * 55)


# ==============================================================================
# PROJECT 3: 2D GRID DUNGEON CRAWLER & MAZE ENGINE
# ==============================================================================
class DungeonMaze:
    """2D Grid Game Engine demonstrating nested loops for rendering & while loop game loop."""
    
    def __init__(self, size: int):
        self.size = size
        self.player_pos = [0, 0]  # [row, col]
        self.exit_pos = [size - 1, size - 1]
        self.obstacles = {(1, 1), (2, 1), (0, 2)}
        self.game_over = False

    def render_grid(self) -> None:
        """Renders 2D dungeon matrix using nested loops."""
        print(f"\n--- DUNGEON GRID ({self.size}x{self.size}) ---")
        r = 0
        while r < self.size:
            row_str = ""
            c = 0
            while c < self.size:
                if [r, c] == self.player_pos:
                    row_str += " P "  # Player
                elif [r, c] == self.exit_pos:
                    row_str += " E "  # Exit Goal
                elif (r, c) in self.obstacles:
                    row_str += " # "  # Wall obstacle
                else:
                    row_str += " . "  # Empty floor
                c += 1
            print(f"  {row_str}")
            r += 1

    def move_player(self, direction: str) -> None:
        """Updates player position with boundary and collision checks."""
        dr, dc = 0, 0
        if direction == "UP": dr = -1
        elif direction == "DOWN": dr = 1
        elif direction == "LEFT": dc = -1
        elif direction == "RIGHT": dc = 1
        
        new_r = self.player_pos[0] + dr
        new_c = self.player_pos[1] + dc

        # Bounds Checking Loop Logic
        if 0 <= new_r < self.size and 0 <= new_c < self.size:
            if (new_r, new_c) in self.obstacles:
                print(f"  [COLLISION] Hit wall obstacle at ({new_r}, {new_c})! Move blocked.")
            else:
                self.player_pos = [new_r, new_c]
                print(f"  [MOVED] Player moved to position ({new_r}, {new_c}).")
        else:
            print("  [BOUNDS ERROR] Cannot move outside dungeon boundaries!")

        if self.player_pos == self.exit_pos:
            self.game_over = True
            print("\n  [VICTORY] You reached the Dungeon Exit (E)! Maze Cleared!")


def run_project_3() -> None:
    header("Project 3: 2D Grid Dungeon Crawler & Maze Engine")
    maze = DungeonMaze(4)
    
    # Pre-programmed movement moves sequence: DOWN, RIGHT, DOWN, DOWN, RIGHT, RIGHT
    moves = ["DOWN", "RIGHT", "DOWN", "DOWN", "RIGHT", "RIGHT"]
    move_pointer = 0

    maze.render_grid()
    print("\nStarting Maze Exploration Loop...")

    # Main Game Loop using while
    while not maze.game_over and move_pointer < len(moves):
        direction = moves[move_pointer]
        move_pointer += 1
        print(f"\nStep #{move_pointer}: Input Action -> {direction}")
        maze.move_player(direction)
        maze.render_grid()


# ==============================================================================
# PROJECT 4: STREAMING LOG PARSER & ANOMALY DETECTION PIPELINE
# ==============================================================================
def run_project_4() -> None:
    header("Project 4: Streaming Log Parser & Anomaly Detection Pipeline")
    
    # Simulated log stream lines
    mock_log_stream = [
        "2026-10-04 10:00:01 INFO UserLogin user_12",
        "2026-10-04 10:00:02 WARN FailedAuth IP=192.168.1.5",
        "2026-10-04 10:00:03 WARN FailedAuth IP=192.168.1.5",
        "2026-10-04 10:00:04 WARN FailedAuth IP=192.168.1.5",
        "2026-10-04 10:00:05 CRITICAL RateLimitExceeded IP=192.168.1.5",
        "2026-10-04 10:00:06 INFO UserLogout user_12",
        "EOF"
    ]

    log_idx = 0
    warning_counter = 0
    anomaly_threshold = 3
    window: List[str] = []

    print("Reading log stream chunks with while loop & sliding anomaly detector...\n")
    
    while log_idx < len(mock_log_stream):
        line = mock_log_stream[log_idx]
        log_idx += 1
        
        if line == "EOF":
            print("  [STREAM END] EOF Sentinel detected. Flushing pipeline buffer.")
            break
            
        print(f"  [STREAM CHUNK] {line}")
        
        if "WARN FailedAuth" in line:
            warning_counter += 1
            window.append(line)
            if warning_counter >= anomaly_threshold:
                print(f"     >>> [SECURITY ANOMALY DETECTED] {warning_counter} Consecutive Failed Auth Attempts! Blocked IP! <<<")
        else:
            # Reset window counter on normal traffic line
            warning_counter = 0
            window.clear()

    print("\nLog Parsing Pipeline Complete.")


# ==============================================================================
# MAIN EXECUTION ROUTINE
# ==============================================================================
def main() -> None:
    print("=" * 75)
    print("   DAY 9 - MODULE 05: PRACTICAL PRODUCTION PROJECTS   ")
    print("=" * 75)
    
    run_project_1()
    run_project_2()
    run_project_3()
    run_project_4()


if __name__ == "__main__":
    main()
