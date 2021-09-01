#!/usr/bin/python3
# -*- coding: utf-8 -*-
#inspired from image2pdf from https://github.com/geekcomputers/Python/blob/master/image2pdf/image2pdf.py
from PIL import Image
import os
import sys


__version__ = "1.0.0"


class imageTopdf:
    def __init__(self, images, pdf):
        self.validFormats = (
            '.jpg',
            '.jpeg',
            '.png',
            '.JPG',
            '.PNG'
        )
        self.images = images
        self.pictures = []
        #self.files = os.listdir()
        self.convertPictures(images, pdf)

    
    def filter(self, item):
        return item.endswith(self.validFormats)


    # def sortFiles(self):
    #     return sorted(self.files)

    
    def getPictures(self, images):
        pictures = list(filter(self.filter, images))
        if self.isEmpty(pictures):
            print(" [Error] there are no pictures with expected format! ")
            raise Exception(" [Error] there are no pictures with expected format !")
        print('pictures are : \n {}'.format(pictures))
        return pictures

    def isEmpty(self, items):
        return True if len(items) == 0 else False

    def convertPictures(self, image, pdf):
        for picture in self.getPictures(image):
            self.pictures.append(Image.open(picture).convert('RGB'))
        self.save(pdf)


    def save(self, pdf):
        self.pictures[0].save(pdf, save_all=True, append_images=self.pictures[1:])


def print_help():
    print("imageToPdf is a python3 converter that saves your image into a pdf")
    print("For linux and linux-like OS that have the pre-requisite pillow module")
    print("Usage: imagetopdf [options] image1 image2 imagex pdfname")
    print("image should have the required extension JPG, JPEG or PNG")
    print("pdfname should have the pdf extension")
    print("Options:")
    print("-V, --version        Display version number of imageToPdf")
    print("-H, --help           Display this help")
    print("__________________________________________")
    print("Enjoy!")


if __name__ == "__main__":
    argList = []
    isForbid = False
    # execute only if run as a script
    #print(f"Arguments count: {len(sys.argv)}")
    argList = sys.argv[1:]
    nbarg = len(argList)
    argFirst = argList[0]
    isImage = False
    images = argList[:-1]
    pdf = argList[-1]
    if argFirst.lower() == '--help' or argFirst.lower() == '-h':
        print_help()
    elif argFirst.lower() == '--version' or argFirst.lower() == '-v':
        print("imageToPdf version " + __version__)    
    else:     
        if nbarg == 0 or nbarg == 1:
            print("missing arguments! ") 
            print_help()
        else:
            for image in images:           
                if os.path.isfile(image):         
                    isImage = True
                else:
                    isImage = False
                    print(image + " not found!")                
                    break
            if isImage:
                imageTopdf(images, pdf)
                print("done!")                
    