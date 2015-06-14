import csv
import sys
import numpy as np
import caffe
from skimage.transform import rotate

net = caffe.Classifier('/home/matthias/kaggle/plankton/networks/plankton_vgg_test.prototxt', '/home/matthias/kaggle/plankton/models/plankton_vgg_train_iter_30000.caffemodel', image_dims=(56, 56), channel_swap=(2, 1, 0), raw_scale=255)

net.set_phase_test()
net.set_mode_gpu()

a = caffe.io.caffe_pb2.BlobProto()
f = open('/home/matthias/kaggle/plankton/mean.binaryproto', 'rb')
d = f.read()
a.ParseFromString(d)
mean_image = a.data
mean_image = np.asarray(mean_image)
mean_image = mean_image.reshape(1, 56, 56)
net.set_mean('data', mean_image)
#net.set_raw_scale('data', 255)
#net.set_channel_swap('data', (2, 1, 0))

fc = csv.reader(file(sys.argv[1]))
file_list = csv.reader(file(sys.argv[2]), delimiter='\t', lineterminator='\n')
fo = csv.writer(open(sys.argv[3], "w"), lineterminator='\n')

head = fc.next()
fo.writerow(head)

head = head[1:]
idx = 0

for line in file_list:
    print str(idx)
    idx += 1
    path = line[0]
    im = caffe.io.load_image('/home/matthias/kaggle/plankton/data/test/' + path)
    scores = net.predict([im], oversample=True)
    path = [path]
    path.extend(scores[0])
    fo.writerow(path)



    

