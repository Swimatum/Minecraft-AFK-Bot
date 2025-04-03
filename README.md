# Minecraft AFK Bot

A Python-based AFK bot for Minecraft that helps prevent being kicked from servers due to inactivity.

## Features

- Random mouse movements to prevent AFK detection
- Random key presses for movement simulation
- Automatic right-click actions
- Teleportation commands
- Configurable settings
- Beautiful terminal interface with:
  - Animated header
  - Real-time status display with progress bars
  - Precise percentage tracking (2 decimal places)
  - Loading animations
  - Countdown timer

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

## Usage

1. Open Minecraft and position your character
2. Run the bot:
   ```bash
   python bot.py
   ```
3. The bot will show:
   - An animated header
   - Loading animation
   - Countdown timer
   - Real-time status display with:
     - Food counter (0-2000)
     - TP counter (0-2355)
     - Progress bars and percentages
4. To stop the bot:
   - Move mouse to top-left corner (failsafe)
   - Press Ctrl+C

## Safety Features

- Failsafe enabled (move mouse to top-left corner to stop)
- Configurable movement patterns
- Error handling for common issues
- Smooth animations and status updates

## Disclaimer

This bot is for educational purposes only. Using AFK bots may violate server rules. Use at your own risk. 