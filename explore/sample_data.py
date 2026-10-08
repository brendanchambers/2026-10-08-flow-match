import random
from pathlib import Path
import matplotlib.pyplot as plt
from PIL import Image

png_dir = "/Users/bc/bcdata_warm/library/respectful_mirror/visual_poetry"

# Get all PNG files
png_files = list(Path(png_dir).glob("*.png"))
print(f"Found {len(png_files)} PNG files")

# Load random entry
random_file = random.choice(png_files)
print(f"Loading: {random_file.name}")

img = Image.open(random_file)
print(f"Image size: {img.size}, mode: {img.mode}")

# Visualize
plt.figure(figsize=(8, 8))
plt.imshow(img)
plt.axis("off")
plt.title(random_file.name)
plt.tight_layout()
plt.show()