"""
Convert images from training set to 56x56 pixels and augment the dataset
by generating flipped versions, rotations by 5 specified angles and apply random
scaling and image shearing at random angles.
"""

import os
import sys
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

    # resize original images
    print "Resizing images for " + cls
    for img in imgs:
        md = ""
        md += cmd
        md += fi + cls + "/" + img
        md += " " + fo + cls + "/" + img
        os.system(md)

    # create flipped and flopped versions from originals
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

    print "Creating scaled rotated versions"
    for img in imgs:
        for deg in [0, 60, 120, 180, 240, 300]:
            for nRep in range(5):
                scale_factor = random.randint(48, 64)
                md = "convert -resize " + str(scale_factor) + "x" + str(scale_factor) + \
                     "\! -gravity center -background white -extent 56x56 "
                md += "-rotate " + str(deg)
                md += " -gravity center -crop 56x56+0+0 +repage "
                md += fi + cls + "/" + img
                basename = os.path.basename(img)
                filename = os.path.splitext(basename)
                img_without_ext = filename[0]
                md += " " + fo + cls + "/" + img_without_ext + "_scaled_" + str(scale_factor) + "_" \
                      + str(deg) + "deg.jpg"
                os.system(md)

    print "Creating scaled sheared versions"
    for img in imgs:
        for nRep in range(5):
            scale_factor = random.randint(48, 64)
            shear_x = random.randint(-10, 10)
            shear_y = random.randint(-10, 10)
            md = "convert -resize " + str(scale_factor) + "x" + str(scale_factor) \
                 + "\! -gravity center -background white -extent 56x56 "
            md += "-shear " + str(shear_x) + "x" + str(shear_y)
            md += " -gravity center -crop 56x56+0+0 +repage "
            md += fi + cls + "/" + img
            basename = os.path.basename(img)
            filename = os.path.splitext(basename)
            img_without_ext = filename[0]
            md += " " + fo + cls + "/" + img_without_ext + "_scaled_" + str(scale_factor) \
                  + "_" + str(shear_x) + "x" + str(shear_y) + "shear.jpg"
            os.system(md)


