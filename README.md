# kaggle-plankton
This repository contains model training for the [Kaggle National Datascience Bowl](http://www.kaggle.com/c/datasciencebowl/) on plankton image classification. The task is to classify underwater microscopic images into one of 121 different plankton classes. Some examples can be seen in the picture below. The submission uses deep convolutional neural networks trained similar to [1] trained with the [Caffe](http://caffe.berkeleyvision.org/) framework.

![alt text](https://kaggle2.blob.core.windows.net/competitions/kaggle/3978/media/plankton%20schmorgasborg.jpg)
Source: https://www.kaggle.com/c/datasciencebowl/data

Model training
--------------

The model traning was done by alternating steps of data augmentation and fine-tuning of expanded models from previous ones. The final submission used an 11 layer network that is adapted from [1] and looks like this:

| Layer |   Type            		|
|:-----:|:-------------------------:|
| Input | 48x48             		|
| 1     | conv 3x3, 64, relu    	|
| 2     | conv 3x3, 64, relu    	|
|       | max 2x2/2, dropout 0.25	| 
| 3     | conv 3x3, 128, relu    	|
| 4     | conv 3x3, 128, relu    	|
|       | max 2x2/2, dropout 0.25 	|
| 5     | conv 3x3, 256, relu    	|
| 6     | conv 3x3, 256, relu    	|
| 7     | conv 3x3, 256, relu    	|
| 8     | conv 3x3, 256, relu    	|
|       | max 2x2/2, dropout 0.25 	|
| 9     | fc 4096, relu     		|
|       | droput 0.5 				|
| 10    | fc 4096, relu     		|
|       | dropout 0.5 				|
| 11    | fc 121, softmax    		|


The final architecture achieved a multiclass log loss of 0.693548/0.704775 on the public/private part of the test set, resulting in rank 58 on the [private leaderboard](https://www.kaggle.com/c/datasciencebowl/leaderboard/private).



References
------
[1] Karen Simonyan and Andrew Zisserman. Very deep convolutional networks for large-scale image recognition. [http://arxiv.org/pdf/1409.1556v5.pdf](http://arxiv.org/pdf/1409.1556v5.pdf)


