import cv2
import sys
import os
import numpy as np
from numpy import linalg as LA

IMAGE = "input.png"
OUT = "output.png"
SHAPE = (1151, 2048)
SHAPE_EIG = (1151, 1151)

compression = [1, 10, 25, 100, 500, 1000, 1050, 1100]

def save_grayscale():
    img = cv2.imread("original.jpg")
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cv2.imwrite("input.png", img_gray)

def encode_decode(input, decoder):
    encoder = decoder.transpose()
    output = np.matmul(np.matmul(decoder, encoder), input)
    return output

def main():
    input_img = cv2.imread(IMAGE, 0)
    assert (input_img.shape == SHAPE)
    A = np.matmul(input_img, input_img.transpose())
    assert (A.shape == SHAPE_EIG)
    values, vectors = LA.eig(A)
    assert (vectors.shape == SHAPE_EIG)
    idx = np.argsort(values)[::-1]
    eigenValues = values[idx]
    eigenVectors = vectors[:,idx]
    for index, c in enumerate(compression):
        out_img = encode_decode(input_img,eigenVectors[:,0:c])
        assert (out_img.shape == SHAPE)
        cv2.imwrite(str(index) + "_" + str(c) + "_" + OUT,out_img)
    out_img = encode_decode(input_img,eigenVectors)
    assert (out_img.shape == SHAPE)
    cv2.imwrite("FULL_" + OUT,out_img)

if __name__ == "__main__":
    main()
