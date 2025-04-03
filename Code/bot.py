import pyautogui as pag
import time
import random
import keyboard
import sys
from config import *
from terminal_utils import TerminalUtils
from colorama import Fore, Style

class MinecraftAFKBot:
    def __init__(self):
        """Initialize the AFK bot."""
        # Initialize pyautogui with custom settings
        pag.FAILSAFE = False  # Disable the built-in failsafe
        pag.PAUSE = 0.1  # Add a small delay between actions
        
        # Initialize coordinates and position
        self.coordinates = self._generate_coordinates()
        self.current_position = pag.position()
        self.coord_index = 0
        
        # Initialize counters
        self.mouse_count = 0
        self.tp_count = 0
        self.afk_count = 0
        self.running = True
        self.terminal = TerminalUtils()
        self.failsafe_triggered = False
        self.header_shown = False
        self.last_status_update = 0
        self.status_update_interval = 0.5  # Update status every 0.5 seconds

    def _generate_coordinates(self):
        """Generate random coordinates within safe screen boundaries."""
        screen_width, screen_height = pag.size()
        return [
            (
                random.randint(SCREEN_SAFETY_MARGIN, screen_width - SCREEN_SAFETY_MARGIN),
                random.randint(SCREEN_SAFETY_MARGIN, screen_height - SCREEN_SAFETY_MARGIN)
            ) for _ in range(NUM_COORDINATES)
        ]

    def _check_afk(self):
        """Check if the player is AFK based on mouse movement."""
        current_pos = pag.position()
        if current_pos == self.current_position:
            self.afk_count += 1
        else:
            self.afk_count = 0
            self.current_position = current_pos
        return self.afk_count > AFK_THRESHOLD

    def _perform_mouse_movement(self):
        """Move mouse to next coordinate and update counters."""
        x, y = self.coordinates[self.coord_index]
        pag.moveTo(x, y, duration=MOUSE_MOVE_DURATION)
        self.current_position = pag.position()
        self.coord_index = (self.coord_index + 1) % len(self.coordinates)
        self.mouse_count += 1
        self.tp_count += 1
        time.sleep(PAUSE_BETWEEN_ACTIONS)

    def _perform_key_press(self):
        """Simulate a random movement key press."""
        random_key = random.choice(MOVEMENT_KEYS)
        keyboard.press(random_key)
        time.sleep(KEY_PRESS_DURATION)
        keyboard.release(random_key)
        time.sleep(PAUSE_BETWEEN_ACTIONS)

    def _perform_right_click(self):
        """Perform right-click action."""
        pag.mouseDown(button='right')
        time.sleep(RIGHT_CLICK_DURATION)
        pag.mouseUp(button='right')
        self.mouse_count = 0
        time.sleep(PAUSE_BETWEEN_ACTIONS)

    def _perform_teleport(self):
        """Execute teleport command."""
        pag.write(TELEPORT_COMMAND)
        keyboard.press('enter')
        self.tp_count = 0
        time.sleep(PAUSE_BETWEEN_ACTIONS)

    def _check_failsafe(self):
        """Check if failsafe is triggered (mouse in top-left corner)."""
        try:
            x, y = pag.position()
            return x == 0 and y == 0
        except:
            return False

    def run(self):
        """Run the AFK bot."""
        try:
            # Print header only once
            if not self.header_shown:
                self.terminal.clear_screen()
                self.terminal._print_animated_header()
                self.header_shown = True
            
            # Show loading animation
            self.terminal._loading_animation()
            
            # Countdown before starting
            self.terminal.countdown(5)
            
            # Clear screen and show header again with instructions
            self.terminal.clear_screen()
            self.terminal._print_animated_header()
            print(f"\n{Fore.YELLOW}To stop the bot:{Style.RESET_ALL}")
            print(f"- Move mouse to top-left corner")
            print(f"- Press {Fore.RED}Ctrl+C{Style.RESET_ALL}")
            print()  # Add extra line before status
            
            # Perform first actions before showing initial status
            self._perform_mouse_movement()
            self._perform_key_press()
            
            # Show initial status
            self._update_status()
            
            # Main loop
            while self.running:
                try:
                    # Check for failsafe
                    if self._check_failsafe():
                        self.running = False
                        self._graceful_shutdown()
                        break
                    
                    # Check if player is AFK
                    if self._check_afk():
                        # Perform random actions
                        self._perform_mouse_movement()
                        self._perform_key_press()
                        
                        # Check for right-click interval
                        if self.mouse_count % RIGHT_CLICK_INTERVAL == 0:
                            self._perform_right_click()
                        
                        # Check for teleport interval
                        if self.tp_count % TELEPORT_INTERVAL == 0:
                            self._perform_teleport()
                    
                    # Update status display
                    self._update_status()
                    
                    # Sleep for a short duration
                    time.sleep(0.1)
                    
                except KeyboardInterrupt:
                    self.running = False
                    self._graceful_shutdown()
                    break
                    
        except Exception as e:
            print(f"\n{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")
            self._graceful_shutdown()

    def _update_status(self):
        """Update the status display with current counters."""
        self.terminal.print_status(
            self.mouse_count,
            self.tp_count,
            self.afk_count,
            RIGHT_CLICK_INTERVAL,
            TELEPORT_INTERVAL,
            AFK_THRESHOLD
        )

    def _graceful_shutdown(self):
        """Perform a graceful shutdown with countdown."""
        try:
            # Clear the status line
            print("\r" + " " * 100, end="")
            
            # Show shutdown messages with delay
            messages = [
                f"{Fore.YELLOW}Shutting down bot...{Style.RESET_ALL}",
                f"{Fore.YELLOW}Please wait...{Style.RESET_ALL}",
                f"{Fore.YELLOW}Saving final status...{Style.RESET_ALL}",
                f"{Fore.YELLOW}Cleaning up...{Style.RESET_ALL}",
                f"{Fore.GREEN}Goodbye!{Style.RESET_ALL}"
            ]
            
            for msg in messages:
                print(f"\n{msg}")
                time.sleep(1)
            
            # Final countdown
            for i in range(3, 0, -1):
                print(f"\n{Fore.YELLOW}Closing in {i}...{Style.RESET_ALL}")
                time.sleep(1)
            
            # Clear screen one last time
            self.terminal.clear_screen()
            
        except Exception as e:
            print(f"\n{Fore.RED}Error during shutdown: {str(e)}{Style.RESET_ALL}")
        finally:
            sys.exit(0)

if __name__ == "__main__":
    try:
        bot = MinecraftAFKBot()
        bot.run()
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1) 
