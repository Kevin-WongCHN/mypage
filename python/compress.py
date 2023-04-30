from PIL import Image
import os

# 定义要处理的图片路径
img_path = "..\\images\\IMG_20230110_085415.jpg"

# 获取原始图片大小，以便后面比对压缩后的大小
size_before = os.stat(img_path).st_size

# 打开并压缩图片
with Image.open(img_path) as im:
    # 设置压缩率
    quality = 10
    # 压缩图片并保存
    im.save('compressed_image.jpg', optimize=True, quality=quality)

# 计算压缩后的图片大小，以便输出比对结果
size_after = os.stat('compressed_image.jpg').st_size

# 输出压缩前后的图片大小
print(f"Original size is {size_before} bytes.")
print(f"Compressed image size is {size_after} bytes.")
