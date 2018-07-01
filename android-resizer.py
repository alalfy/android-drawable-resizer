#
# The Android Drawable Resizer.
#
#
# Copyright (c) 2018 by Islam Alalfy.  All rights reserved.
# Copyright (c) 2016-2018 by Engineer Mix.
#

import os
import PIL
from PIL import Image

LDPI_RATIO = 3
MDPI_RATIO = 4
TVDPI_RATIO = 5.33333333
HDPI_RATIO = 6
XHDPI_RATIO = 8
XXHDPI_RATIO = 12
XXXHDPI_RATIO = 16

in_ratio = {}
out_ratios = {}

# height = img.height

imgs_path = input("please enter images path/dir (example: /home/user/imgs): ")
out_path = input("please enter Output path/dir (example: /home/user/output): ")

in_ratio_string = input("please enter image ratio (example: mdpi): ")

if in_ratio_string == "ldpi":
    in_ratio = LDPI_RATIO
elif in_ratio_string == "mdpi":
    in_ratio = MDPI_RATIO
elif in_ratio_string == "tvdpi":
    in_ratio = TVDPI_RATIO
elif in_ratio_string == "hdpi":
    in_ratio = HDPI_RATIO
elif in_ratio_string == "xhdpi":
    in_ratio = XHDPI_RATIO
elif in_ratio_string == "xxhdpi":
    in_ratio = XXHDPI_RATIO
elif in_ratio_string == "xxxhdpi":
    in_ratio = XXXHDPI_RATIO
else:
    print("wrong ratio please enter correct ratio\nratios : ldpi - mdpi - tvdpi - hdpi - xhdpi - xxhdpi - xxxhdpi")
    exit()

replay = input("do you want ldpi in out sizes?(y/n)\n")
if replay == 'y':
    out_ratios["ldpi"] = LDPI_RATIO

replay = input("do you want mdpi in out sizes?(y/n)\n")
if replay == 'y':
    out_ratios["mdpi"] = MDPI_RATIO

replay = input("do you want tvdpi in out sizes?(y/n)\n")
if replay == 'y':
    out_ratios["tvdpi"] = TVDPI_RATIO

replay = input("do you want hdpi in out sizes?(y/n)\n")
if replay == 'y':
    out_ratios["hdpi"] = HDPI_RATIO

replay = input("do you want xhdpi in out sizes?(y/n)\n")
if replay == 'y':
    out_ratios["xhdpi"] = XHDPI_RATIO

replay = input("do you want xxhdpi in out sizes?(y/n)\n")
if replay == 'y':
    out_ratios["xxhdpi"] = XXHDPI_RATIO

replay = input("do you want xxxhdpi in out sizes?(y/n)\n")
if replay == 'y':
    out_ratios["xxxhdpi"] = XXXHDPI_RATIO


for img_name in os.listdir(imgs_path):
    try:
        img = Image.open(imgs_path+"/"+img_name)
    except FileNotFoundError as err:
        print(err)
        continue
    except IsADirectoryError as err:
        print(err)
        continue

    out_width = {}
    width = img.width

    for ratio in out_ratios:
        out_width[ratio] = (width * (out_ratios[ratio] / in_ratio))

    for out_w in out_width:
        if not os.path.exists(out_path+"/drawable-" + out_w):
            os.makedirs(out_path+"/drawable-" + out_w)
        basewidth = int(out_width[out_w])
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        new_img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        new_img.save(out_path+"/drawable-" + out_w + "/" + img_name, img.format)
