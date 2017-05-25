# -*- coding: utf-8 -*-
import csv
import codecs
import shutil
import os
from time import clock
import glob
import chardet

def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')


def autoDetectEncoding(txtFilePath):
    with open(txtFilePath) as f:
        bufferSize = 10240
        while True:
            rawData = f.read(bufferSize)
            encodingMethod = chardet.detect(rawData).get('encoding')
            confidence =  chardet.detect(rawData).get('confidence')
            print '='*50
            print "file: " + txtFilePath 
            print 'encodingMethod:' + encodingMethod 
            print "confidence: " + str(confidence)
            print 'bufferSize: ' + str(bufferSize)
            print '='*50
            if confidence > 0.9:
                break
            bufferSize *= 2
            f.seek(0)
        return encodingMethod

#def guessEncodeMethod(rawData):
    #encodeMethods = ['utf-8',]

def txt2csv(txtFilePath, encodingMethod):
    with codecs.open(txtFilePath, 'r', encodingMethod) as f:
        file_head_raw_data = f.read(10240)
        dialect = csv.Sniffer().sniff(file_head_raw_data)
        f.seek(0)
        print file_head_raw_data.encode("utf-8")
        lines = f.readlines(3)
        reader = csv.reader(utf_8_encoder(lines), delimiter=dialect.delimiter)
        for row in reader:
            print row
        if raw_input("\nwould you wanna using the dialect[" + dialect.delimiter
            + "] to parsing this txt file?[y]\n") != "":
            dialect = raw_input("\nwill you specify a dialect\n?")
            if dialect == "":
                return
                
    


def autoClassify(src_root_path, target_dir):
    root_src_dir = src_root_path
    root_target_dir = target_dir
    encodingMethod = []
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
                encoding = autoDetectEncoding(txtFile)
                if encoding not in encodingMethod:
                    encodingMethod.append(encoding)
                #print encoding
                print encodingMethod
                #txt2csv(txtFile, encoding)

autoClassify("/media/jason/Seagate Backup Plus Drive/penetration/Dic/data/",
"/media/jason/sgk/")
