import os
import numpy
import cv2
import glob


def imread(filename, flags=cv2.IMREAD_COLOR, dtype=numpy.uint8):
    try:
        n = numpy.fromfile(filename, dtype)
        img = cv2.imdecode(n, flags)
        return img
    except Exception as e:
        print(e)
        return None


def imwrite(filename, img, params=None):
    try:
        ext = os.path.splitext(filename)[1]
        result, n = cv2.imencode(ext, img, params)

        if result:
            with open(filename, mode='w+b') as f:
                n.tofile(f)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def searchName(inners):
    i = 0
    while True:
        name = 'change'+str(i)
        if name not in inners:
            return name
        else:
            i += 1

if sys.argv[1]:
    files = glob.glob(os.path.dirname(sys.argv[1])+'\\*')
    inners = list()

    for file in files:
        inners.append((os.path.split(file))[1])
    new_dir = os.path.dirname(sys.argv[1])+'\\'+searchName(inners)
    os.makedirs(new_dir)

    for i in range(1,len(sys.argv)):
        path = sys.argv[i]
        path_tmp = os.path.split(path)
        name_tmp = (path_tmp[1]).split('.')
        file_name = name_tmp[0]
        img = imread(path, -1)
        imwrite(new_dir+'\\'+file_name + '.jpg', img)