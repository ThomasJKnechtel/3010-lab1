from PIL import Image
import numpy as np

def person_detected(image1_file, image2_file, t1):
    image1= Image.open(image1_file)
    image2=Image.open(image2_file)
    
    a1=np.asarray(image1)
    a2=np.asarray(image2)
    
    a3=a2-a1
    a3=np.absolute(a3)
    total = np.sum(a3)
    if total>t1:
        return True
    return False

    
    