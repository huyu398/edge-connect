import os
import argparse
import numpy as np
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument('--size', type=int, help='value of resize')
parser.add_argument('--path', type=str, help='path to the dataset')
parser.add_argument('--output', type=str, help='path to the file list')
args = parser.parse_args()

ext = {'.JPG', '.JPEG', '.PNG', '.TIF', 'TIFF'}

images = []
for root, dirs, files in os.walk(args.path):
    print('loading ' + root)
    for file in files:
        if os.path.splitext(file)[1].upper() in ext:
            img = Image.open(os.path.join(root, file))
            w, h = img.size
            array = np.array(img)
            w_long = w - args.size
            h_long = h - args.size
            if w_long < h_long:
                width  = args.size
                height = round(h / w * args.size)
            else:
                height = args.size
                width  = round(w / h * args.size)
            img.resize((width, height)).save(os.path.join(args.output, file))

# images = sorted(images)
# np.savetxt(args.output, images, fmt='%s')
