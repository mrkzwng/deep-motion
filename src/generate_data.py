import os
from os.path import dirname
from data_generator import *
from scipy.misc import imread, imsave, imshow, imresize, imsave

NEW_KITTI_VID_DIR = os.path.join(KITTI_VID_DIR, 'resized')

im_list = []
for path, subdirs, files in os.walk(KITTI_VID_DIR):
    for name in files:
        fn = os.path.join(path, name)
        if fn.endswith(".png"):
            recurse = lambda f, n, x: eval('f(' * n + '"' + x + '"' + ')' * n)
            subpath = os.path.join(*list(recurse(dirname, i, fn).split('/')[-1] 
                                    for i in [4, 3, 2]))
            if not os.path.exists(os.path.join(NEW_KITTI_VID_DIR, subpath)):
                os.makedirs(os.path.join(NEW_KITTI_VID_DIR, subpath))
            new_fn = os.path.join(NEW_KITTI_VID_DIR, subpath, name)
            im_list.append(fn[len(KITTI_VID_DIR):])
            im = imread(fn)
            imsave(new_fn, imresize(im, (128, 424)))
            print(new_fn)

with open(os.path.join(KITTI_VID_DIR, 'im_list.txt'), 'w') as f:
    f.write('\n'.join(im_list) + '\n')
    f.close()

with open(os.path.join(KITTI_VID_DIR, 'im_list.txt'), 'r') as f:
    s = f.read()
    f.close()
    print(s)