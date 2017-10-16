import os, sys
from PIL import Image

#Image width and height
width = 51 
height = 49

List = []

#This function was adapted from the awnser of Val Kalinic at
# https://stackoverflow.com/questions/138250/how-can-i-read-the-rgb-value-of-a-given-pixel-in-python
#Get file name (image name)
#Read the image using width and height global variable
#And return a list with all the bits
def readToBin (fileName):#, elem):

    bitLst = []
    im = Image.open(fileName)
    im = im.convert('RGB')
    for y in xrange(0, height) :
        for x in xrange(0, width):

          try:
              RGB = im.getpixel((x, y))
              R,G,B = RGB
              if R > 0 or G > 0 or B > 0 :
                  bitLst.append('-1 ')
              else:
                  bitLst.append('1 ')
          except:
              pass
    return bitLst

#Write 'mark'.data file
#File will have a format that will be easy to read from lisp
#  target
#  Lisp list
def writeToLisp (lst, mark, path):

    size = len(lst)
    fileName = path + "data/" + mark + ".data"
    print "Mark:" + mark
    print "Saving at:" + fileName
    with open(fileName, 'w') as file:
        file.write(mark)
        for x in lst : 
            file.write('\n')
            file.write(' \'( ')
            for elem in x :
                file.write(elem)
            file.write(')')

#Write to lisp list
def readWrite (fName):
    binL = readToBin(fName)
    fileName = fName + ".data"
    with open(fileName, 'w') as file:
        file.write(' \'( ')
        for elem in binL :
            file.write(elem)
        file.write(')')
        
#Get all files in currently directory
#And create data dir
def getFiles (filePath): 
    dir = os.getcwd() + '/' + filePath
    dataDir = ""
    try:
        dataDir = dir + "data"
        os.mkdir(dataDir, 0755)
        print "Creating file: " + dataDir
    except:
        pass
    
    files =  os.listdir(dir)[1::]
    print files
    for item in files:
        if item == 'data':
            continue
        else: 
            path_to_image = dir  + item #Path to the file where the images are saved
            mark = item #Where tha data will be writted
            images = os.listdir(path_to_image)
            lst = []
            for img in images: #Will read from the data and write to memory
                file = path_to_image + '/' + img #Will get all .png files in the path file
                lst.append(readToBin(file)) #will read .png file convert to bitmap and save in memory
            writeToLisp(lst, mark, dir)
            
#python bitMap.py file-name/
if __name__ == '__main__':

    
    s = len(sys.argv)
    if s > 2:
        readWrite(sys.argv[1])
    elif s == 2 : 
        getFiles(sys.argv[1])
    else :
        print "Wrong number of arguments"

    
            
        
