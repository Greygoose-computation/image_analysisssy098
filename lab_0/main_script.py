import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# load the image
image=Image.open('data/lemon.png')

# Convert the image to a numpy array
image = np.array(image)

# 