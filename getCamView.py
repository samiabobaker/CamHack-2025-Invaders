import numpy as np
from PIL import Image


screen = np.asarray(Image.open("Unknown.png").convert('RGB'))
print(screen.shape)

clipped_screen = screen[131:131+186, 1509:1509+331]
new_im = Image.fromarray(clipped_screen)
new_im.show()

clipped_screen = screen[331:331+186, 1509:1509+331]
new_im = Image.fromarray(clipped_screen)
new_im.show()

clipped_screen = screen[532:532+186, 1509:1509+331]
new_im = Image.fromarray(clipped_screen)
new_im.show()

clipped_screen = screen[734:734+186, 1509:1509+331]
new_im = Image.fromarray(clipped_screen)
new_im.show()

