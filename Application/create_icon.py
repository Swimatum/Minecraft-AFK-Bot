from PIL import Image, ImageDraw

def create_icon():
    # Create a 256x256 image with a transparent background
    img = Image.new('RGBA', (256, 256), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw a simple Minecraft-style icon
    # Background
    draw.rectangle([(0, 0), (256, 256)], fill=(0, 0, 0, 0))
    
    # Main square
    draw.rectangle([(64, 64), (192, 192)], fill=(0, 100, 0, 255))
    
    # Inner square
    draw.rectangle([(96, 96), (160, 160)], fill=(0, 150, 0, 255))
    
    # Save as icon
    img.save('icon.ico', format='ICO', sizes=[(256, 256)])

if __name__ == '__main__':
    create_icon()
    print("Icon created successfully!") 