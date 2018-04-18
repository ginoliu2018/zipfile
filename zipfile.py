# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 16:04:31 2018

@author: Gino_Liu
"""
#
#
#
import shutil
import os
from email.mime.base import MIMEBase
from email import encoders
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import zipfile

mypath=os.getcwd()


def Achive_Folder_To_ZIP(sFilePath):
    """
    input : Folder path and name
    output: using zipfile to ZIP folder
    """
    zf = zipfile.ZipFile(sFilePath + '.ZIP', mode='w')#只儲存不壓縮
    #zf = zipfile.ZipFile(sFilePath + '.ZIP', mode = 'w', compression = zipfile.ZIP_DEFLATED)#預設的壓縮模式
    os.chdir(sFilePath)
    #print sFilePath
    for root, folders, files in os.walk(".\\"):
        for sfile in files:
            aFile = os.path.join(root, sfile)
            #print aFile
            zf.write(aFile)
    zf.close()
 
 
if __name__ == "__main__":
    Achive_Folder_To_ZIP(mypath+'\\testlog0')#會將 C:\temp\FolderN 壓成 FolderN.zip 放在 C:\temp\ 裡面

#