from PIL import Image
from inference import Predictor
import pathlib
import cv2 
import numpy as np

CELEBRITY_LABELS = {'female': 0, 'male': 1}

def gen_img(src_p, ref_p, label):
    predictor = Predictor(entity="celebrity")
    src = Image.open(src_p).convert("RGB")
    ref = Image.open(ref_p).convert("RGB")
    result_p = pathlib.Path(f"images/res/{src_p.split('/')[-1]}_{ref_p.split('/')[-1]}.jpg")
    res_img = predictor.create_interpolation(label, src_image=src, ref_image=ref, res_p=result_p)
    
    src = cv2.imread(src_p)
    ref = cv2.imread(ref_p)

    newsrc_width = int((src.shape[1]*256)/src.shape[0])
    newref_width = int((ref.shape[1]*256)/ref.shape[0])
    print(src.shape[0],src.shape[1], newsrc_width)
    print(ref.shape[0],ref.shape[1], newref_width)

    src_resized = cv2.resize(src, (newsrc_width, 256))
    ref_resized = cv2.resize(ref, (newref_width, 256))
    res_resized = res_img[0].transpose(1, 2, 0)
    print(src_resized.shape, ref_resized.shape, res_resized.shape)
    combined_image = np.concatenate((src_resized, res_resized), axis=1)
    cv2.imwrite('combined_image.png', res_resized)  # Save as an image
    cv2.imshow('Combined Image', res_resized)  # Display the image
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite(f"{result_p.replace(1, 'gen')}", combined_image)


if __name__ == '__main__':
    src_p = './images/mask1/f/2.jpg'
    ref_p = './images/mask1/m/3.jpg'
    label = "female"
    gen_img(src_p, ref_p, label)
