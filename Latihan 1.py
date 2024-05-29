import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('kucing.jpg')
cat = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(cat)
plt.show()
kernel = np.ones((5,5),np.float32)/25
print("Kernel:\n", kernel)
kucing_filter = cv2.filter2D(img, -1, kernel)
plt.imshow(kucing_filter)
plt.show()


