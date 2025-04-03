# Minecraft AFK Bot

A Python-based AFK bot for Minecraft that helps prevent being kicked from servers due to inactivity.

## Features

- Random mouse movements to prevent AFK detection
- Random key presses for movement simulation
- Automatic right-click actions
- Teleportation commands
- Configurable settings
- Beautiful terminal interface with:
  - Animated header with typing effect
  - Real-time status display with progress bars
  - Precise percentage tracking (2 decimal places)
  - Loading animations
  - Countdown timer
  - Clear stop instructions
  - Graceful shutdown sequence

## Installation

1. Install Python 3.8 or higher
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Edit the `config.py` file to customize:
- Movement patterns
- AFK detection timing
- Teleportation commands
- Mouse movement frequency
- Right-click interval (default: 2000)
- Teleport interval (default: 2355)

## Usage

1. Open Minecraft and position your character
2. Run the bot:
   ```bash
   python bot.py
   ```
3. The bot will show:
   - An animated header with typing effect
   - Loading animation
   - 5-second countdown
   - Clear stop instructions
   - Real-time status display with:
     - Food counter (0-2000)
     - TP counter (0-2355)
     - Progress bars and precise percentages
   - Status updates every 0.5 seconds

4. To stop the bot:
   - Move mouse to top-left corner (failsafe)
   - Press Ctrl+C
   - The bot will show a graceful shutdown sequence with countdown

## Safety Features

- Failsafe enabled (move mouse to top-left corner to stop)
- Configurable movement patterns
- Error handling for common issues
- Smooth animations and status updates
- Graceful shutdown with 3-second countdown
- Console window for error visibility
- Proper cleanup on exit

## Building the Executable

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Run the build script:
   ```bash
   python build.py
   ```

3. The executable will be created in the `dist` folder

## Disclaimer

This bot is for educational purposes only. Using AFK bots may violate server rules. Use at your own risk. 
