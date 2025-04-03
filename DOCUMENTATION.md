# Minecraft AFK Bot - Complete Documentation

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Technical Details](#technical-details)
- [Building the Executable](#building-the-executable)
- [Troubleshooting](#troubleshooting)
- [Safety Features](#safety-features)
- [Disclaimer](#disclaimer)

## Project Overview

The Minecraft AFK Bot is a Python-based automation tool designed to prevent players from being kicked from Minecraft servers due to inactivity. It achieves this by simulating human-like mouse movements and keyboard inputs.

### Features
- Random mouse movements with configurable patterns
- Random key presses for movement simulation
- Automatic right-click actions at specified intervals
- Teleportation commands at specified intervals
- Beautiful terminal interface with animations
- Real-time status display with progress bars
- Graceful shutdown sequence
- Failsafe mechanism

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps
1. Clone or download the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

The `config.py` file contains all customizable settings:

### Movement Settings
```python
NUM_COORDINATES = 1000           # Number of random coordinates
MOUSE_MOVE_DURATION = 0.5        # Mouse movement duration
KEY_PRESS_DURATION = 0.2         # Key press duration
SCREEN_SAFETY_MARGIN = 100       # Pixels from screen edges
```

### Action Settings
```python
RIGHT_CLICK_INTERVAL = 2000      # Right-click every 2000 actions
TELEPORT_INTERVAL = 2355         # Teleport every 2355 actions
AFK_THRESHOLD = 5               # Seconds before considering player AFK
CHECK_INTERVAL = 2              # Seconds between AFK checks
```

### Movement Keys
```python
MOVEMENT_KEYS = ['z', 'q', 's', 'd', 'space']
```

## Usage

### Starting the Bot
1. Open Minecraft and position your character
2. Run the bot:
   ```bash
   python bot.py
   ```

### Interface Elements
1. **Animated Header**: Shows the bot name with typing animation
2. **Loading Animation**: Spinning animation during initialization
3. **Countdown**: 5-second countdown before bot activation
4. **Status Display**:
   - Food counter (0-2000)
   - TP counter (0-2355)
   - Progress bars
   - Precise percentages (2 decimal places)
5. **Stop Instructions**: Clear display of how to stop the bot

### Stopping the Bot
1. Move mouse to top-left corner (failsafe)
2. Press Ctrl+C
3. The bot will show a graceful shutdown sequence

## Technical Details

### How It Works
1. **AFK Detection**: Checks mouse position every 2 seconds
2. **Mouse Movement**: Moves to random coordinates when AFK is detected
3. **Key Presses**: Simulates random movement keys
4. **Right-Click**: Performs right-click every 2000 actions
5. **Teleportation**: Executes teleport command every 2355 actions

### Error Handling
- Try-catch blocks around all critical operations
- Graceful shutdown on errors
- Console window for error visibility
- Status update throttling (every 0.5 seconds)

## Building the Executable

### Requirements
- PyInstaller
- All project dependencies

### Build Process
1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Run the build script:
   ```bash
   python build.py
   ```

3. The executable will be created in the `dist` folder

### Executable Features
- Single file distribution
- Console window for error visibility
- Custom icon
- Includes all dependencies
- Graceful shutdown sequence

## Troubleshooting

### Common Issues
1. **Bot not starting**:
   - Check Python version
   - Verify all dependencies are installed
   - Run as administrator if needed

2. **Mouse not moving**:
   - Check screen resolution
   - Verify Minecraft window is active
   - Check failsafe is not triggered

3. **Status not updating**:
   - Check console window is visible
   - Verify terminal supports ANSI colors
   - Check for error messages

## Safety Features

1. **Failsafe Mechanism**:
   - Move mouse to top-left corner to stop
   - Immediate shutdown when triggered
   - Visual confirmation of shutdown

2. **Error Recovery**:
   - Automatic retry on failed actions
   - Graceful shutdown on critical errors
   - Status preservation during errors

3. **Resource Management**:
   - Efficient status updates
   - Proper cleanup on exit
   - Memory leak prevention

## Disclaimer

This bot is for educational purposes only. Using AFK bots may violate server rules. Use at your own risk. 
