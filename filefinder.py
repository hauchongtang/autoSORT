import os
import shutil
import glob
import pathlib
from os import path

path_ = "D:/Sorter/*"
filename = glob.glob(path_)

# Arrays of file types/ extensions
def open_as_array(targetfile):
    f = open(targetfile, "r+")
    variablename = [line[:-1] for line in f.readlines()] # remove \n from every ele in tags[]
    f.close()
    return variablename

exts = open_as_array("extensions.txt")
# print(exts)
tags = open_as_array("tags.txt")
tags[3] = "data" # fix "None" bug
tags[14] = "wordprocessor" # remove dash (standardization)
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
        name = "D:/Sorter/" + array[i]
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

def do_sort(array, path):
    if os.path.splitext(file)[1] in array:
        if (os.path.exists(path)):
            shutil.move(file, path)
        else:
            os.makedirs(path)
            shutil.move(file, path)

for file in filename:
    do_sort(audio, audioLoc)
    do_sort(compressed, compressedLoc)
    do_sort(disc, discLoc)
    do_sort(data, dataLoc)
    do_sort(email, emailLoc)
    do_sort(executable, executableLoc)
    do_sort(font, fontLoc)
    do_sort(image, imageLoc)
    do_sort(internet, internetLoc)
    do_sort(presentation, presentationLoc)
    do_sort(programming, programmingLoc)
    do_sort(spreadsheet, spreadsheetLoc)
    do_sort(system, systemLoc)
    do_sort(video, videoLoc)
    do_sort(wordprocessor, wordLoc)

