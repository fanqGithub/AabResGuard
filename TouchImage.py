# coding = utf-8
import os
from optparse import OptionParser

from PIL import Image


def touch_image(_path):
    i = 1
    j = 1

    img = Image.open(_path)
    img = img.convert("RGBA")
    width = img.size[0]
    height = img.size[1]
    for i in range(0, width):
        for j in range(0, height):
            data = (img.getpixel((i, j)))
            # print(data)
            # print(data[0])
            if 255 > data[3] > 0:
                img.putpixel((i, j), (data[0], data[1], data[2], data[3] - 1))
                img.save(_path)
                return True
            elif 255 > data[2] > 0:
                img.putpixel((i, j), (data[0], data[1], data[2] - 1, data[3]))
                img.save(_path)
                return True
            elif 255 > data[1] > 0:
                img.putpixel((i, j), (data[0], data[1] - 1, data[2], data[3]))
                img.save(_path)
                return True
            elif 255 > data[0] > 0:
                img.putpixel((i, j), (data[0] - 1, data[1], data[2], data[3]))
                img.save(_path)
                return True
    return False


def touch_dir(_dir):
    for root, dirs, file in os.walk(_dir):
        for _item in file:
            try:
                file_path = os.path.join(root, _item)
                if file_path.endswith(".png") or file_path.endswith(".jpg") or file_path.endswith(".webp"):
                    _bf_size = os.path.getsize(file_path)
                    _b = touch_image(file_path)
                    _f_size = os.path.getsize(file_path)
                    print("touch img=%s success=%r 原size=%d to 现=%d" % (file_path,_b, _bf_size, _f_size))
            except Exception as e:
                print("touch img failed@@@@@@@@@@:", e)


# if __name__ == '__main__':
#     parser = OptionParser()
#     parser.add_option(
#         '-i', '--input',
#         action='store',
#         type='string',
#         dest='input',
#         help='input your apk dir path',
#         metavar='input your apk dir path'
#     )
#
#     (options, args) = parser.parse_args()
#
#     path = options.input
#
#     if not path:
#         print("options.input is null")
#         pass
#     elif os.path.isdir(path):
#         print("options.input is dir: " + path)
#         touch_dir(path)
#     else:
#         print("options.input is file: " + path)
#         a = touch_image(path)
#         print("result: " + str(a))

    # 调用函数，传入项目根目录和脚本文件名
project_root_directory = os.getcwd()  # 修改为你的项目根目录路径
path = project_root_directory
print("path=%s" % path)

if not path:
    print("options.input is null")
    pass
elif os.path.isdir(path):
    print("options.input is dir: " + path)
    touch_dir(path)
else:
    print("options.input is file: " + path)
    a = touch_image(path)
    print("result: " + str(a))