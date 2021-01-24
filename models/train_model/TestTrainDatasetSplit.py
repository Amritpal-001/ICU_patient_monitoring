
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

        if shuffle == True:
            ListofAllFiles = random.shuffle(ListofAllFiles)
        if shuffle == False:
            pass
        numofFilesTransfered = 0
        for files in ListofAllFiles:
                while numofFilesTransfered <= PercentageSplit*(len(glob.glob(ParentDirectoryAddress , recursive=False))):
                    os.cp(files  , (CurrentTraindestination+'/'+os.path.basenamefiles))
                    ListofAllFiles.remove(files)
                    numofFilesTransfered += 1
                while numofFilesTransfered <= (len(glob.glob(ParentDirectoryAddress , recursive=False))):
                    os.cp(files  , (CurrentTestdestination +'/'+os.path.basenamefiles))
                    ListofAllFiles.remove(files)
                    numofFilesTransfered += 1


ParentfolderNameList = glob('images', recursive=False)
subfolders = [ f.path for f in os.scandir('images') if f.is_dir() ]
print(subfolders)

FileTransfer('./images', 0.7 , shuffle = True)