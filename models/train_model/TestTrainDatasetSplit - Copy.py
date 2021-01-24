
from glob import glob
import os
import random

def MakeTestTrainFolders(ParentDirectoryAddress):
    try:
        os.mkdir(os.path.join(ParentDirectoryAddress , 'Splitted'))
        os.mkdir(os.path.join(ParentDirectoryAddress , 'Spliited/train'))
        os.mkdir(os.path.join(ParentDirectoryAddress , 'Spliited/test'))
    except:
        print(ParentDirectoryAddress+'Splitted  - folder already exists')

def FileTransfer(ParentDirectoryAddress, PercentageSplit , shuffle = True):
    MakeTestTrainFolders(ParentDirectoryAddress)
    #ParentfolderNameList = glob(ParentDirectoryAddress, recursive=False)
    ParentfolderNameList = [f.path for f in os.scandir('images') if f.is_dir()]
    print(ParentfolderNameList)

    print("Length of ParentfolderNameList" , len(ParentfolderNameList))

    TrainDestination =  './'+ParentDirectoryAddress + 'Spliited/train'
    TestDestination = './'+ParentDirectoryAddress+'Spliited/test'

    for foldername in ParentfolderNameList:
        CurrentTraindestination = TrainDestination + foldername
        CurrentTestdestination = TestDestination + foldername
        try:
            os.mkdir(CurrentTraindestination)
            os.mkdir(CurrentTestdestination)
        except:
            print('Test and Train subdirectories already exist')

        print('FOlder name' , foldername)
        ListofAllFiles = glob(os.path.join(ParentDirectoryAddress, foldername), recursive=False)
        print("Number of files in " , foldername , len(ListofAllFiles))




