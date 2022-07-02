# --- standard function.py ---
# movie - video
#       |
#       L pic_video


# --- picup frame ---
import cv2
import os
def save_frame(video_name, video_folder, pic_folder):  
    # setting
    # video_folder = 'examples/videos' 
    # pic_folder ='pic'  
    frame_num = 10
    # content
    video_path = video_folder + '/' + video_name
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
    ret, frame = cap.read()
    result_path = pic_folder + '/' + os.path.splitext(video_name)[0]+'.jpg'
    if ret:
        cv2.imwrite(result_path, frame)

# --- display_movie ---
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import os
import glob

def display_movie(folder, name):
    fig = plt.figure(figsize=(30, 60))
    files = sorted(glob.glob(folder+'/*.jpg'))
    for i, file in enumerate(files):
        img = Image.open(file)    
        images = np.asarray(img)
        ax = fig.add_subplot(10, 5, i+1, xticks=[], yticks=[])
        image_plt = np.array(images)
        ax.imshow(image_plt)
        ax.set_xlabel(name[i], fontsize=30)
    fig.tight_layout()               
    plt.show()
    plt.close()


# --- display_mp4 ---
from IPython.display import display, HTML, clear_output

def display_mp4(path):
    from base64 import b64encode
    mp4 = open(path,'rb').read()
    data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
    display(HTML("""
    <video width=500 controls>
        <source src="%s" type="video/mp4">
    </video>
    """ % data_url))



# --- display_pic ---
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import os
import glob

def display_pic(folder):
    fig = plt.figure(figsize=(30, 60))
    files = sorted(glob.glob(folder+'/*.jpg'))
    for i, file in enumerate(files):
        img = Image.open(file)    
        images = np.asarray(img)
        ax = fig.add_subplot(10, 5, i+1, xticks=[], yticks=[])
        image_plt = np.array(images)
        ax.imshow(image_plt)
        name = os.path.basename(file)
        ax.set_xlabel(name, fontsize=30)  
        fig.tight_layout()             
    plt.show()
    plt.close()


# --- display_pic_png ---
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import os
import glob

def display_pic_png(folder):
    fig = plt.figure(figsize=(30, 60))
    files = sorted(glob.glob(folder+'/*.png'))
    for i, file in enumerate(files):
        img = Image.open(file)    
        images = np.asarray(img)
        ax = fig.add_subplot(10, 5, i+1, xticks=[], yticks=[])
        image_plt = np.array(images)
        ax.imshow(image_plt)
        name = os.path.basename(file)
        ax.set_xlabel(name, fontsize=30)  
        fig.tight_layout()             
    plt.show()
    plt.close()
    
# --- size adjust --- 
import cv2

def size_opt(file, max_size):
    #max_size = 1280
    npyImage = cv2.imread(filename = file, flags = cv2.IMREAD_COLOR)
    intWidth = npyImage.shape[1]
    intHeight = npyImage.shape[0]

    fltRatio = float(intWidth) / float(intHeight)
    intWidth = min(int(max_size * fltRatio), max_size)
    intHeight = min(int(max_size / fltRatio), max_size)

    # make even
    if not intWidth % 2 == 0:
      intWidth +=1
    if not intHeight % 2 ==0:
      intHeight +=1

    npyImage = cv2.resize(src=npyImage, dsize=(intWidth, intHeight), fx=0.0, fy=0.0, interpolation=cv2.INTER_AREA)
    cv2.imwrite(file, npyImage)
    
    
# --- reset_folder ---
import shutil

def reset_folder(path):
    if os.path.isdir(path):
      shutil.rmtree(path)
    os.makedirs(path,exist_ok=True)
    
    
