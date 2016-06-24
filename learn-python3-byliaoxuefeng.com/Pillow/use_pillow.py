#!/usr/bin/env python

from PIL import Image, ImageFilter

#打开一个jpg图像文件，注意是当前路径
im = Image.open('a.jpg')
#获得图像尺寸
w, h = im.size
print('Original image size: %s x %s' % (w,h))
#缩放到%50
im.thumbnail((w//2, h//2))
print('Resize image to: %s x %s' % (w//2, h//2))
#把缩放后的图片用jpeg格式保存
im.save('thumbnail.jpg', 'jpeg')
# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')