import os
import shutil
import sys
from pathlib import Path
from os.path import join

class mp3_converter():
    def __init__(self, base, path, ext, dirName):
        """Class that takes folder of music files of one file type, 
        converts them to mp3 and creates a new directory and moves them into it
        Input path of files that you would like to convert
        Extension of files you would like to convert i.e. WAV
        Folder name of the new directory you would like to create"""
        self.path = path
        self.ext = ext
        self.dirName = dirName
        self.home = os.path.split(base)[1]
        print('HOME IS ' + self.home)

    def setPath(self, path):
        self.path = path

    def mp3(self):
        """
        Converts all files in path with entered extension to mp3
        """
        directory = self.path   
       
        print('scanning -->' + directory)
        obj = os.scandir(directory)
        
        found = False
        for entry in obj :
            if entry.is_file():
                print('file is ' + entry.name)
                #print(os.path.dirname(entry.path))
                if (entry.name.endswith(self.ext)):
                    found = True
                    os.system("ffmpeg -i \"{}\" -ar 44100 -ac 2 -b:a 192k \"{}\"/\"{}\".mp3".format(
                        entry.path, os.path.dirname(entry.path), os.path.splitext(entry.name)[0]))
        return found

    def make_dir(self):
        """
        Creates a directory for mp3's and moves all 
        previously created mp3's into it and moves the directory up one
        """
        newDir = os.path.split(self.path)[1] + '-' + self.dirName
        mp3_directory = self.path + "/" + newDir
#        return
        if not os.path.exists(mp3_directory):
            os.makedirs(mp3_directory)
        for filename in os.listdir(self.path):
            if (filename.endswith(".mp3")):
                source = os.path.join(self.path, filename)
                dest = shutil.move(source, mp3_directory)
#                print(f"Moved {filename} to {dest}")
        toDisk = 'I:\\mp3copies\\' + self.home + newDir
        print (toDisk)
        os.makedirs(toDisk, exist_ok=True)
        overToDisk = shutil.move(mp3_directory, toDisk)
    
    def move_to_dir(self):
        newDir = os.path.split(self.path)[1] + '-' + self.dirName
        mp3_directory = self.path + "/" + newDir
#        return
        if not os.path.exists(mp3_directory):
            os.makedirs(mp3_directory)
        for filename in os.listdir(self.path):
            if (filename.endswith(".mp3")):
                source = os.path.join(self.path, filename)
                dest =  'I:\\mp3copies\\' + self.home + '/' + newDir
                os.makedirs(dest, exist_ok=True)
                dest = shutil.move(source, dest)
                
                print(' s ' + source)
                print(' d ' + 'I:\\mp3copies\\' + self.home + '/' + newDir)



if __name__ == '__main__':  
    path = join(sys.argv[-1])
# Print the path for debugging
    print(path)
#   path = "G:\__music\\test\Simple Minds - Sparkle In The Rain (1984) [FLAC] (2015 Deluxe Expanded Edition)"    
    baseobj = os.scandir(path)
    for entry in baseobj :
        if entry.is_dir():
            subpath = os.path.join(path, entry.name)
            print('checking ' + subpath)
            conv = mp3_converter(path, subpath, (".wav", "flac"), "mp3")
            conv.setPath(subpath)
            if conv.mp3(): 
                conv.move_to_dir()
    conv = mp3_converter(path, path, (".wav", "flac"), "mp3")
    if conv.mp3(): 
        conv.move_to_dir()
#    print(conv.home)


