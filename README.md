# Minecraft AFK Bot

This repository contains a Python script for an AFK (Away From Keyboard) bot designed for Minecraft. The bot simulates player activity to prevent being kicked from servers due to inactivity.

## Features

- Moves the mouse cursor to random screen coordinates
- Simulates random key presses for basic Minecraft movements
- Performs right-click action periodically
- Executes a teleport command at regular intervals

## Requirements

- Python 3.6+
- pyautogui
- keyboard

## Installation

1. Clone this repository:

2. Install the required libraries:
git clone https://github.com/yourusername/minecraft-afk-bot.git
cd minecraft-afk-bot

2. Install the required libraries:
pip install pyautogui keyboard


## Usage

1. Start your Minecraft game and join a server.
2. Run the script:
python minecraft_afk_bot.py

3. Switch back to your Minecraft window.

The bot will start running and will continue until you forcibly stop the script (e.g., by pressing Ctrl+C in the terminal).

## How It Works

- The bot checks if the mouse cursor has been idle for more than 5 cycles (10 seconds).
- If idle, it moves the cursor to a random coordinate on the screen.
- It simulates random key presses (W, A, S, D, Space) to mimic player movement.
- Every 2000 cycles, it performs a right-click action for 10 seconds.
- Every 2355 cycles, it types and executes the command "/home cactus".

## Customization

You can modify the following variables in the script to adjust the bot's behavior:

- `movement_keys`: List of keys to simulate Minecraft movements
- `mouse`: Counter for right-click action (resets every 2000 cycles)
- `tp`: Counter for teleport command (resets every 2355 cycles)

## Important Notes

- This bot is designed for educational purposes and personal use only.
- Using bots or automated scripts may be against the rules of some Minecraft servers. Always check and comply with server rules.
- The script uses `pyautogui.FAILSAFE = False`, which disables the failsafe feature. Be cautious when using this setting.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the [issues page](https://github.com/yourusername/minecraft-afk-bot/issues) if you want to contribute.

## Disclaimer

This tool is for educational purposes only. The developers are not responsible for any misuse or damage caused by this program. Use at your own risk.
This README provides a comprehensive overview of your Minecraft AFK bot, including installation instructions, usage guide, explanation of how it works, customization options, and important notes about its use. Remember to replace "yourusername" with your actual GitHub username in the clone URL and issues page link.
