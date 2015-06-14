import os
import sys
import subprocess
import random

random.seed(0)

if len(sys.argv) < 3:
    print "Usage: python gen_train.py input_folder output_folder"
    exit(1)

fi = sys.argv[1]
fo = sys.argv[2]

cmd = "convert -resize 56x56\! "
classes = os.listdir(fi)

os.chdir(fo)
for cls in classes:
    try:
        os.mkdir(cls)
    except:
        pass

    imgs = os.listdir(fi + cls)

    # resize images
    print "Resizing images for " + cls
    for img in imgs:
        md = ""
        md += cmd
        md += fi + cls + "/" + img
        md += " " + fo + cls + "/" + img
        os.system(md)

    # create flipped and flopped versions
    print "Creating mirror images for " + cls

    for img in imgs:
        md = ""
        md += cmd
        md += " -flip -flop "
        md += fi + cls + "/" + img
        basename = os.path.basename(img)
        filename = os.path.splitext(basename)
        img_without_ext = filename[0]
        md += " " + fo + cls + "/" + img_without_ext + "_flip_flop.jpg"
        os.system(md)

    # create rotations for five intermediate angles
    print "Creating rotations for " + cls
    for img in imgs:
        for deg in [60, 120, 180, 240, 300]:
            md = ""
            md += cmd
            md += "-rotate "
            md += str(deg)
            md += " -gravity center -crop 56x56+0+0 +repage "
            md += fi + cls + "/" + img
            basename = os.path.basename(img)
            filename = os.path.splitext(basename)
            img_without_ext = filename[0]
            md += " " + fo + cls + "/" + img_without_ext + "_" + str(deg) + "deg.jpg"
            os.system(md)



