import pyautogui as pag
import time
import random
import keyboard
import sys
from config import *
from terminal_utils import TerminalUtils

class MinecraftAFKBot:
    def __init__(self):
        self.coordinates = self._generate_coordinates()
        self.current_position = pag.position()
        self.afk_count = 0
        self.coord_index = 0
        self.mouse_count = 0
        self.tp_count = 0
        self.running = True
        self.terminal = TerminalUtils()
        self.failsafe_triggered = False

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

    def run(self):
        """Main bot loop."""
        # Enable failsafe (move mouse to top-left corner to stop)
        pag.FAILSAFE = True
        
        try:
            # Show startup sequence
            self.terminal.countdown(5)
            
            # Set initial AFK count to 5
            self.afk_count = 5
            
            # Display initial status with 0 counters but AFK at 5
            self.terminal.print_status(
                0,              # Start at 0/2000
                0,              # Start at 0/2355
                self.afk_count, # Start at 5
                RIGHT_CLICK_INTERVAL,
                TELEPORT_INTERVAL,
                AFK_THRESHOLD
            )
            
            # Perform first actions immediately after showing counters
            self._perform_mouse_movement()
            self._perform_key_press()
            
            # Update display to show the increment to 1
            self.terminal.print_status(
                self.mouse_count,  # Now at 1/2000
                self.tp_count,     # Now at 1/2355
                self.afk_count,
                RIGHT_CLICK_INTERVAL,
                TELEPORT_INTERVAL,
                AFK_THRESHOLD
            )
            
            while self.running:
                if self._check_afk():
                    self._perform_mouse_movement()
                    self._perform_key_press()
                    
                    if self.mouse_count >= RIGHT_CLICK_INTERVAL:
                        self._perform_right_click()
                    
                    if self.tp_count >= TELEPORT_INTERVAL:
                        self._perform_teleport()
                    
                    # Update status display with required parameters
                    self.terminal.print_status(
                        self.mouse_count,
                        self.tp_count,
                        self.afk_count,
                        RIGHT_CLICK_INTERVAL,
                        TELEPORT_INTERVAL,
                        AFK_THRESHOLD
                    )
                
                time.sleep(CHECK_INTERVAL)
                
        except KeyboardInterrupt:
            self.terminal.print_exit(failsafe=False)
        except pag.FailSafeException:
            self.failsafe_triggered = True
            self.terminal.print_exit(failsafe=True)
        except Exception as e:
            print(f"\nError: {e}")
        finally:
            self.running = False

if __name__ == "__main__":
    try:
        bot = MinecraftAFKBot()
        bot.run()
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1) 
