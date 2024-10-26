# Import uuid
import uuid

# Import Operating System
import os

labels = ['fishingnet', 'buoy']
number_imgs = 12

IMAGES_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'collectedimages')

for label in os.listdir(IMAGES_PATH):
    if os.path.isdir(os.path.join(IMAGES_PATH, label)):
        for file in (os.listdir(os.path.join(IMAGES_PATH, label))):
            if not file.startswith("."):
                os.rename((os.path.join(IMAGES_PATH, label, file)),
                          (os.path.join(IMAGES_PATH, label, label + '.'
                                        + '{}.jpg'.format(str(uuid.uuid1())))))


