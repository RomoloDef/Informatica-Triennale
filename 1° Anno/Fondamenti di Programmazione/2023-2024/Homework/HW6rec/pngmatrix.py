#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Utility functions to load and save image files.
'''
import png

def load_png8(fname):
    """ Loads a PNG-8 image from the "fname" file.
        Returns a matrix (list of lists) of pixels.
        Every pixel is a triple (r, g, b) with the intensity of the three
        screen colours, expressed as a number ranging between 0 and 255
        (included), where:
            - r stands for red;
            - g stands for green;
            - b stands for blue.
    """
    with open(fname, mode='rb') as f:
        reader = png.Reader(file=f)
        try:
            w, h, png_img, _ = reader.asRGB8()
        except:
            raise ValueError("WARNING: The image has a transparency channel.")
        w *= 3
        return [ [ (line[i],line[i+1],line[i+2]) for i in range(0, w, 3) ]
                 for line in png_img ]

def save_png8(img, fname):
    """ Saves the "img" image in the "fname" file using the PNG-8 encoding.
        img is a matrix (list of lists) of pixels.
        Every pixel is a triple (r, g, b) with the intensity of the three
        screen colours, expressed as a number ranging between 0 and 255
        (included), where:
            - r stands for red;
            - g stands for green;
            - b stands for blue.
    """
    pngimg = png.from_array(img,'RGB')
    pngimg.save(fname)
