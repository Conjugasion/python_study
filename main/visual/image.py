"""
@author Lucas
@date 2019/1/18 15:00

"""
import matplotlib.pyplot as plt
import scipy.misc as misc

face_g = misc.face(gray=True)
plt.imshow(face_g, cmap='gray')
print(face_g)
plt.show()