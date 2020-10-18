from PIL import Image
import numpy as np
from utils import *

im = np.array(Image.open('clear.jpg'))

with open('text.txt', 'r') as t:
    text = t.read()
ar = get_array(text)
shape = im.shape
new_ar = encript(im.copy(), ar, shape)
print(new_ar[0, 0]-im[0, 0], ar[0])
new = Image.fromarray(encript(im.copy(), ar, shape))
new.save('new.jpg')




