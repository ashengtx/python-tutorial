from scipy.misc import imread, imsave, imresize

# Read an JPEG image into a numpy array
img = imread('../img/cat.jpg')
print(img.dtype, img.shape)  # Prints "uint8 (400, 248, 3)"

# 调整颜色。红绿蓝三个通道分别乘以1,0.95,0.9
img_tinted = img * [1, 0.95, 0.9]

# Resize the tinted image to be 300 by 300 pixels.
img_tinted = imresize(img_tinted, (300, 300))

# Write the tinted image back to disk
imsave('../img/cat_tinted.jpg', img_tinted)
