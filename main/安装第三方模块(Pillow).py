from PIL import Image

# 打开图片
im = Image.open("./image/zoro.jpg")

# 查看图片路径
print(im.format, im.size, im.mode)
