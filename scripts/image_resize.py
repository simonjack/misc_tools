import os
import cv2

def get_image_size(folder, debug = None):
    
    oversize_files = []
    for root, dirs, files in os.walk(folder, topdown = False):
        for file in files:
            if file.endswith('.png'):
                im = cv2.imread(os.path.join(root, file))
                h,w,c = im.shape
                if h and w >= 1024:
                    oversize_files.append(os.path.join(root, file))
            else:
                pass
    if debug is None:
        pass
    else:
        for f in oversize_files:
            print(f)
        print('total_files: %d' %(len(oversize_files)))
    
    return oversize_files



def resize(image):

    im = cv2.imread(image, cv2.IMREAD_UNCHANGED)
    try:
        h,w,c  = im.shape
    except ValueError:
        h,w = im.shape    
    half_width = int(w/2)
    half_height = int(h/2)
    half_size = (half_width, half_height)
    half = cv2.resize(im, half_size, interpolation= cv2.INTER_LINEAR)
    cv2.imwrite(image, half)

a = get_image_size('C:/beep_boop_images')
if len(a)==0:
    pass
else:
    for i in a:
        try:
            resize(i)
        except ValueError:
            print('ERROR:' + i)

    