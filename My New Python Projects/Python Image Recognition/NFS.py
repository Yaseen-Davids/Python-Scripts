from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time

def threshold(imageArray):
    blanceAr = []
    newAr = imageArray

    for eachRow in imageArray:
        for eachPix in eachRow:
            print(eachPix)

            time.sleep(5)

i = Image.open('images/shift-MCE.png')
iar = np.array(i)

fig = plt.figure()
ax1 = plt.subplot2grid((8,6), (0,0), rowspan=4, colspan=3)

ax1.imshow(iar)

print(np.array(i))
