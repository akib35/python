import sys
import os
from PIL import Image

given_dir = sys.argv[1]
new_dir = sys.argv[2]

os.chdir(os.path.dirname(os.path.abspath(__file__)))

if not os.path.exists(new_dir):
    os.mkdir(new_dir)

for filename in os.listdir(given_dir):
    img = Image.open(f'{given_dir}{filename}')
    img.save(f'{new_dir}{os.path.splitext(filename)[0]}.png', 'png')
