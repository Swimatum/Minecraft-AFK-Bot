import pyautogui as pag
import time
import random
import keyboard  # Requires the 'keyboard' library


pag.FAILSAFE = False


# Generate random coordinates within the screen dimensions
def generate_coordinates(num_points):
    screen_width, screen_height = pag.size()
    return [(random.randint(0, screen_width), random.randint(0, screen_height)) for _ in range(num_points)]


# Generate 1000 random coordinates
coordinates = generate_coordinates(1000)
curr_pos = pag.position()
afk_count = 0
coord_index = 0
mouse = 0
tp = 2340

# List of keys to simulate for Minecraft movements
movement_keys = ['z', 'q', 's', 'd', 'space']


while True:
    if pag.position() == curr_pos:
        afk_count += 1
    else:
        afk_count = 0
        curr_pos = pag.position()


    if afk_count > 5:
        # Move to the next coordinate in the list
        x, y = coordinates[coord_index]
        pag.moveTo(x, y, duration=0.5)
        curr_pos = pag.position()
        coord_index = (coord_index + 1) % len(coordinates)  # Loop back to the start


        # Simulate a random key press
        random_key = random.choice(movement_keys)
        keyboard.press(random_key)
        time.sleep(0.2)  # Hold the key for a short duration
        keyboard.release(random_key)
       
        mouse += 1
        tp += 1
        print(f'Mouse count: {mouse}\nTp count : {tp}')
       
        if mouse == 2000:
            pag.mouseDown(button='right')
            time.sleep(10)  # Hold the key for a short duration
            pag.mouseUp(button='right')
            mouse = 0

        if tp == 2355:
            pag.write('/home cactus')
            keyboard.press('enter')
            tp = 0


    print(f'Afk count: {afk_count}')
    time.sleep(2)

