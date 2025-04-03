import PyInstaller.__main__
import os
import shutil
import sys
import site

def build_executable():
    # Clean previous build
    if os.path.exists('build'):
        shutil.rmtree('build')
    if os.path.exists('dist'):
        shutil.rmtree('dist')
    
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Get site-packages directory
    site_packages = site.getsitepackages()[0]
    
    # PyInstaller options
    options = [
        'bot.py',  # Main script
        '--name=MinecraftAFKBot',  # Name of the executable
        '--onefile',  # Create a single executable
        '--console',  # Use console mode to see errors
        '--icon=icon.ico',  # Icon file
        '--add-data=README.md;.',  # Include README
        '--add-data=DOCUMENTATION.md;.',  # Include documentation
        '--add-data=config.py;.',  # Include config file
        '--clean',  # Clean PyInstaller cache
        '--noconfirm',  # Replace output directory without asking
        '--hidden-import=pyautogui',  # Explicitly include pyautogui
        '--hidden-import=keyboard',  # Explicitly include keyboard
        '--hidden-import=colorama',  # Explicitly include colorama
        '--hidden-import=terminal_utils',  # Explicitly include terminal_utils
        '--hidden-import=pynput',  # Include pynput for keyboard
        '--hidden-import=pynput.keyboard',  # Include pynput.keyboard
        '--hidden-import=pynput.mouse',  # Include pynput.mouse
        '--hidden-import=win32api',  # Include win32api for Windows
        '--hidden-import=win32con',  # Include win32con for Windows
        '--hidden-import=win32gui',  # Include win32gui for Windows
        '--log-level=DEBUG',  # Enable debug logging
    ]
    
    # Add data files for Windows
    if sys.platform == 'win32':
        # Get the actual paths of the modules
        pyautogui_path = os.path.join(site_packages, 'pyautogui')
        keyboard_path = os.path.join(site_packages, 'keyboard')
        pynput_path = os.path.join(site_packages, 'pynput')
        
        if os.path.exists(pyautogui_path):
            options.extend([
                f'--add-data={pyautogui_path};pyautogui',
            ])
        if os.path.exists(keyboard_path):
            options.extend([
                f'--add-data={keyboard_path};keyboard',
            ])
        if os.path.exists(pynput_path):
            options.extend([
                f'--add-data={pynput_path};pynput',
            ])
    
    try:
        # Run PyInstaller
        PyInstaller.__main__.run(options)
        print("\nBuild successful! The executable can be found in the 'dist' folder.")
        
        # Additional Windows-specific steps
        if sys.platform == 'win32':
            print("\nWindows-specific post-build steps:")
            print("1. Run the executable by double-clicking it")
            print("2. If you get a Windows Defender warning, add an exception for the executable")
            print("3. The console window will show any errors that occur")
            print("4. To stop the bot, close the console window or press Ctrl+C")
    except Exception as e:
        print(f"\nError during build: {str(e)}")
        print("Please make sure all dependencies are installed and try again.")

if __name__ == '__main__':
    print("Building Minecraft AFK Bot executable...")
    build_executable() 
