# Minecraft AFK Bot - Complete Documentation

## Table of Contents
- [Minecraft AFK Bot - Complete Documentation](#minecraft-afk-bot---complete-documentation)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
    - [Key Features](#key-features)
  - [Project Structure](#project-structure)
    - [File Descriptions](#file-descriptions)
  - [Installation Guide](#installation-guide)
    - [Prerequisites](#prerequisites)
    - [Installation Steps](#installation-steps)
  - [Configuration Guide](#configuration-guide)
    - [AFK Detection Settings](#afk-detection-settings)
    - [Movement Settings](#movement-settings)
    - [Action Settings](#action-settings)
    - [Movement Keys](#movement-keys)
  - [Terminal Interface](#terminal-interface)
    - [Startup Sequence](#startup-sequence)
    - [Status Display](#status-display)
    - [Progress Tracking](#progress-tracking)
  - [Usage Guide](#usage-guide)
  - [Technical Details](#technical-details)
    - [How It Works](#how-it-works)
    - [Error Handling](#error-handling)
  - [Safety Features](#safety-features)
  - [Troubleshooting](#troubleshooting)
    - [Common Issues](#common-issues)
    - [Error Messages](#error-messages)
  - [Disclaimer](#disclaimer)

## Project Overview

The Minecraft AFK Bot is a Python-based automation tool designed to prevent players from being kicked from Minecraft servers due to inactivity. It achieves this by simulating human-like mouse movements and keyboard inputs.

### Key Features
- Random mouse movements to prevent AFK detection
- Random key presses for movement simulation
- Automatic right-click actions
- Teleportation commands
- Configurable settings
- Safety features and error handling

## Project Structure

```
minecraft-afk-bot/
├── bot.py              # Main bot implementation
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
├── README.md          # Quick start guide
└── DOCUMENTATION.md   # This file
```

### File Descriptions

1. **bot.py**
   - Main implementation of the AFK bot
   - Contains the `MinecraftAFKBot` class
   - Handles all automation logic and error handling

2. **config.py**
   - Contains all configurable settings
   - Easy to modify parameters without touching the main code
   - Includes timing, movement, and action settings

3. **requirements.txt**
   - Lists all required Python packages
   - Specifies exact versions for compatibility

## Installation Guide

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps
1. Clone or download the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Verify installation by running:
   ```bash
   python bot.py --version
   ```

## Configuration Guide

The `config.py` file contains all customizable settings:

### AFK Detection Settings
```python
AFK_THRESHOLD = 5      # Seconds before considering player AFK
CHECK_INTERVAL = 2     # Seconds between AFK checks
```

### Movement Settings
```python
NUM_COORDINATES = 1000           # Number of random coordinates
MOUSE_MOVE_DURATION = 0.5        # Mouse movement duration
KEY_PRESS_DURATION = 0.2         # Key press duration
SCREEN_SAFETY_MARGIN = 100       # Pixels from screen edges
```

### Action Settings
```python
RIGHT_CLICK_INTERVAL = 2000      # Mouse movements before right-click
RIGHT_CLICK_DURATION = 10        # Right-click hold duration
TELEPORT_INTERVAL = 2355         # Mouse movements before teleport
TELEPORT_COMMAND = "/home cactus" # Teleport command
```

### Movement Keys
```python
MOVEMENT_KEYS = ['z', 'q', 's', 'd', 'space']
```

## Terminal Interface

### Startup Sequence
1. **Animated Header**: Displays the bot's name with a typing animation
2. **Loading Animation**: Shows a spinning animation while initializing
3. **Countdown Timer**: 5-second countdown before bot activation
4. **Starting Animation**: Brief animation indicating bot startup
5. **Status Display**: Real-time counters and progress bars

### Status Display
The status display shows:
- **Food Counter**: Tracks right-click actions (0-2000)
- **TP Counter**: Tracks teleportation commands (0-2355)
- **Progress Bars**: Visual representation of progress
- **Percentages**: Precise progress tracking with 2 decimal places

Example status display:
```
Food [  45/2000] [███░░░░░░░░░░░]  2.25% | TP [  50/2355] [███░░░░░░░░░░░]  2.12%
```

### Progress Tracking
- Progress bars update in real-time
- Percentages calculated with 2 decimal precision
- Counters reset automatically at their respective intervals
- Status updates every 0.5 seconds for smooth display

## Usage Guide

1. **Preparation**
   - Open Minecraft
   - Position your character in a safe location
   - Ensure the game window is active

2. **Starting the Bot**
   ```bash
   python bot.py
   ```
   - A 5-second countdown will begin
   - Move mouse to top-left corner during countdown to abort

3. **During Operation**
   - Bot will automatically perform movements
   - Status updates will be printed to console
   - Press Ctrl+C to stop the bot

4. **Emergency Stop**
   - Move mouse to top-left corner of screen
   - Press Ctrl+C in the terminal

## Technical Details

### How It Works
1. **AFK Detection**
   - Monitors mouse position
   - Triggers actions after specified inactivity period

2. **Movement System**
   - Generates random coordinates within safe screen boundaries
   - Moves mouse smoothly between points
   - Simulates keyboard inputs for movement

3. **Action System**
   - Performs right-clicks at specified intervals
   - Executes teleport commands when needed
   - Maintains counters for various actions

### Error Handling
- Catches and reports exceptions
- Provides graceful shutdown
- Includes failsafe mechanism

## Safety Features

1. **Failsafe Mechanism**
   - Move mouse to top-left corner to stop
   - 5-second startup delay
   - Configurable safety margins

2. **Error Prevention**
   - Screen boundary checks
   - Input validation
   - Graceful error handling

3. **Customization**
   - Adjustable timing
   - Configurable movement patterns
   - Customizable commands

## Troubleshooting

### Common Issues

1. **Bot Not Starting**
   - Check Python version
   - Verify dependencies are installed
   - Ensure Minecraft window is active

2. **Mouse Movement Issues**
   - Adjust `SCREEN_SAFETY_MARGIN`
   - Check screen resolution
   - Verify game window position

3. **Performance Issues**
   - Increase `CHECK_INTERVAL`
   - Reduce `NUM_COORDINATES`
   - Adjust movement durations

### Error Messages
- "Module not found": Run `pip install -r requirements.txt`
- "Permission denied": Run as administrator
- "Screen not found": Check game window visibility

## Disclaimer

This bot is provided for educational purposes only. Using AFK bots may violate:
- Minecraft's Terms of Service
- Server rules and regulations
- Fair play principles

Use at your own risk. The developers are not responsible for any consequences resulting from the use of this software. 