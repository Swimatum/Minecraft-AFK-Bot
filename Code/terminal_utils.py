import time
import sys
import os
from colorama import init, Fore, Style
import pyautogui as pag
import itertools
import threading

# Initialize colorama
init()

class TerminalUtils:
    def __init__(self):
        self.last_status = ""
        self.header_lines = [
            "███╗   ███╗██╗███╗   ██╗███████╗██████╗  ██████╗ ██████╗ ███████╗████████╗",
            "████╗ ████║██║████╗  ██║██╔════╝██╔══██╗██╔═══██╗██╔══██╗██╔════╝╚══██╔══╝",
            "██╔████╔██║██║██╔██╗ ██║█████╗  ██████╔╝██║   ██║██████╔╝█████╗     ██║   ",
            "██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ██╔══██╗██║   ██║██╔══██╗██╔══╝     ██║   ",
            "██║ ╚═╝ ██║██║██║ ╚████║███████╗██║  ██║╚██████╔╝██║  ██║███████╗   ██║   ",
            "╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝   ╚═╝   "
        ]

    def _print_animated_header(self):
        """Print the header with a typing animation."""
        print()  # Initial newline
        for line in self.header_lines:
            sys.stdout.write(f"{Fore.CYAN}")
            for char in line:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.001)  # Very small delay for smooth animation
            sys.stdout.write(f"{Style.RESET_ALL}\n")
        print()  # Final newline

    def _loading_animation(self, duration=1):
        """Display a loading animation."""
        chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
        start_time = time.time()
        while time.time() - start_time < duration:
            for char in chars:
                sys.stdout.write(f'\r{Fore.CYAN}Loading {char}{Style.RESET_ALL}')
                sys.stdout.flush()
                time.sleep(0.1)
        sys.stdout.write('\r' + ' ' * 20 + '\r')
        sys.stdout.flush()

    def countdown(self, seconds=5):
        """Display a simple countdown."""
        print(f"{Fore.YELLOW}To stop the bot:{Style.RESET_ALL}")
        print(f"- Move mouse to top-left corner")
        print(f"- Press {Fore.RED}Ctrl+C{Style.RESET_ALL}")
        print()
        
        # Show loading animation
        self._loading_animation()
        
        for i in range(seconds, 0, -1):
            print(f"{Fore.YELLOW}Starting in {i}...{Style.RESET_ALL}")
            time.sleep(1)  # Back to 1 second for better readability
        print()  # Add extra line before bot started message
        
        # Show starting animation
        sys.stdout.write(f"{Fore.GREEN}Starting bot")
        for _ in range(3):
            time.sleep(0.2)
            sys.stdout.write(".")
            sys.stdout.flush()
        sys.stdout.write("\r" + " " * 20 + "\r")  # Clear the line
        print(f"{Fore.GREEN}Bot started!{Style.RESET_ALL}\n")  # Add newline after message

    def _check_failsafe(self):
        """Check if mouse is in top-left corner."""
        try:
            return pag.position() == (0, 0)
        except:
            return False

    def print_status(self, mouse_count, tp_count, afk_count, right_click_interval, teleport_interval, afk_threshold):
        """Print the current status with progress bars."""
        # Calculate progress percentages
        food_progress = min((mouse_count % right_click_interval) / right_click_interval * 100, 100)
        tp_progress = min((tp_count % teleport_interval) / teleport_interval * 100, 100)

        # Create progress bars
        food_bar = self._create_progress_bar(food_progress, Fore.CYAN)
        tp_bar = self._create_progress_bar(tp_progress, Fore.GREEN)

        # Clear previous status
        print("\r" + " " * 100, end="")
        
        # Print new status with improved formatting
        status = (
            f"\r{Fore.CYAN}Food [{mouse_count:>4}/2000] {food_bar} {food_progress:>6.2f}%{Style.RESET_ALL} | "
            f"{Fore.GREEN}TP [{tp_count:>4}/{teleport_interval:<4}] {tp_bar} {tp_progress:>6.2f}%{Style.RESET_ALL}"
        )
        
        print(status, end="")
        self.last_status = status

    def _create_progress_bar(self, progress, color):
        """Create a progress bar with the given progress percentage."""
        bar_length = 15  # Reduced length for better display
        filled_length = int(bar_length * progress / 100)
        bar = f"{color}{'█' * filled_length}{'░' * (bar_length - filled_length)}{Style.RESET_ALL}"
        return f"[{bar}]"  # Removed percentage for cleaner display

    def print_exit(self, failsafe=False):
        """Print exit message."""
        print("\n")
        box_width = 50
        if failsafe:
            message1 = "Bot stopped by failsafe!"
            message2 = "Mouse moved to top-left corner"
            padding1 = (box_width - len(message1)) // 2
            padding2 = (box_width - len(message2)) // 2
            print(f"{Fore.RED}┌{'─' * box_width}┐")
            print(f"│{' ' * padding1}{message1}{' ' * (box_width - len(message1) - padding1)}│")
            print(f"│{' ' * padding2}{message2}{' ' * (box_width - len(message2) - padding2)}│")
            print(f"└{'─' * box_width}┘{Style.RESET_ALL}")
        else:
            message = "Bot stopped successfully!"
            padding = (box_width - len(message)) // 2
            print(f"{Fore.GREEN}┌{'─' * box_width}┐")
            print(f"│{' ' * padding}{message}{' ' * (box_width - len(message) - padding)}│")
            print(f"└{'─' * box_width}┘{Style.RESET_ALL}")
        print()  # Add extra line before goodbye
        print(f"{Fore.CYAN}Goodbye! 👋{Style.RESET_ALL}\n")

    def clear_screen(self):
        """Clear the terminal screen."""
        try:
            # For Windows
            if os.name == 'nt':
                os.system('cls')
            # For Unix/Linux/MacOS
            else:
                os.system('clear')
        except:
            # Fallback if system call fails
            print("\n" * 100)  # Print 100 newlines to clear the screen 
