import scipy
from scipy import misc
import scipy.ndimage as ndimage
f = misc.face()
misc.imsave('face.png', f) # uses the Image module (PIL)
blurred_face = ndimage.gaussian_filter(f, sigma=3)

import matplotlib.pyplot as plt
plt.imshow(blurred_face)
plt.show()
