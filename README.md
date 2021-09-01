# imagetopdf

ImageToPdf is a small tool that generates a pdf using pillow

inspired from image2pdf from https://github.com/geekcomputers/Python/blob/master/image2pdf/image2pdf.py

I prefer passed images in command line before converting automatically images from directory

imageToPdf is a python3 converter that saves your image into a pdf
For linux and linux-like OS that have the pre-requisite pillow module
Usage: imagetopdf [options] image1 image2 imagex pdfname
image should have the required extension JPG, JPEG or PNG
pdfname should have the pdf extension
Options:
-V, --version Display version number of imageToPdf
-H, --help Display this help

---

Enjoy!

Note that you can convert into an exe using my other tool pytoc!

## imagetopdf usage

### imagetopdf help

imagetopdf -H
imagetopdf --heLp (case insensitive)

prints the help (see above)

### imagetopdf version

imagetopdf -V
imagetopdf --version

will display :
imageToPdf version 1.0.0

### imagetopdf with two images :

imagetopdf heart.png start.png test.pdf

will display :
pictures are :
['heart.png', 'start.png']
done!

test.pdf contains now the two images
