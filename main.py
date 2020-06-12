import os
import shutil
import glob
import pathlib
from os import path

path_ = "D:\\Sorter"
path_w = path_.replace('/', '\\')
print(path_w)
path_main = path_ + "/*"
filename = glob.glob(path_main)

# Read from data (.txt file)
def open_as_array(targetfile):
    f = open(targetfile, "r+")
    variablename = [line[:-1] for line in f.readlines()] # remove \n from every ele in tags[]
    f.close()
    return variablename

exts = open_as_array("extensions.txt")
# print(exts)
tags = open_as_array("tags.txt")
# print(tags)

# assign to groups
audio = exts[:10]
compressed = exts[10:19]
disc = exts[19:24]
data = exts[24:34]
email = exts[34:42]
executable = exts[42:54]
font = exts[54:58]
image = exts[58:70]
internet = exts[70:86]
presentation = exts[86:91]
programming = exts[91:101]
spreadsheet = exts[101:105]
system = exts[105:120]
video = exts[120:135]
wordprocessor = exts[135:]
# print(data)

def generatepathname(array, i):
        name = os.path.join(path_, array[i])#path_ + "/" + array[i]
        return name

audioLoc = generatepathname(tags, 0)
compressedLoc = generatepathname(tags, 1)
discLoc = generatepathname(tags, 2)
dataLoc = generatepathname(tags, 3)
emailLoc = generatepathname(tags, 4)
executableLoc = generatepathname(tags, 5)
fontLoc = generatepathname(tags, 6)
imageLoc = generatepathname(tags, 7)
internetLoc = generatepathname(tags, 8)
presentationLoc = generatepathname(tags, 9)
programmingLoc = generatepathname(tags, 10)
spreadsheetLoc = generatepathname(tags, 11)
systemLoc = generatepathname(tags, 12)
videoLoc = generatepathname(tags, 13)
wordLoc = generatepathname(tags, 14)

# print(audioLoc)

def do_sort(array, path):
    if os.path.splitext(file)[1] in array:
        if (os.path.exists(path)):
            shutil.move(file, path)
        else:
            os.makedirs(path)
            shutil.move(file, path)
def exception_handler(array, path):
    try:
        if not do_sort(array, path):
            raise FileNotFoundError
    except FileNotFoundError:
        print("Files are sorted, listening for another action...")

for file in filename:
    exception_handler(audio, audioLoc)
    exception_handler(compressed, compressedLoc)
    exception_handler(disc, discLoc)
    exception_handler(data, dataLoc)
    exception_handler(email, emailLoc)
    exception_handler(executable, executableLoc)
    exception_handler(font, fontLoc)
    exception_handler(image, imageLoc)
    exception_handler(internet, internetLoc)
    exception_handler(presentation, presentationLoc)
    exception_handler(programming, programmingLoc)
    exception_handler(spreadsheet, spreadsheetLoc)
    exception_handler(system, systemLoc)
    exception_handler(video, videoLoc)
    exception_handler(wordprocessor, wordLoc)


