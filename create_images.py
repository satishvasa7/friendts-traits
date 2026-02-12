"""
Generate placeholder images for friends
Run this script once to create placeholder images in static/images/
"""
from PIL import Image, ImageDraw, ImageFont
import os

# Create images directory if it doesn't exist
images_dir = 'static/images'
os.makedirs(images_dir, exist_ok=True)

friends = {
    "sasi": "#FF6B6B",
    "satish": "#4ECDC4",
    "rkn": "#FFE66D",
    "kalanwesh": "#95E1D3",
    "prakash": "#F38181",
    "maniratnam": "#AA96DA"
}

for friend, color in friends.items():
    # Create image with gradient-like solid color
    img = Image.new('RGB', (400, 300), color=color)
    draw = ImageDraw.Draw(img)
    
    # Try to use a larger font, fall back if not available
    try:
        font = ImageFont.truetype("arial.ttf", 80)
    except:
        font = ImageFont.load_default()
    
    # Draw the friend's name in the center
    text = friend.upper()
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (400 - text_width) // 2
    y = (300 - text_height) // 2
    
    draw.text((x, y), text, fill='white', font=font)
    
    # Save image
    filename = f'{images_dir}/{friend}.jpg'
    img.save(filename)
    print(f"✓ Created {filename}")

print("\n✅ All placeholder images created successfully!")
print("🖼️  Now you can run: python running.py")
