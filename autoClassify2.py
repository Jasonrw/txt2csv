# -*- coding: utf-8 -*-
import shutil
import os
from time import clock
import glob
import chardet

def autoDetectEncoding(txtFilePath):
    with open(txtFilePath) as f:
        rawData = f.read(99999)
        encodingMethod = chardet.detect(rawData).get('encoding')
        confidence =  chardet.detect(rawData).get('confidence')
        print "find the file: " + txtFilePath + "is encoded with \n" +\
        encodingMethod + "\nconfidence: " + str(confidence)
        return encodingMethod

def txt2csv(textFilePath):
    pass


def autoClassify(src_root_path, target_dir):
    root_src_dir = src_root_path
    root_target_dir = target_dir
    for src_dir, dirs, files in os.walk(root_src_dir):
        #detect if there any txt files in src_dir
        #print src_dir
        txtList = glob.glob(src_dir + "/*.txt")
        if txtList.__sizeof__ > 0:
            targetDir = src_dir.replace(root_src_dir, root_target_dir)
            if not os.path.exists(targetDir):
                #os.mkdir(targetDir)
                pass
            for txtFile in txtList:
                targetTxtFile = txtFile.replace(root_src_dir, root_target_dir)
                #print targetDir
                #print targetTxtFile
                autoDetectEncoding(txtFile)

autoClassify("/media/jason/Seagate Backup Plus Drive/penetration/Dic/data/",
"/media/jason/sgk/")
